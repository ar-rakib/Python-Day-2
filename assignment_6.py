# # 1st input: enter height in meters e.g: 1.65
# height = input()
# # 2nd input: enter weight in kilograms e.g: 72
# weight = input()
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# new_height = float(height)
# new_weight = float(weight)
# BMI = new_weight/(new_height*new_height)
# print(int(BMI))


#type-2

# 1st input: enter height in meters e.g: 1.65
print("Please enter your height")
height = input()
# 2nd input: enter weight in kilograms e.g: 72
print("Please enter your weight")
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
new_height = float(height)
new_weight = int(weight)
BMI = new_weight/new_height**2
bmi_as_int = int(BMI)
print( bmi_as_int)



