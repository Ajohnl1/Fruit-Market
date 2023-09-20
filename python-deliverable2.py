import math
name = input("Welcome to the Fruit Market! What is your name?")

total = 0
subtotal = 0
apple = 0
grape = 0
orange = 0
basket = []

options = {
    1: " Grapes $1",
    2: " Apples $2",
    3: " Oranges $3",
}

def print_options():
    print("Welcome, " + name + ". Please select the fruit you would like to purchase.")
    for key in options.keys():
        print(key, options[key])
while True:
    print_options()
    fruit = input()
    print("You bought 1" + options[int(fruit)][:-2] + "at" + options[int(fruit)][-3:])
    basket.append(int(fruit))
    answer = input("Would you like to by another piece of fruit? y/n ")
    if answer != "y":
        break

for fruit in basket:
    if fruit == 1:
        grape += 1
    if fruit == 2:
        apple += 1
    if fruit == 3:
        orange += 1
    subtotal += fruit

print("Receipt for " + name + ":")
print(str(grape) + " Grapes are $1 per")
print(str(apple) + " Apples are $2 per")
print(str(orange) + " Oranges are $3 per")

total = subtotal * 1.05
tax = .05 * subtotal

print("subtotal: $", subtotal)
print("5% Tax: $", tax)
print("total: $", total)