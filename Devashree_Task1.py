def calculate_bmi(weight, height):
    bmi=weight/(height**2)
    return bmi
def get_category(bmi):
    if bmi<18.5:
        return"Underweight"
    elif bmi<24.9:
        return"Normal weight"
    elif bmi<29.9:
        return"Overweight"
    else:
        return"obese"
def main():
    print("=== BMI Calculator ===")
    try:
        weight=float(input("Enter your weight in kilogram:"))
        height=float(input("Enter your height in meters:"))
        if weight<=0 or height<=0:
            print("Weight and height must be positive values")
            return
        bmi=calculate_bmi(weight, height)
        category=get_category(bmi)
        print("\n==== RESULT ====")
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
if __name__ == "__main__":
    main()
