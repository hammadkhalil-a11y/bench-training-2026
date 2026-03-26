name = "Hammad"
age = '23'
drink_coffee = True
salary = 23500.25

name = "Hammad"
age = 23
drink_coffee = True
salary = 23500.25
retirement_age=60
week_days=7
coffe_per_day=3
coffee_price = 150

years_untill_retirement = retirement_age - 23

print(f"My name is {name}. I am {age} years old. I {'drink' if drink_coffee else 'do not drink'} coffee. My Salary is {salary}")

print("There are ",years_untill_retirement," years left in retirement")
print("The weekly budget of my coffee is ",coffe_per_day * week_days * coffee_price)