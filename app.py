def show_menu():
    print("\n--- Sree's Multi-Unit Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. KG to Pounds")
    print("4. Pounds to KG")
    print("5. KM to Miles")
    print("6. Miles to KM")
    print("Q. Quit")

while True:
    show_menu()
    choice = input("\nChoose an option (1-6 or Q): ").upper()

    if choice == 'Q':
        print("Exiting... Goodbye!")
        break

    try:
        val = float(input("Enter value to convert: "))
        
        if choice == '1':
            print(f"Result: {val}°C = {(val * 9/5) + 32:.2f}°F")
        elif choice == '2':
            print(f"Result: {val}°F = {(val - 32) * 5/9:.2f}°C")
        elif choice == '3':
            print(f"Result: {val}kg = {val * 2.20462:.2f}lbs")
        elif choice == '4':
            print(f"Result: {val}lbs = {val / 2.20462:.2f}kg")
        elif choice == '5':
            print(f"Result: {val}km = {val * 0.621371:.2f} miles")
        elif choice == '6':
            print(f"Result: {val} miles = {val / 0.621371:.2f}km")
        else:
            print("Invalid Choice! Please pick 1-6.")
    except ValueError:
        print("Invalid Input! Please enter a number.")