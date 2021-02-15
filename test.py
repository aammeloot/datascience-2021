import typing

# Example of function without type hints
def multiply(a,b):
    return a*b

# Example of function with type hints
def add(a: int, b: int) -> int:
    return a+b

# Python selection
def ageCheck(age: int) -> str:
    if age >= 18:
        return "You can have wine."
    else:
        return "You need to stick to juice"

# Python loops
# While loop
def demoWhile() -> None:
    userInput = str("")
    while userInput != "cheese":
        userInput = input("Type 'cheese' to end the loop")

    # When finished thank user
    print("Thanks for lifting the curse.")

# For loop
def demoFor() -> None:
    for index in range(10, 0, -1):
        print("index =", index)

# Main function
def main() -> None:
    demoFor()

# Definition of main function
if __name__ == "__main__":
    main()
