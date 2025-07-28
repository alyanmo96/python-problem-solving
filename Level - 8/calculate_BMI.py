#    Calculates BMI (Body Mass Index) and returns a classification.

def bmi(weight,height):
    result_of_bmi= weight/(pow(height,2))
    if result_of_bmi <=18.5:
        return "Underweight"
    if result_of_bmi > 18.5 and result_of_bmi <= 25:
        return "Normal"
    if result_of_bmi > 25 and result_of_bmi <= 30.0:
        return "Overweight"
    else:
        return "Obsee"


print(bmi(86, 1.80))  # Output: 'Overweight'
