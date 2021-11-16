"""Testing Division"""
from calculator.calculations.division import Division

def test_calculation_subtraction():
    """testing that our calculator has a static method for multiplication"""
    #Arrange
    nums = (8.0,2.0)
    division = Division(nums)
    #Act
    #Assert
    assert division.get_result() == 4.0

def test_division_throws_exception():
    """test divide by 0 raises error"""
    nums = (8.0, 0.0)
    err_test = Division(nums)
    with pytest.raises(Exception) as err:
        err_test.get_result()
    assert err.type == ZeroDivisionError
