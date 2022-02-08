"""
Tests the validator functions
Command line: python -m pytest tests/unit/test_validators.py
"""

import pytest
from app.utils.validators import validate_integer



def test_valid():
    validate_integer('arg', 10, 0, 20, 'custom min msg', 'custom max msg')

def test_type_error():
    with pytest.raises(TypeError):
        validate_integer('arg', 1.5)

def test_min_std_err_msg():
    with pytest.raises(ValueError) as ex:
        validate_integer('arg', 10, 100)
    assert 'arg' in str(ex.value)
    assert '100' in str(ex.value)

def test_min_custom_msg():
    with pytest.raises(ValueError) as ex:
        validate_integer('arg', 10, 100, custom_min_message='custom')
    assert str(ex.value) == 'custom'

def test_max_std_err_msg():
    with pytest.raises(ValueError) as ex:
        validate_integer('arg', 10, 1, 5)
    assert 'arg' in str(ex.value)
    assert '5' in str(ex.value)

def test_max_custom_err_msg():
    with pytest.raises(ValueError) as ex:
        validate_integer('arg', 10, 1, 5, custom_max_message='custom')
    assert str(ex.value) == 'custom'

#


