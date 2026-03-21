import sys

class CustomException(Exception):
    def __init__(self, message:str,error_details:Exception=None):
        self.error_message=self.get_detailed_error_message(message, error_details)
        super().__init__(self.error_message)
    
    @staticmethod
    def get_detailed_error_message(message, error_detail):
        _,_,exc_tb=sys.exc_info()
        file_name= exc_tb.tb_frame.f_code.co_filename
        line_number=exc_tb.tb_lineno
        
        return (f"{message} | "
                f"Error message: {error_detail} |"
                f"Error occurred in File name: {file_name} |"
                f"Line number: {line_number}")

    def __str__(self):
        return self.error_message

