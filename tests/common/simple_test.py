import pytest

# Fixture defined on the level of this specific test script
@pytest.fixture
def second_input_value():
    input = 10
    return input

# Adding first_set marker on the specific test (to be able to group tests per specific functionality)
# Markers are defined in pyproject.toml file
@pytest.mark.first_set
def test_equality(input_value, second_input_value):
    assert input_value == second_input_value

@pytest.mark.second_set
def test_greater(input_value):
    assert input_value < 20

@pytest.mark.third_set
def test_output(define_inputs):
    for x in define_inputs:
        assert x > 5

# Beside adding first_set marker to the test, we are also parametrizing test so it will be executed for specified set of input values
@pytest.mark.first_set
@pytest.mark.parametrize("first_value, second_value",[(11,11),(22,22),(35,35),(44,44)])
def test_equality_with_params(first_value, second_value):
    assert first_value == second_value