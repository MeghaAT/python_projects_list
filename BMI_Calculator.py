#round off to closest whole number 

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI=round(weight/height**2)
if BMI<18.5:
 print(f"your BMI is {BMI}, you are underweight")
elif BMI<25:
  print(f"your BMI is {BMI}, you are normal weight")
elif BMI<30:
  print(f"your BMI is {BMI}, you are over weight")
else:
  print(f"your BMI is {BMI} ,you are clinically  obese")