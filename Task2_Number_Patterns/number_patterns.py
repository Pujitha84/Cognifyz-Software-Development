# Cognifyz Technologies - Software Development Internship
# Level 1 - Task 2: Generate and Print Simple Number Patterns


def number_pyramid(rows):
    print("\nNumber Pyramid:")
    
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def reverse_pyramid(rows):
    print("\nReverse Number Pyramid:")
    
    for i in range(rows, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def number_square(rows):
    print("\nNumber Square:")
    
    for i in range(1, rows + 1):
        for j in range(1, rows + 1):
            print(j, end=" ")
        print()


def main():
    print("=" * 40)
    print("       NUMBER PATTERN GENERATOR")
    print("=" * 40)

    print("\nChoose a pattern:")
    print("1. Number Pyramid")
    print("2. Reverse Number Pyramid")
    print("3. Number Square")

    choice = input("\nEnter your choice (1-3): ")

    if choice not in ["1", "2", "3"]:
        print("\nInvalid choice. Please select 1, 2, or 3.")
        return

    try:
        rows = int(input("Enter the number of rows: "))

        if rows <= 0:
            print("Please enter a positive number.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    if choice == "1":
        number_pyramid(rows)

    elif choice == "2":
        reverse_pyramid(rows)

    elif choice == "3":
        number_square(rows)

    print("\nPattern generated successfully!")


if __name__ == "__main__":
    main()