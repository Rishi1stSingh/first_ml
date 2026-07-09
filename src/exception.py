import sys
from src.logger import logging


def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message =f'error happened in file {file_name} and at line {exc_tb.tb_lineno} and error is {error}'

    return error_message
    


class custom_exception(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail)


    def __str__(self):
        return self.error_message
    

if __name__=="__main__":
    try:
        print(10/0)
    except Exception as e:
        logging.info("zero_divison_error")
        raise custom_exception(str(e),sys)