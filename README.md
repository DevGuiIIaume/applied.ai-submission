## annalise.ai technical submission

Welcome to my dates.py program!

#### Usage
To run my program, type: *python3 dates.py*

#### Overview of solution
This programs gets user input from stdin, verifies the validity of the input, and calculates the difference between two dates

To determine the difference between two days, the Gregorian calendar date (YYYY-MM-DD) is converted into its corresponding Julian day number, a continuous count of days since the beginning of the Julian period

This means that to calculate the difference between two Gregorian calendar dates, you can convert them into their Julian day numbers and subtract them from one another

The algorithm to convert from Gregorian calendar date to Julian day number was found in the following publication: https://www.researchgate.net/publication/316558298_Date_Algorithms

#### Verifying correctness
I have written extensive testcases to ensure the correctness of my program
- I consider negative cases such as invalid formats and invalid dates eg. 29th of Feb 2022
- I generated all dates from 0001-01-01 to 9999-12-31 and checked that my algorithm to calculate the julian day number was correct
- I also generated 1M random date pairs and checked that my program matched with the output of datetime, a python library

To run my testcases and to generate a code coverage html report, type: *pytest --cov=dates --cov-report=html*
