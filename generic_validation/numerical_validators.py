'''
Provides the following decorator functions for validating
numerical function arguments:

- validate_positive
'''

from .generic_validators import validate


def validate_positive(argument_names: tuple, enable_warnings=True):
    '''
    Raises an exception if any argument listed in `argument_names`
    is not positive.

    ---
    Usage: In the example below the decorator checks if the argument
    `width` is positive:
    ``` python
    @validate_positive('width')
    def my_func(id, width = 10):
        pass
    ```
    '''
    return validate(
        argument_names,
        validator=lambda input: input > 0,
        message='Must be positive.',
        enable_warnings=enable_warnings,
    )
