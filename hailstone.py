"""
Asks for user input and calculates the cascading hailstone sequence re: Hofstadter
version 0.001
2021 @cheynolds
"""

steps = 0

def main():

    numberCalc(steps)

#asks for user input and calculates the cascading hallstone sequence
def numberCalc(steps):
    num1 = int(input("Enter a number: "))
    int(num1)
    while num1 > 1:
        if num1 % 2 == 0:
            num2 = num1 / 2
            print(str(int(num1)) + " is even, so I take half: " + str(int(num2)))
            num1 = num2
            steps += 1

        else:
            num2 = (num1*3) + 1
            print(str(int(num1)) + " is odd, so I make 3n + 1: " + str(int(num2)))
            num1 = num2
            steps += 1

    print("The process took " + str(steps) + " steps to reach 1")


if __name__ == "__main__":
    main()
