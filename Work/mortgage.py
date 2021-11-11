# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
payment_number = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

monthly_amount = 1 + rate / 12

while principal > 0:
  payment_number += 1

  if payment_number >= extra_payment_start_month and payment_number <= extra_payment_end_month:
    principal -= extra_payment
    total_paid += extra_payment

  if payment > principal:
    payment = principal * monthly_amount
  
  principal = principal * monthly_amount - payment
  total_paid = total_paid + payment
  
  print(payment_number, round(total_paid, 2), round(principal, 2))

print('')
print('Total paid:', round(total_paid, 2))
print('Months', payment_number)