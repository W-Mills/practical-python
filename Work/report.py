# report.py

import fileparse

def read_portfolio(filename):
  '''
  Reads a portfolio, converts each holding into a dictionary and returns the collection
  '''
  return fileparse.parse_csv(filename, types=[str,int,float])

def read_prices(filename):
  '''
  Reads prices, converts each key value into a dictionary and returns the collection
  '''
  prices = fileparse.parse_csv(filename, has_headers=False, types=[str, float])
  return dict(prices)

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
  portfolio = read_portfolio(portfolio_file)
  prices = read_prices(prices_file)
  report = make_report(portfolio, prices)
  print_report(report)

def main(args):
  if len(args) != 3:
    raise SystemExit('Usage: %s portfolio_file prices_file' % args[0])
  portfolio_report(args[1], args[2])

if __name__ == '__main__':
  import sys
  main(sys.argv)

# portfolio_report('Data/portfolio.csv', 'Data/prices.csv')