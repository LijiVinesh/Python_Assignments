
def custom_function(a, b=10, c=None):

    if c is None:
        print(a + b)
    else:
        print(a * b * c)

a = int(input("Enter the first value (a): "))  # Input for a
b_input = input("Enter the second value (b) [default is 10]: ")
b = int(b_input) if b_input else 10
c_input = input("Enter the third value (c) [default is None]: ")
c = int(c_input) if c_input else None
custom_function(a, b, c)


def strings_length(strings):
    result = []
    for string in strings:
        if len(string) >= 5:
            result.append(string)
    return result
strings = ["Elephant", "Fish", "Tiger", "Lion", "Giraffe"]
final_String =strings_length(strings)
print(final_String)

expression = "3 * 5 + 2"
result = eval(expression)
print("The result of the expression is:", result)

def prime_check(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13,14,15,16,17,18,19,20]
prime_numbers = list(filter(prime_check, numbers))
print("Prime numbers in the list:", prime_numbers)

strings = ["python", "programming", "language"]

uppercase_strings = list(map(str.upper, strings))
print("Uppercase:", uppercase_strings)
