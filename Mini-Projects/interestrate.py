def main():
    print("THIS IS MONTHLY PAYMENT LOAN CALCULATOR\n")


    principal = float(input("THE LOAN AMOUNT"))
    apr = float(input("ENTER THE ANNUAL INTEREST RATE"))
    years = int(input("ENTER THE AMOUNT OF YEARS: "))


    monthly_interest_rate = apr/1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate/(1 - (1+monthly_interest_rate)** (-amount_of_months))


    print(f"THE MONTHLY PAYMENT FOR THIS LOAN IS {monthly_payment}")