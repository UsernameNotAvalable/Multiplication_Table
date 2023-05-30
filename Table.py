def Checker():
   user_input = input(": ")
   while user_input.isdigit() == False:
       user_input = input("Please put a number: ")
   return user_input

print("Welcome! Please use the multiplication table whenever needed! Enjoy.")
print("Give me a multiplicand")
Multiplicand = int(Checker())
print("You have given", Multiplicand)


print("Give me a multiplier")
Multiplier = int(Checker())
print("You have given", Multiplier)


print("Give me a range / times of multiplication")
Times = int(Checker())
print("You have given", Times)


print("Your multiplicand is: ", Multiplicand, "| ", "Your multiplier is: ", Multiplier, "| ", "Your times is: ", Times, "|")


Product = Multiplicand * Multiplier

for i in range (Multiplicand, Times+1):
   Math = i * Multiplier
   print(i, "x", Multiplier, "=", Math)
