
##This program is to practice using the user_input feature in python

print("Halt!")
user_input = input("Who goes there? ")
print("You may pass,",user_input,".")

addend = int(input("What would you like me to cube? "))
print(addend**3)
print()

##For practice with user input
random_number = float(input("Type in a number: "))
integer = int(input("Type in an integer, loser: "))
text = input("Type in a string: ")
print("number =", random_number)
print("number is a", type(random_number))
print("number * 2 =", random_number*2)
print("integer =", integer)
print("integer is a", type(integer))
print("integer * 200 =", integer*200)
print("text =", text)
print("text is a", type(text))
print("text * 2 =", text*2)
print()

##For calculating time
print("Now, input a rate and a distance")
rate = float(input("Rate (m/s): "))
distance = float(input("Distance (m): "))
time=distance/rate
print("Time (s): ",time)
print()

##For calculating area
print("Now, let's calculate area. Enter length and width.")
length = float(input("Length: "))
width = float(input("Width: "))
area = length*width
print("Area: ",area)
perimeter = 2*length+2*width
print("Perimeter: ",perimeter)
print()

##For converting between temperatures
print("Now, let's convert celcius to fahrenheit:")
tempC = float(input("Temp. (C): "))
tempF = 1.8*tempC+32
print("Temp. (F):",tempF)
print()

##Simple exercise: Concatenating and Adding user inputs
print("Now, let's smush words together and do some math.")
word1 = str(input("First Word: "))
word2 = str(input("Second Word: "))
print(word1)
print(word2)
word_smush = word1+word2
print(word_smush)
print()
print("Math time!")
number1 = float(input("First Number: "))
number2 = float(input("Second Number: "))
combined = number1*number2
print(combined)
