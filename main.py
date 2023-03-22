#Hannah Heflin - SW testing HW 2
#BMI Calculator
import math


def get_input():
    height_feet = str(input("Feet: "))
    height_inches = str(input("Inches: "))
    weight = str(input("What is you weight (in pounds)? "))

    return height_feet, height_inches, weight

def check_input(height_feet, height_in, weight):
    try:
        height_feet = int(height_feet)
    except:
        return 0
    try:
        height_in = int(height_in)
    except:
        return 0
    try:
        weight = int(weight)
    except:
        return 0
    
    return height_feet, height_in, weight

def convert(height_feet, height_inches):
    height = (int(height_feet) * 12) + int(height_inches)
    return height

def calculate(height, weight):
    temp = (height * .025)
    bmi = (weight * .45)/(temp * temp)
    round_bmi = round(bmi, 1)
    return round_bmi

def compare(bmi):
    if bmi < 25:
        if bmi < 18.5:
            category = "underweight"
        else:
            category = "normal weight"
    elif bmi >= 25:
        if bmi < 30:
            category = "overweight"
        else:
            category = "obese"
    return category


def main():
    print("Body Mass Index Calculator")
    print("What is your height?")
    feet, inches, pounds = get_input()
    height_feet, height_inches, weight = check_input(feet, inches, pounds)
    
    height = convert(height_feet, height_inches)
    bmi = calculate(height, weight)
    category = compare(bmi)
    
    print(bmi)
    print("Category: " + category)
    
#main()