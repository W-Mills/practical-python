# fileparse.py
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
  '''
  Parse a CSV file into a list of records
  '''
  # Raise exception on invalid option combination
  if has_headers == False and select != None:
    raise RuntimeError('select argument requires headers')

  with open(filename) as f:
    rows = csv.reader(f, delimiter=delimiter)

    # Read the file headers if exist
    if has_headers:
      headers = next(rows)
    else:
      headers = []

    # If specific columns have been selected, make indices for filtering
    if select:
      indices = [headers.index(colname) for colname in select]
      headers = select

    records = []
    for row_num, row in enumerate(rows, start=1):
      try:
        if not row: # Skip rows with no data
          continue

        # Filter the row if specific columns were selected
        if select:
          row = [ row[index] for index in indices ]

        # Perform type conversion if supplied
        if types:
          row = [func(val) for func, val in zip(types, row) ]

        # Make a dictionary or a tuple
        if headers:
          record = dict(zip(headers, row))
        else:
          record = tuple(row)
        records.append(record)
      except ValueError as e:
        if silence_errors == True:
          continue
        else:
          print(f"Line {row_num}: Couldn't convert {row}")
          print(f"Line {row_num}: Reason {e}")

    return records
