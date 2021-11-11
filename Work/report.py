# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
  '''Reads a portfolio, converts each holding into a dictionary and returns the collection'''
  portfolio = []

  with open(filename, 'rt') as f:
    rows = csv.reader(f)
    headers = next(rows)

    for row_num, row in enumerate(rows, start=1):
      try:
        # holding = { 'name': row[0], 'shares':int(row[1]), 'price': float(row[2]) }
        holding = dict(zip(headers, row))
        portfolio.append(holding)
      except IndexError:
        print(f'Line {row_num}: Error reading portfolio, index unavailable for:', row)
  return portfolio

def read_prices(filename):
  '''Reads prices, converts each key value into a dictionary and returns the collection'''
  prices = {}

  with open(filename, 'rt') as f:
    rows = csv.reader(f)
    for row_num, row in enumerate(rows, start=1):
      try:
        prices[row[0]] = float(row[1])
      except IndexError:
        print(f'Line {row_num}: Error reading prices, index unavailable for:', row)
  return prices

# def portfolio_value_difference(portfolio_file, prices_file):
#   portfolio = read_portfolio(portfolio_file)
#   prices = read_prices(prices_file)
#   initial_portfolio_value = 0.0
#   current__portfolio_value = 0.0

#   for holding in portfolio:
#     try:
#       initial_portfolio_value += holding['shares'] * holding['price']
#       current_stock_price = float(prices[holding['name']])
#       current__portfolio_value += holding['shares'] * current_stock_price
#     except KeyError:
#       print('KeyError while calculating value difference for holding:', holding)

#   return current__portfolio_value - initial_portfolio_value

# print('Value difference: $', round(portfolio_value_difference('Data/portfolio.csv', 'Data/prices.csv'), 2))

def make_report(portfolio, prices):
  items = []
  
  for s in portfolio:
    try:
      current_price = prices[s['name']]
    except KeyError:
      print('KeyError accessing current price for stock', s)
      pass
    price_difference = current_price - float(s['price'])
    t = (s['name'], s['shares'], current_price, price_difference)

    items.append(t)
    
  return items

# Read data files and create the report data

# portfolio = read_portfolio('Data/portfolio.csv')
portfolio = read_portfolio('Data/portfoliodate.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

# Output the report

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
# space = ' '
# print(f'{space:-<10} {space:-<10} {space:-<10} {space:-<10}')

for r in report:
  name, shares, price, change = r
  print(f"{name:>10s} {shares:>10s} {'$' + str(price):>10s} {change:>10.2f}")
