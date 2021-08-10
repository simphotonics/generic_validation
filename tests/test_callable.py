import pytest

from generic_validation.callable import validate_callable


@validate_callable(('callback'))
def f_callable(func, callback):
    pass


def g():
    pass


class TestValidateCallable:
    def test_raised_exception_keyword(self):
        with pytest.raises(ValueError):
            f_callable(g, callback=-5)

    def test_message(self):
        try:
            f_callable(lambda x: x, callback=5)
        except ValueError as e:
            assert 'Invalid argument in function f_callable: ' \
            'callback = 5. Must be callable.' in str(
                e)
