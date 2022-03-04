from fizzbuzz_fortest import fizzbuzz

def test_multiple_of_three():
    result = fizzbuzz(6)
    assert result == 'Fizz'

def test_multiple_of_five():
    result = fizzbuzz(20)
    assert result == 'Buzz'

def test_fizzbuzz():
    result = fizzbuzz(15)
    assert result == 'FizzBuzz'

