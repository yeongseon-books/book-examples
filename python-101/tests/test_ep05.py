from en.ep05_control_flow import fizzbuzz


def test_fizzbuzz() -> None:
    result = fizzbuzz(15)
    assert result[2] == "Fizz"
    assert result[4] == "Buzz"
    assert result[14] == "FizzBuzz"
