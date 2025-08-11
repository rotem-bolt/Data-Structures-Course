# This is a sample Python script for debugging practice.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    return f"Greeting sent to {name}"

def calculate_sum(numbers):
    """Calculate sum of numbers - good for debugging loops"""
    total = 0
    for i, num in enumerate(numbers):
        total += num
        print(f"Adding {num}, running total: {total}")  # Good breakpoint location
    return total

def debug_example():
    """Function to demonstrate debugging features"""
    x = 10
    y = 20
    result = x + y
    print(f"x = {x}, y = {y}, result = {result}")
    
    # List to iterate over
    numbers = [1, 2, 3, 4, 5]
    sum_result = calculate_sum(numbers)
    print(f"Sum of {numbers} is {sum_result}")
    
    return result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Dvir`s angles')
    debug_example()
