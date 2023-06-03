#Input check for the integer inputs for each multiplicand / multiplier and times.
def Checker():
   user_input = input(": ")
   while user_input.isdigit() == False:
       user_input = input("Please put a number: ")
   return user_input

#placed for double-click usage of code, keeps the terminal open for reading of multiplication table.
def Finished():
    task_done = input ("When you are finished reading, please press enter to end program.")


print("Welcome! Please use the multiplication table whenever needed! Enjoy.")
print("Give me a multiplicand")
#specified int check so there are no issues with string inputs in math logic.
Multiplicand = int(Checker())
print("You have given", Multiplicand)


print("Give me a multiplier")
Multiplier = int(Checker())
print("You have given", Multiplier)


print("Give me a range / times of multiplication")
Times = int(Checker())
print("You have given", Times)

#printing each choice integer for verification.
print("Your multiplicand is: ", Multiplicand, "| ", "Your multiplier is: ", Multiplier, "| ", "Your times is: ", Times, "|")


Product = Multiplicand * Multiplier
#in range times - Start and end ranges for the math logic.
for i in range (Multiplicand, Times+1):
   Math = i * Multiplier
   print(i, "x", Multiplier, "=", Math)

Finished()
