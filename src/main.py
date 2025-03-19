import math

loan_principal = int(input("Enter the loan principal: "))

kind_of_calculation = input('What do you want to calculate? \n'
                            'type "m" - for number of monthly payments,\n'
                            'type "p" - for the monthly payment: ')

if kind_of_calculation == 'm':
    monthly_payment = int(input("Enter the monthly payment: "))
    months_to_pay = math.ceil(loan_principal / monthly_payment)
    print(f"It will take {months_to_pay} months to repay the loan")

elif kind_of_calculation == 'p':
    months_number = int(input("Enter the number of months: "))
    monthly_payment = math.ceil(loan_principal / months_number)
    last_payment = loan_principal - (months_number - 1) * monthly_payment
    if last_payment == monthly_payment:
        print(f"Your monthly payment = {monthly_payment}")
    else:
        print(f"Your monthly payment = {monthly_payment} and the last payment = {last_payment}.")
