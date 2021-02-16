import sys
import os
clear = lambda: os.system('clear')

def code():
  print("\nSelect Operation")
  print("1.Add")
  print("2.Subtract")
  print("3.Devide")
  print("4.Multiply")

  Operator = int(input())

  if Operator == 1:
    num1 = float(input("Number 1: "))
    num2 = float(input("Number 2: "))
    answer = num1 + num2
    print(f"Answer: {answer}")

    rerun = input("\nDo you want to run this again? [y/n]\n")

    if rerun == "y":
      clear()
      code()
    else:
      sys.exit()

  if Operator == 2:
    num1 = float(input("Number 1: "))
    num2 = float(input("Number 2: "))
    answer = num1 - num2
    print(f"Answer: {answer}")

    rerun = input("\nDo you want to run this again? [y/n]\n")

    if rerun == "y":
      clear()
      code()
    else:
      sys.exit()

  if Operator == 3:
    num1 = float(input("Number 1: "))
    num2 = float(input("Number 2: "))
    answer = num1 / num2
    print(f"Answer: {answer}")

    rerun = input("\nDo you want to run this again? [y/n]\n")

    if rerun == "y":
      clear()
      code()
    else:
      sys.exit()

  if Operator == 4:
    num1 = float(input("Number 1: "))
    num2 = float(input("Number 2: "))
    answer = num1 * num2
    print(f"Answer: {answer}")

    rerun = input("\nDo you want to run this again? [y/n]\n")

    if rerun == "y":
      clear()
      code()
    else:
      sys.exit()

code()

