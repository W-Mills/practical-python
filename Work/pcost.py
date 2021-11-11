# pcost.py
#
# Exercise 1.27

# with open('/Users/wmills/codes/practical-python/Work/Data/portfolio.csv', 'rt') as file:
#   headers = next(file)
#   total = 0

#   for line in file:
    # row = line.split(',')
    # cost = float(row[2])
    # quantity = int(row[1])
    # total += (cost * quantity)

# print(total)


# import gzip

# with gzip.open('/Users/wmills/codes/practical-python/Work/Data/portfolio.csv.gz', 'rt') as file:
#   for line in file:
#     print(line, end='')

import csv
import sys

def portfolio_cost(filename):
  total = 0

  with open(filename, 'rt') as file:

    rows = csv.reader(file)
    headers = next(rows)

    for row_num, row in enumerate(rows, start=1):
      record = dict(zip(headers, row))
      try:
        num_shares = int(record['shares'])
        price_shares = float(record['price'])
        total += (price_shares * num_shares)
      except ValueError:
        print(f"Row {row_num}: Couldn't convert: {row}")

  return total


# print(portfolio_cost('/Users/wmills/codes/practical-python/Work/Data/portfolio.csv'))

if len(sys.argv) == 2:
  filename = sys.argv[1]
else:
  filename = '/Users/wmills/codes/practical-python/Work/Data/missing.csv'
  # filename = 'non-existent path'

cost = portfolio_cost(filename)
print('Total cost:', cost)