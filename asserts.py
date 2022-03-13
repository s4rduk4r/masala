from masala.pretty_msg import print_error

def assert_step(expression : bool) -> None:
    """Обвязка try...except конструкции вокруг стандартного assert

    Args:
        expression (bool)   :   выражение для assert
        err_msg (str)       :   сообщение о природе ошибки
    """
    try:
        assert expression
    except AssertionError as err:
        print_error(err)
    
    
def assert_step2(expression : bool, error_to_print : Exception) -> None:
    """Обвязка try...except конструкции вокруг стандартного assert

    Args:
        expression (bool): выражение для assert
        error_to_print (Exception): сообщение о природе ошибки
    """
    try:
        assert expression
    except AssertionError:
        print_error(error_to_print)
    