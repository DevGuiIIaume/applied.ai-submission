"""Generate 1M random date pairs and write the result to a txt file"""

from datetime import date
import random

ls = []
with open("./test_date_algorithm/check_date_algorithm.txt", "r") as file:
    for date in file:
        ls.append(date)

with open("random_date_pairs.txt", "w") as file:
    for i in range(1000000):
        first_idx = random.randint(0, 3000000)
        second_idx = random.randint(0, 3000000)

        first_date = ls[first_idx].strip("\n")
        second_date = ls[second_idx]

        file.write(f"{first_date},{second_date}")
