import pandas as pd
from langchain_core.documents import Document

class DataConverter:
    def __init__(self,file_path:str):
        self.file_path = file_path
    
    def convert(self):
        df=pd.read_csv(self.file_path)[["product_title","review"]]
        
        docs = []
        for index, row in df.iterrows():
            # 1. Glue the Title and the Review together into one string
            combined_text = f"Product Title: {row['product_title']}\nReview: {row['review']}"
            
            # 2. (Optional but highly recommended) Save the title in the metadata too
            metadata = {
                "product_title": row['product_title'],
                "rating": row['rating']
            }
            
            # 3. Create the document with the combined text
            doc = Document(page_content=combined_text, metadata=metadata)
            docs.append(doc)
        
        return docs