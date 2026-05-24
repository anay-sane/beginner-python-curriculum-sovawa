age= int(input("How old are you? "))
if age>=18:
   print("You can vote!")
print("Vote check complete")

#if else= choose 1 of 2 paths
temp=int(input("What is thew weather?(in farhenight)" ))
if temp < 50:
   print("It's cold waer a jacket")
else:
   print("no jacket needed")
print("Weather check done")

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