"""
Colored output messages
"""
from termcolor import colored

def print_error(error : Exception) -> None:
    """
    Exception and other critical message
    """
    print(colored(f"{error.__class__.__name__}: {error}", color = "red"))
    
def print_msg(msg : str) -> None:
    """
    Normal info message
    """
    print(colored(msg, color = "blue"))
    
def print_warn(msg : str) -> None:
    """
    Warning message
    """
    print(colored(msg, color = "magenta"))
