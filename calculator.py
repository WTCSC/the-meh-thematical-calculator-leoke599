# Simple calculator with a rude twist
# Intro message
print ("Bruh. Why do you even need a calculator for basic math? Just use your brain. I can help you out, but it's going to cost 10$ per operation.")

# Take number and operation input
x = float(input('Enter first number （￣へ￣）: '))
y = float(input("""Enter second number                              ＿＿
　　　　　🌼＞　　フ
　　　　　| 　_　 _ l
　 　　　／` ミ＿xノ
　　 　 /　　　 　 |
　　　 /　 ヽ　　 ﾉ
　 　 │　　|　|　|
　／￣|　　 |　|　|
　| (￣ヽ＿_ヽ_)__)
　＼二つ: """))
operation = input('What do you want? (¬_¬") (+, -, *, /) ')

# Define functions for operations
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

# Perform operation and display result with rude comments
if operation == '+':
    print (f"{x} + {y} = {add(x, y)} HOW DO YOU NOT KNOW ADDITION IT'S THE FIRST THING YOU LEARN!? IT'S 15$ NOW!")
elif operation == '-':
    print (f"{x} - {y} = {subtract(x, y)} Bruh, even a kid knows that. You were probably too busy with your Dubai chocolate gold Labubu, 67, 41, Adrian's friend group, and a barbershop haircut that costs a quarter to learn anything. Pay up 10.25$.")
elif operation == '*':
    print (f"{x} * {y} = {multiply(x, y)} You didn't memorize your times tables? Go to your cardboard box on the street. 10$ now.")
elif operation == '/':
    if x == 0 or y == 0:
        print ("You can't divide by zero, genius. Just because of that, you owe me 1000$ now and a bag of fries.")
    else:
        print (f"{x} / {y} = {divide(x, y)} Wow, you don't even know division. Get me some McNuggets and 10$.")
else:
    print ("Invalid operation. You owe me 50$ for wasting my time. You can't even follow simple instructions. Put the fries in the bag.")