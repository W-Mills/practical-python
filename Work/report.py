# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
  '''
  Reads a portfolio, converts each holding into a dictionary and returns the collection
  '''
  portfolio = []

  with open(filename, 'rt') as f:
    rows = csv.reader(f)
    headers = next(rows)

    for row_num, row in enumerate(rows, start=1):
      try:
        # holding = { 'name': row[0], 'shares':int(row[1]), 'price': float(row[2]) }
        holding = dict(zip(headers, row))
        holding['shares'] = int(holding['shares'])
        holding['price'] = float(holding['price'])

        portfolio.append(holding)
      except IndexError:
        print(f'Line {row_num}: Error reading portfolio, index unavailable for:', row)
  return portfolio

def read_prices(filename):
  '''
  Reads prices, converts each key value into a dictionary and returns the collection
  '''
  prices = {}

  with open(filename, 'rt') as f:
    rows = csv.reader(f)
    for row_num, row in enumerate(rows, start=1):
      try:
        prices[row[0]] = float(row[1])
      except IndexError:
        print(f'Line {row_num}: Error reading prices, index unavailable for:', row)
  return prices

def make_report(portfolio, prices):
  '''
  Creates report that includes price change for each stock in a portfolio given a prices list
  '''
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

def print_report(report):
  '''
  Outputs report in a pretty tabular way
  '''

  headers = ('Name', 'Shares', 'Price', 'Change')
  print('%10s %10s %10s %10s' % headers)
  print(('-' * 10 + ' ') * len(headers))

  for r in report:
    name, shares, price, change = r
    print(f"{name:>10s} {shares:>10d} {'$' + str(price):>10s} {change:>10.2f}")

def portfolio_report(portfolio_file, prices_file):
  '''
  Reads data files, creates report data and prints it
  '''
  report = make_report(read_portfolio(portfolio_file), read_prices(prices_file))
  print_report(report)

portfolio_report('Data/portfolio.csv', 'Data/prices.csv')