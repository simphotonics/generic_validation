import pytest

from gvalidation import validate_non_whitespace


@validate_non_whitespace(("id"))
def f_non_whitespace(id: str, name: str):
    pass


@validate_non_whitespace(())
def f_non_whitespace_check_all(id: str, name: str):
    pass


class TestValidatePositive:
    def test_raised_exception_pos(self):
        with pytest.raises(ValueError):
            f_non_whitespace("", name="Anna")

    def test_raised_exception_keyword(self):
        with pytest.raises(ValueError):
            f_non_whitespace("one ", name="\n")

    def test_raised_exception_incompatible_type(self):
        with pytest.raises(AttributeError):
            f_non_whitespace(0, name="Marc")

    def test_message(self):
        try:
            f_non_whitespace("\n", name="Paul")
        except ValueError as e:
            assert "Invalid argument at position: 0. "
            "Value: -3. Must be positive." in str(e)

    def test_all(self):
        with pytest.raises(ValueError):
            f_non_whitespace_check_all("", name="Naomi")
