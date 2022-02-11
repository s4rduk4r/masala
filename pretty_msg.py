from termcolor import colored

"""Exception and other critical message
"""
def print_error(error : Exception) -> None:
    print(colored(f"{error.__class__.__name__}: {error}", color = "red"))
    
"""Normal info message
"""
def print_msg(msg : str) -> None:
    print(colored(msg, color = "blue"))
    
"""Warning message
"""
def print_warn(msg : str) -> None:
    print(colored(msg, color = "magenta"))
