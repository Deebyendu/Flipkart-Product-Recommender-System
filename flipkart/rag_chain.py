from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_classic.chains.history_aware_retriever import create_history_aware_retriever
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain
from flipkart.data_ingestion import DataIngestion
from flipkart.config import Config
class RagChainBuilder:
    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.model = ChatGroq(
            model=Config.RAG_MODEL,
            temperature=0,
            api_key=Config.GROQ_API_KEY
        )
        self.history_store = {} 
        self.chain = self.build_chain()

    def _get_history(self, session_id: str) -> BaseChatMessageHistory:
        if session_id not in self.history_store:
            self.history_store[session_id] = ChatMessageHistory()
        return self.history_store[session_id]
    
    def build_chain(self):
        retriever = self.vector_store.as_retriever(search_type="mmr",
            search_kwargs={"k": 15, "fetch_k": 40})
        
        context_prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a query reformulation assistant. Your only task is to rewrite a user's follow-up question into a clear, self-contained query.
            INSTRUCTIONS:
            1. Read the provided chat history to understand the context.
            2. Read the latest user question.
            3. Replace any pronouns (e.g., "it", "they", "this") or implied subjects in the latest question with the specific names or items from the chat history.
            4. Output ONLY the rewritten question. Do not provide an answer, explanation, or conversational filler."""),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}")
        ])
        
        qa_prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a highly knowledgeable e-commerce shopping assistant. Your primary goal is to help users by answering questions about products using ONLY the provided CONTEXT.
            CRITICAL RULES:
            1. Product Names: When a user asks for the names of products (like headphones or earphones), you MUST extract and provide the official Product Title (e.g., "BoAt Rockerz 235v2"). Do NOT quote how users describe the item in the reviews (e.g., do not say "Super super head phones") as the product name.
            2. Grounding: Base your answer strictly on the information provided in the CONTEXT below. Do not use outside knowledge or assume product features.
            3. Unknowns: If the CONTEXT does not contain the answer, or if you cannot find the official product title, politely state: "I don't have enough information in the current product data to answer that." Do not guess or hallucinate.
            4. Conciseness: Keep your answers brief, direct, and helpful. Focus on extracting the most relevant details.
            
            CONTEXT:
            {context}"""),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}")
        ])
        history_aware_retriever = create_history_aware_retriever(self.model, retriever, context_prompt)
        
        question_answer_chain = create_stuff_documents_chain(self.model, qa_prompt)
        
        rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
        
        chain_with_history = RunnableWithMessageHistory(
            rag_chain,
            self._get_history,
            input_messages_key="input",
            history_messages_key="chat_history",
            output_messages_key="answer"
        )
        
        return chain_with_history
