# Generic Validation For Python

Checking the input arguments of a function is a common task.
It allows the software designer to stop the flow of execution if
an error occured and to display information detailing the error.

Python provides *decorators* that can be used to add extra
functionality to a function. The package [`generic_validation`][generic_validation]
provides the function [`validate`][validate] that
can be used to easily create argument validating decorators while avoiding most of the
required boilerplate.

## Installation

To install the package [`generic_validation`][generic_validation] use the command:
```Console
$ pip install -i https://test.pypi.org/simple/ generic-validation-simphotonics
```

## Usage

This section demonstrates how to use the function [`validate`][validate]
to define validation decorators.

### Generic Validation Decorators

The example below shows how to define a decorator that will validate
the arguments of the decorated function and
raise an exception of type `ValueError` if any argument does not pass validation.

The most important ingredient is the function provided as `validator`.
This function must accept one argument (the one
being validated) and return a boolean.
If it returns `False` validation fails.
The function [`validate`][validate] is generic in the sense that we
can pass any function with the required signature as a validator.



``` python
from generic_validation.generic_validators import validate

@validate(argument_names = (),
             validator = lambda x: x > 0,
             message='Dimensions must be positive.' # Optional, default: ''
             error_type=ValueError,               # Optional, default: ValueError
             enable_warnings=True                 # Optional, default: True
             )
def box_dimensions(length, height, width):
  pass
```
To validate an argument it must be listed in the tuple `argument_names`.

As a convenience, the following syntax is also accepted:

- To validate a *single* argument one may pass the name of the argument as a string:
`@validate('length', validator = lambda x: x > 0)`.
- To a validate *all* arguments  an empty tuple may be passed as `argument_names`:
`@validate((), validator = lambda x: x > 0)`.

Calling the function `box_dimensions` with negative arguments
causes an exception to be raised:
``` python
box_dimensions(-1, 10, 20)
# ... stack trace will be printed here
ValueError: ('Invalid argument in function box_dimensions: length = -10.'
             'Dimensions must be positive.')

```
The argument `message` passed to the decorator is appended to the
message attached to the exception. In the example above `message` was:
'Dimensions must be positive'.

### Concrete Validation Decorators

In the example above, we defined a validating decorator on the spot
using the generic method [`validate`][validate].
To reuse a validating decorator that uses a specific validator
one may define a separate function.

In the example below the decorator `validate_callable` checks if the
specified arguments are callable.
```Python
def validate_callable(argument_names: tuple, enable_warnings=True):
    '''
    Raises an exception if any argument in `argument_names` is not callable.
    '''
    return validate(
        argument_names,
        validator=lambda input: callable(input),
        message='Must be callable.',
        enable_warnings=enable_warnings,
        )

# Using the decorator defined above.
@validate_callable(('callback',))
def function_with_a_callback(id: int, callback: callable):
    pass

```

Ready made validation decorators can be found in the modules:

- `function_validators`
- `numerical_validators`
- `string_validators`

### Disabling Warnings

Any invalid argument name listed in the tuple `argument_names`
will be silently ignored if `enable_warnings` is explicitly set to `False`.
Consider the function below:
``` python
from generic_validation.generic_validators import validate

@validate(argument_names = ('aeg',),
             validator = lambda x: x > 0,
             message='Age must be positive.',
             enable_warnings=False
             )
def person_data(age, name):
  pass
```
Calling the function with the arguments: `person_data(age = -10, name = 'Anna')`
will *pass* validation since the argument name `aeg` specified
in the decorator does not exist.

## Nested validators

Several decorators performing validation
may be applied to the same function.
In that case, validation starts with the top-most decorator.
Stacking decorators allows fine grained validation.

In the example below, we check that `length` is positive and `callback` is callable:
```Python
@gv.validate_positive('length')
@gv.validate_callable('callback')
def g(length, callback):
    '''
    Used to test nested validation decorators.
    '''
    pass
```

Note: Stacked decorators are in fact nested decorators. To allow
access to the signature of the decorated
function from within nested decorators
[`functools.wraps`](https://docs.python.org/3/library/functools.html#functools.wraps)
was used. For more details check out the implementation of [`validate`][validate].

## Testing

To run the tests clone the project source code available at
[`generic_validation`](https://github.com/simphotonics/generic_validation)
using the command:
```
$ git clone https://github.com/simphotonics/generic_validation.git
```
The command above will create a directory called `generic_validation`.
Then navigate to directory `generic_validation` and use the commands:
```Console
$ make init
$ make test
```
The first command will install [`pytest`][pytest]. The second command
will run the unit tests located in the sub-directory `tests`.

## Contributing

Contributions are welcome. To add validators that are useful to you
or other users please create a pull request or equest to be added
as a collaborator.

The following steps should be considered when creating a pull request:

1. Add validators to existing modules for example `string_validators` or
   alternatively create a new module.

2. Document the added functions. Add a doc entry to the top of the module.
   Add a doc entry to `__init__.py` if a new module was added.
   Consider adding documentation to `README.md`.

3. Add tests to unit test the added functions.


## Features and bugs

Please file feature requests and bugs at the [issue tracker].


[issue tracker]: https://github.com/simphotonics/generic_validation/issues

[generic_validation]: https://github.com/simphotonics/generic_validation

[pytest]: https://pypi.org/project/pytest/

[validate]: https://generic-validation.simphotonics.com/reference/generic_validation/generic_validators/#validate