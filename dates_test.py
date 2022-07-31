from dates import *

def test_is_valid_format_negative() -> None:
    """Tests for dates that have an invalid format"""

    assert False == is_valid_format("definitely not valid") # invalid length
    assert False == is_valid_format("helloworld") # valid length, no separators/numbers
    assert False == is_valid_format("----------") # valid length, no numbers
    assert False == is_valid_format("1234567890") # valid length, no separators
    assert False == is_valid_format("1000-12.01") # valid length, invalid separators
    assert False == is_valid_format("2020 10 03") # valid length, invalid separators
    assert False == is_valid_format("1950-10-3") # invalid length
    assert False == is_valid_format("abcd-ef-gh") # valid length, invalid date
    assert False == is_valid_format("1b3d-12-g1") # valid length, invalid date
    assert False == is_valid_format("1965-a1-03") # valid length, invalid date
    assert False == is_valid_format("193-01--05") # valid length, invalid separators

def test_is_valid_format_positive() -> None:
    """Tests for dates that have a valid format"""

    assert True == is_valid_format("2020-01-01")
    assert True == is_valid_format("1900-12-05")

def test_is_valid_date_negative() -> None:
    """Tests for dates that are invalid, eg. 31st of September"""

    assert False == is_valid_date("0000-00-00") # year, month, day must be > 0
    assert False == is_valid_date("0001-00-00") # year, month, day must be > 0
    assert False == is_valid_date("0001-01-00") # year, month, day must be > 0
    assert False == is_valid_date("0000-01-01") # year, month, day must be > 0
    assert False == is_valid_date("1900-13-21") # month is invalid
    assert False == is_valid_date("2022-02-29") # not a leap year
    assert False == is_valid_date("1900-09-31") # september has 30 days
    assert False == is_valid_date("1950-09-70") # invalid day
    assert False == is_valid_date("1550-00-90") # invalid month and day

def test_is_valid_date_positive() -> None:
    """Tests for dates that are valid"""

    assert True == is_valid_date("2020-02-29") # leap year
    assert True == is_valid_date("0001-01-01")
    assert True == is_valid_date("2020-03-01")
    assert True == is_valid_date("2020-12-31")

def test_date_algorithm() -> None:
    """Calculates the julian day number for a range of dates
    and ensures they are linearly increasing
    """

    # Get all the dates
    with open("tests/test_date_algorithm/check_date_algorithm.txt", "r") as file:
        ls = []
        for date in file:
            date_object = init_date_object(date)
            jdn = get_julian_day_number(date_object)
            ls.append(jdn)

    # Ensure that the n'th date is n days from the 0th date
    for i in range(len(ls)):
        assert i == (ls[i] - ls[0])

def test_e2e() -> None:
    """Iterates through 1M random date pairs and compares the result
    of my own implementation with the python datetime library
    """

    # Iterate through the file
    with open("tests/test_random_date_pairs/random_date_pairs.txt", "r") as file:
        # Check all the dates
        for date in file:
            first_date, second_date = date.strip("\n").split(",")

            assert True == is_valid_date(first_date)
            assert True == is_valid_date(second_date)

            first_date_object = init_date_object(first_date)
            second_date_object = init_date_object(second_date)

            difference = calculate_difference(first_date_object, second_date_object)
            true_difference = calculate_true_difference(first_date_object, second_date_object)

            # Compare program output to datetime output
            assert difference == true_difference