##Use if/else statements
print("I can tell you the absolute value of any number!")
n = int(input("Number? "))
if n < 0:
    print("The absolute value of", n, "is", -n)
else:
    print("The absolute value of", n, "is", n)
print()
print()

##Use elif statements
print("I will tell you whether numbers between 0 and 10 are greater than or equal to 9 or less than or equal to 6.")

a = 0
while a < 10:
    a = a + 1
    if a <= 6:
        print(a, "<=", 6)
    elif a >= 9:
        print(a, ">=", 9)
    else:
        print("Fails both tests")
print()
print()

##Use an operator

print("I will now tell you some inequalities.")
print("Does 5 = 6?")
print(5 == 6)
x = 5
y = 7
print("Does x=5 equal y=7?")
print(x == y)
print()
print()

##Make a higher/lower guessing game

number = 8
guess = 0
count = 0

print("Now guess a number! Then I'll tell you if it's higher or lower than what I'm thinking.")
while guess != number:
    guess = int(input("Guess? "))
    count = count + 1

    if guess == number:
        print("Yay! You got it right!")
        if count > 3:
            print("That must have been hard.")
        else:
            print("Good job!")
    elif guess < number:
        print("It's a bit bigger...")
        count = count + 1
    elif guess > number:
        print("It's a bit smaller...")
        count = count + 1

print()
print()

##Figure out if number is even or odd

print("Now I'll let you know if any number is even or odd.")
number = float(input("Tell me a number: "))

if number % 2 == 0:
    print(int(number), "is even.")
elif number % 2 == 1:
    print(int(number), "is odd.")
else:
    print(number, "is very strange.")
print()
print()

##Sum a running total and find the average
print("Now I'll find an average across however many data points.")
print("Enter 0 as last data point to calculate average.")
number = 1
count = 0
sum = 0

while number != 0:
    number = float(input("Data point: "))
    if number != 0:
        count = count + 1
        sum = sum + number
        print("Current sum:",sum)
    if number == 0:
        print("The average is:", sum / count)
print()
print()


##State a number of data points you'll enter then average them
print("Now, I'll calculate the average over a certain number of data points.")

number = 0
count = int(input("How many numbers would you like to average: "))
sum = 0
current_count = 0

while current_count < count:
    current_count = current_count + 1
    print("Number", current_count)
    number = float(input("Data point: "))
    sum = sum + number

print("Average:", sum / count)
print()
print()
    
##Enter a program about names
print("Now, enter you're name.")
my_name = str("Brandon Sherrard")
john_name = str("John Cleese")
michael_name = str("Michael Palin")

user_name = str(input("What is your name? "))

if user_name == my_name:
    print("That is a nice name.")
elif user_name == john_name:
    print("Whoa, coincidence.")
elif user_name == michael_name:
    print("Whoa, coincidence.")
else:
    print("You have a nice name.")
print()
print()

##Ask for two numbers, add them, and decide if those numbers are 'big'
print("I can add two numbers together to let you know if it's big or small!")
number1 = float(input("Number 1? "))
number2 = float(input("Number 2? "))
sum = number1 + number2
print("Sum =",sum)

if sum > 100:
    print("That is a big number.")
else:
    print("Oh wow.")
print()
print()
