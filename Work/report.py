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

    for row in rows:
      try:
        holding = { 'name': row[0], 'shares':int(row[1]), 'price': float(row[2]) }
        portfolio.append(holding)
      except IndexError:
        print('Error reading portfolio, index unavailable for:', row)
  return portfolio

def read_prices(filename):
  '''Reads prices, converts each key value into a dictionary and returns the collection'''
  prices = {}

  with open(filename, 'rt') as f:
    rows = csv.reader(f)
    headers = next(rows)

    for row in rows:
      try:
        prices[row[0]] = row[1]
      except IndexError:
        print('Error reading prices, index unavailable for:', row)
  return prices

def portfolio_value_difference(portfolio_file, prices_file):
  portfolio = read_portfolio(portfolio_file)
  prices = read_prices(prices_file)
  initial_portfolio_value = 0.0
  current__portfolio_value = 0.0

  for holding in portfolio:
    try:
      initial_portfolio_value += holding['shares'] * holding['price']
      current_stock_price = float(prices[holding['name']])
      current__portfolio_value += holding['shares'] * current_stock_price
    except KeyError:
      print('KeyError while calculating value difference for holding:', holding)

  return current__portfolio_value - initial_portfolio_value

print('Value difference: $', round(portfolio_value_difference('Data/portfolio.csv', 'Data/prices.csv'), 2))
