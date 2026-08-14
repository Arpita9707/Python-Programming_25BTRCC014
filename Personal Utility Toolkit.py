import math

while True:
    print("\n========== PERSONAL UTILITY TOOL ==========")
    print("1. Celsius to Fahrenheit Conversion")
    print("2. Fahrenheit to Celsius Conversion")
    print("3. Calculate Area of Circle")
    print("4. Calculate Area of Rectangle")
    print("5. Calculate Simple Interest")
    print("6. Calculate Body Mass Index (BMI)")
    print("7. Exit")

    choice = int(input("\nEnter your choice (1-7): "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")

    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"Temperature in Celsius: {celsius:.2f}°C")

    elif choice == 3:
        radius = float(input("Enter the radius of the circle: "))
        area = math.pi * radius ** 2
        print(f"Area of Circle: {area:.2f}")

    elif choice == 4:
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        area = length * width
        print(f"Area of Rectangle: {area:.2f}")

    elif choice == 5:
        principal = float(input("Enter Principal Amount: "))
        rate = float(input("Enter Rate of Interest (%): "))
        time = float(input("Enter Time (years): "))
        simple_interest = (principal * rate * time) / 100
        print(f"Simple Interest: {simple_interest:.2f}")

    elif choice == 6:
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (m): "))
        bmi = weight / (height ** 2)
        print(f"Your BMI is: {bmi:.2f}")

        if bmi < 18.5:
            print("Category: Underweight")
        elif bmi < 25:
            print("Category: Normal weight")
        elif bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obese")

    elif choice == 7:
        print("Thank you for using the Personal Utility Tool!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 7.")