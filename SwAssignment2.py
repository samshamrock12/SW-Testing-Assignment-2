def calculate_bmi(height, weight):

    # Calculate BMI
    bmi = ((weight * 0.45) / ((height * 0.025) * (height * 0.025)))

    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        category = "Normal weight"
    elif 25 <= bmi <= 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi, category

def main():
    print("Body Mass Index (BMI) Calculator")

    # Get user input
    height = int(input("Enter height in inches: "))
    weight = float(input("Enter weight in pounds: "))

    # Calculate BMI
    bmi, category = calculate_bmi(height, weight)

    # Display results
    print(f"\nBMI Value: {bmi:.2f}")
    print(f"BMI Category: {category}")

if __name__ == "__main__":
    main()
