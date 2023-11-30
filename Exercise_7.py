age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

age_as_int = int(age)

age_in_week = age_as_int*52

total_age = 90*52

remain = total_age - age_in_week

print(f"You have {remain} weeks left.")


#solution 2
print("Write your present age:")
age = input()
years = 90-int(age)
weeks = years*52
print(f"You have {weeks} weeks left.")







