from masala.pretty_msg import print_error

def assert_step(value, expected = True) -> None:
    """Обвязка try...except конструкции вокруг стандартного assert

    Args:
        value (_type_): проверяемое значение
        expected (bool, optional): ожидаемое значение. Defaults to True.
    """
    try:
        assert value == expected
    except AssertionError as err:
        print_error(err)
    