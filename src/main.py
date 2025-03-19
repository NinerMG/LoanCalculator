import math

loan_principal = int(input("Enter the loan principal: "))
monthly_payment = int(input("Enter the monthly payment: "))

months_to_pay = math.ceil(loan_principal / monthly_payment)

print(f"It will take {months_to_pay} months to repay the loan")