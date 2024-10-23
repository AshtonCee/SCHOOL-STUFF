# @author Ashton Coplin

from random import randint
def main():
    MAX_LIST_SIZE = 20
    LOW_VALUE = 1
    HIGH_VALUE = 50
    
    user_num = 0
    
    while user_num < LOW_VALUE or user_num > MAX_LIST_SIZE:
        user_num = int(input(f"How many values (up to {MAX_LIST_SIZE}) to generate? "))
    # Loop until a valid size between 1 and MAX_LIST_SIZE (inclusive)
    # is entered. The value stored in MAX_LIST_SIZE is flexibly placed into
    # the prompt: If the value stored in MAX_LIST_SIZE is changed above,
    # the prompt and loop condition automatically adjust for it. No code
    # needs changing
        
    
    data = []
    for i in range(user_num):
        data.append(randint(LOW_VALUE, HIGH_VALUE))
    # Create an empty list named data and append random integers 
    # in the range LOW_VALUE through HIGH_VALUE. The number of random numbers
    # appended is based upon the size the user previously entered.
    # Keep the code flexible -- use LOW_VALUE and HIGH_VALUE in your code,
    # not the literal values stored inside LOW_VALUE and HIGH_VALUE
    
    
    data.sort()
    # Put the data list in increasing sorted order

    
    for i in data:
        print(i, end=" ")
    print()
    # Loop to display each data value on the same line with space delimiters    
 
    
    print("\nDisplay all values between what inclusive range?")
    lower_bound = int(input("Lower bound: "))
    upper_bound = int(input("Upper bound: "))
    # Prompt for and retrieve the lower and upper bound as integers

    
    for i in range(lower_bound, upper_bound + 1):
        if i in data:
            print(i, end=" ")
    print()
    # Loop to display the values lying in the given range by the user
    # This will be a loop with an if statement inside of it.

    
    print("\nHistogram")
    for i in data:
        print("*" * ((i + 1)//2))
    # Display a histogram for each value in data where a *
    # is displayed for how many times 2 evenly divides into
    # (value + 1). For example if the data value is  1,
    # 1 + 1 is 2, so one * is shown, If the data value is 2, 2 + 1 is 3,
    # so one * is shown, If the data value is 3, 3 + 1 is 4, so two *'s
    # are shown, etc.
    # The data values in the histogram are accessed in sorted order.   
 

main()