import sys
from src.logger import logging


def get_error_details(error, error_detail:sys):

    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno

    error_details = f"Error Occured in Python Script: {file_name}, Line No.: {line_no} & Error: {str(error)}"

    return error_details


class CustomException(Exception):
    def __init__(self, error, error_detail:sys):
        super().__init__(error)
        self.error = get_error_details(error, error_detail) 

    def __str__(self):
        return self.error
