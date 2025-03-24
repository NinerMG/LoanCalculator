import argparse
import math


def calculate_diff_payments(principal, periods, interest):
    i = interest / (12 * 100)
    total_payment = 0

    for m in range(1, periods + 1):
        d_m = math.ceil((principal / periods) + i * (principal - (principal * (m - 1) / periods)))
        total_payment += d_m
        print(f"Month {m}: payment is {d_m}")

    overpayment = total_payment - principal
    print(f"\nOverpayment = {overpayment}")


def calculate_annuity(principal=None, payment=None, periods=None, interest=None):
    i = interest / (12 * 100)

    if principal is None:
        principal = math.floor(payment / ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1)))
        print(f"Your loan principal = {principal}!")
    elif payment is None:
        payment = math.ceil(principal * (i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1))
        print(f"Your annuity payment = {payment}!")
    elif periods is None:
        periods = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
        years, months = divmod(periods, 12)
        if years == 0:
            print(f"It will take {months} months to repay this loan!")
        elif months == 0:
            print(f"It will take {years} years to repay this loan!")
        else:
            print(f"It will take {years} years and {months} months to repay this loan!")

    overpayment = (payment * periods) - principal
    print(f"Overpayment = {overpayment}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", choices=["annuity", "diff"], required=True)
    parser.add_argument("--principal", type=float)
    parser.add_argument("--payment", type=float)
    parser.add_argument("--periods", type=int)
    parser.add_argument("--interest", type=float, required=True)

    args = parser.parse_args()

    if args.interest is None or args.interest <= 0:
        print("Incorrect parameters")
        return

    if args.type == "diff":
        if args.payment is not None or not all([args.principal, args.periods]):
            print("Incorrect parameters")
            return
        calculate_diff_payments(args.principal, args.periods, args.interest)

    elif args.type == "annuity":
        params = [args.principal, args.payment, args.periods]
        if sum(p is not None for p in params) != 2:
            print("Incorrect parameters")
            return
        calculate_annuity(args.principal, args.payment, args.periods, args.interest)


if __name__ == "__main__":
    main()
