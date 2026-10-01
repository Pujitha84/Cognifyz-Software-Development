# Cognifyz Technologies - Software Development Internship
# Level 2 - Task 4: Temperature Converter


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    print("=" * 45)
    print("       TEMPERATURE CONVERTER")
    print("=" * 45)

    print("\nChoose conversion direction:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("\nEnter your choice (1 or 2): ")

    if choice not in ["1", "2"]:
        print("\nInvalid choice. Please select 1 or 2.")
        return

    try:
        temperature = float(input("Enter temperature: "))
    except ValueError:
        print("\nPlease enter a valid temperature.")
        return

    if choice == "1":
        result = celsius_to_fahrenheit(temperature)
        print(f"\n{temperature:.2f}°C = {result:.2f}°F")

    elif choice == "2":
        result = fahrenheit_to_celsius(temperature)
        print(f"\n{temperature:.2f}°F = {result:.2f}°C")

    print("\nConversion completed successfully!")


if __name__ == "__main__":
    main()