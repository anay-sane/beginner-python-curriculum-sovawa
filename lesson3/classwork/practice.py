# Problem 1
# Ask the user to enter their height in centimeters.
# Print "Tall" if the height is greater than 170, otherwise print "Short".
height= int(input("enter your height"))


# Problem 2
# Ask the user for their age.
# If they are 18 or older, print "Adult", else print "Minor".



# Problem 3
# Ask the user to enter a number.
# Print "Fizz" if it is divisible by 3, "Buzz" if divisible by 5,
# print "FizzBuzz" if divisible by both 3 and 5,
# otherwise print the number itself.
num= int(input("Enter a number"))
if num % 3 == 0:
   print("Fizz")
elif num % 5 ==0:
   print("Buzz")
elif num % 5 ==0 

# Problem 4
# Use the random module to generate a random number between 1 and 6 (inclusive).
# If the number is greater than 4, print "High roll!",
# otherwise print "Low roll!".
import random
rum= random.randint(1, 6)
if rum >4:
   print("High Roll")
else:
   print ("Low roll")

# Problem 5
# Ask the user for their test score (0-100).
# Print the grade based on score:
#   90 and above: "A"
#   80 to 89: "B"
#   70 to 79: "C"
#   60 to 69: "D"
#   below 60: "F"
# Use nested if or elif statements.
grade= int(input("Enter your score out of 100: "))
if grade>=90:
   print("You got an A")
elif grade >=80:
   print("You got a B")
elif grade >= 70:
   print("You got a C")
elif grade >= 60:
   print("You got a D")
else:
   print("You got an F. You failed :()")