while True:
    # Check for valid input for vehicle price
    while True:
        try:
            vehicle_price = float(input("Enter the price of your vehicle (in cedis): "))
            if vehicle_price <= 0:
                raise ValueError("Please enter a positive number.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    insurance_rates = [0, 0.08, 0.15, 0.20, 0.30]

    if vehicle_price < 20000:
        insurance_rate = insurance_rates[0]
    elif vehicle_price < 100000:
        insurance_rate = insurance_rates[1]
    elif vehicle_price < 800000:
        insurance_rate = insurance_rates[2]
    elif vehicle_price < 1800000:
        insurance_rate = insurance_rates[3]
    else:
        insurance_rate = insurance_rates[4]

    insurance_amount = vehicle_price * insurance_rate

    total_yearly_cost = insurance_amount * 12 - 1000

    # Offer the option to subscribe to yearly insurance
    subscribe_choice = input("Do you want to subscribe to yearly insurance payment? (yes/no): ").lower()
    if subscribe_choice == 'yes':
        print(f"Yearly insurance payment amount: {total_yearly_cost:.2f} cedis")
    else:
        if insurance_rate > 0:
            print(f"Insurance tax ({insurance_rate*100}%): {insurance_amount:.2f} cedis must be paid into your insurance account.")
        elif insurance_rate == 0:
            print("No insurance tax must be paid, as it is covered by the government.")

    choice = input("Do you want to calculate insurance for another vehicle? (yes/no): ").lower()
    if choice != 'yes':
        break
