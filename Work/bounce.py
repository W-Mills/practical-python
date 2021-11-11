# bounce.py
#
# Exercise 1.5

bounce_height = 100 # meters
bounce_num = 0

while bounce_num < 10:
  bounce_num += 1
  bounce_height = bounce_height * (3 / 5)

  print(bounce_num, round(bounce_height, 4))