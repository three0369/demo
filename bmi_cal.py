Filename:
    bmi_cal.py
Problem Statement:
    Assuming your weight in kilogram and height in meters
    Calculate your BMI value and print it 7
    Take the height and weight of the user from input
Hint:
    How to calculate your BMI?
    Divide your weight in kilograms (kg) by your height in meters (m)
    Then divide the answer by your height again to your BMI 
    1 Feet = 0.3048 m
    2 Inch = 0.0254 m
"""
# User weight
weight =  float(input("Enter your weight in kilograms >"))
# User height
height = float(input("Enter your height in meters >"))
# BMI_value = (weight/height)/height
print ("BMI value is :" + str(round(BMI_value,2)))
"""
Severe Thinness < 16
Moderate Thinness 16 - 17
Mild Thinness 17 - 18.5
Normal 18.5 - 25
Overweight 25 - 30
Obese Class I 30 - 35
Obese Class II 35 - 40
Obese Class III > 40
"""