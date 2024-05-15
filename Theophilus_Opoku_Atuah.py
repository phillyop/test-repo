# Get the withdrawal amount from the customer
withdrawal_amount = float(input("Enter the amount to be transferred by the customer (in cedis): "))

# Define tax rates
tax_rates = [0, 0.05, 0.10, 0.15, 0.20]

# Determine the appropriate tax rate based on withdrawal amount
if withdrawal_amount < 100:
    tax_rate = tax_rates[0]
elif withdrawal_amount < 500:
    tax_rate = tax_rates[1]
elif withdrawal_amount < 1000:
    tax_rate = tax_rates[2]
elif withdrawal_amount < 5000:
    tax_rate = tax_rates[3]
else:
    tax_rate = tax_rates[4]

# Calculate the tax amount to be deducted
tax_amount = withdrawal_amount * tax_rate

# Calculate the total amount to be transferred (withdrawal amount + tax amount)
total_amount = withdrawal_amount + tax_amount

# Inform the customer about the deduction and total amount
if tax_amount > 0:
    print(f"Tax ({tax_rate*100}%): {tax_amount:.2f} cedis will be deducted from your account.")
else:
    print("No tax will be deducted from your account.")

print(f"Total amount to be transferred: {total_amount:.2f} cedis")
