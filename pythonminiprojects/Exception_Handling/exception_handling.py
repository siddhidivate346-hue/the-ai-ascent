"""try:
    num=int(input("enter a number"))
    result = 100/num
    print("result", result)

except ValueError:
    print("please enter a valid number")

except ZeroDivisionError:
    print("cannot dicide by zero")
finally:
    print("program finished")"""

try:
    num = int(input("Enter a number: "))

    if num < 0:
        raise ValueError("Negative numbers not allowed")

    result = 200 / num
    print("Result:", result)

except ValueError as e:
    print("Error:", e)

except ZeroDivisionError:
    print("Cannot divide by 0")

finally:
    print("Program finished")




