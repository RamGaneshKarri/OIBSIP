def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi <= 18.5:
        return "underweight"
    elif bmi <= 24.9:
        return "healthy"
    elif bmi <= 29.9:
        return "overweight"
    else:
        return "obese"

def main():
    try:
        height = float(input("Enter your height in cm: "))
        weight = float(input("Enter your weight in kg: "))

        if height <= 0 or weight <= 0:
            print("Height and weight must be positive numbers.")
            return

        bmi = calculate_bmi(height, weight)
        category = classify_bmi(bmi)

        print(f"Your Body Mass Index is: {bmi:.2f}")
        print(f"You are classified as: {category.capitalize()}.")

    except ValueError:
        print("Please enter valid numeric values for height and weight.")

if __name__ == "__main__":
    main()
