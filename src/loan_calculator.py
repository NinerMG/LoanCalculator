import math


class LoanCalculator:
    def __init__(self):
        print("What do you like to calculate?\n"
              "1. calculating the number of monthly payments\n"
              "2. calculating the monthly payment (the annuity payment)\n"
              "3. calculating the loan principal\n")
        self.choice = input()
        print(self.calculating_choice())

    def calculating_choice(self):
        if self.choice == "1":
            return self.calculating_the_number_of_monthly_payments()
        elif self.choice == "2":
           return self.calculating_monthly_payment()
        elif self.choice == "3":
            return self.calculating_loan_principal()
        else:
            return "Wrong choice"

    def calculating_the_number_of_monthly_payments(self):
        principal = int(input("principal="))
        payment = int(input("payment="))
        interest = int(input("interest="))
        i = interest / (12 * 100)
        n = math.log(payment / (payment - i * principal), 1 + i)
        n = math.ceil(n)
        years, months = divmod(n, 12)
        if years == 0:
             return f"It will take {months} months to repay this loan!"
        elif months == 0:
            return f"It will take {years} years to repay this loan!"
        else:
            return f"It will take {years} years and {months} months to repay this loan!"

    def calculating_monthly_payment(self):
        principal = int(input("principal="))
        periods = int(input("periods="))
        interest = float(input("interest="))

        i = interest / (12 * 100)
        payment = principal * (i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1)
        result = math.ceil(payment)
        return f"Your monthly payment = {result}!"

    def calculating_loan_principal(self):
        payment = float(input("payment="))
        periods = int(input("periods="))
        interest = float(input("interest="))

        i = interest / (12 * 100)
        principal = payment / ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1))
        result = math.floor(principal)
        return f"Your loan principal = {result}!"
