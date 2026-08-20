# Simple Test Automation Script
# Tests basic calculator functions

def add(a, b):
    """Function to add two numbers"""
    return a + b

def subtract(a, b):
    """Function to subtract two numbers"""
    return a - b

def multiply(a, b):
    """Function to multiply two numbers"""
    return a * b

# Test Cases (checking if functions work correctly)
def test_addition():
    assert add(5, 3) == 8, "Addition test failed"
    assert add(-1, 1) == 0, "Negative number test failed"
    print("✅ Addition tests passed")

def test_subtraction():
    assert subtract(10, 5) == 5, "Subtraction test failed"
    assert subtract(0, 5) == -5, "Negative result test failed"
    print("✅ Subtraction tests passed")

def test_multiplication():
    assert multiply(4, 5) == 20, "Multiplication test failed"
    assert multiply(-2, 3) == -6, "Negative multiplication test failed"
    print("✅ Multiplication tests passed")

# Run all tests
if __name__ == "__main__":
    print("Starting test suite...\n")
    test_addition()
    test_subtraction()
    test_multiplication()
    print("\n🎉 All tests passed!")