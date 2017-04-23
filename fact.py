def fact():
  print("This program illustrates a factorial function")
  x = eval(input("Enter a number: "))
  fact = 1
  for factor in range(x, 1, -1):
    fact = fact * factor

  print("The factorial of", x, "is", fact)

fact()