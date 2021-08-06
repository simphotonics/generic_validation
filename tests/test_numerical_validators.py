import pytest

from generic_validation.numerical import validate_positive


@validate_positive('length')
def f_positive(length, width):
    pass


@validate_positive(())
def f_positive_check_all(length, width):
    pass

@validate_positive('length')
@validate_positive('width')
def f_positive_nested(length, width):
    pass

class TestValidatePositive:
    def test_raised_exception_pos(self):
        with pytest.raises(ValueError):
            f_positive(-3, width=5)

    def test_raised_exception_keyword(self):
        with pytest.raises(ValueError):
            f_positive_nested(3, width=-5)

    def test_raised_exception_incompatible_type(self):
        with pytest.raises(TypeError):
            f_positive('not_a_number', width='a')

    def test_message(self):
        try:
            f_positive(-3, width=5)
        except ValueError as e:
            assert 'Invalid argument at position: 0. '
            'Value: -3. Must be positive.' in str(e)

    def test_all(self):
        with pytest.raises(ValueError):
            f_positive_check_all(5, width=-3, )
