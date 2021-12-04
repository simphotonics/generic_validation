import pytest

from gvalidate import validate_in_interval, validate_positive


@validate_positive("length")
def f_positive(length, width):
    pass


@validate_positive()
def f_positive_check_all(length, width):
    pass


@validate_positive("length")
@validate_positive("width")
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
        with pytest.raises(ValueError):
            f_positive("not_a_number", width="a")

    def test_message(self):
        try:
            f_positive(-3, width=5)
        except ValueError as e:
            assert (
                "Invalid argument in function f_positive: "
                "length = -3. Must be positive." in str(e)
            )

    def test_all(self):
        with pytest.raises(ValueError):
            f_positive_check_all(
                5,
                width=-3,
            )


@validate_in_interval("width", left=10, right=20)
def f_in_interval(width):
    pass


@validate_in_interval("number", left=10, right=-20, right_inclusive=False)
def g_in_interval(number):
    pass


class TestValidateInInterval:
    def test_raised_exception(self):
        with pytest.raises(ValueError):
            f_in_interval(width=5)

    def test_raised_exception_incompatible_type(self):
        with pytest.raises(ValueError):
            f_in_interval("not_a_number")

    def test_message(self):
        try:
            f_in_interval(width=5)
        except ValueError as e:
            assert (
                "f_in_interval: width = 5. "
                "Input must satisfy: 10 <= 'input' <= 20." in str(e)
            )

    def test_message_inverted_boundaries(self):
        try:
            g_in_interval(number=-25)
        except ValueError as e:
            assert (
                "number = -25. Input must satisfy: -20 <= 'input' < 10."
                "" in str(e)
            )
