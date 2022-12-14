"""Generate all dates from 0001-01-01 to 9999-12-31"""

from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(1, 1, 1)
end_date = date(9999, 12, 31)

for single_date in daterange(start_date, end_date):
    print(single_date.strftime("%Y-%m-%d"))
