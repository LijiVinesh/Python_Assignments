# def read_file(file_name):
#     try:
#         with open(file_name, 'r') as file:
#             content = file.read()
#             print(content)
#     except FileNotFoundError:
#         print("File not found.")
#
# read_file("C:\\Users\\vines\\PycharmProjects\\D42_Pythonproject\\New_python_File.txt")

# Copying File

# def copy_file(source_file, destination_file):
#     try:
#         with open(source_file, 'r') as src:
#             content = src.read()
#         with open(destination_file, 'w') as dest:
#             dest.write(content)
#         print("File copied successfully.")
#     except FileNotFoundError:
#         print("Source file not found.")
# copy_file('source.txt', 'Destination.txt')

# Count Words on File

# def count_words_in_file(file_name):
#     try:
#         with open(file_name, 'r') as file:
#             content = file.read()
#             words = content.split()
#             word_count = len(words)
#             print(f"Total words: {word_count}")
#     except FileNotFoundError:
#         print("File not found.")
# count_words_in_file('Destination.txt')

#Convet number to integer
# def convert_to_integer():
#     try:
#         user_input = input("Please enter a number: ")
#         number = int(user_input)
#         print(f"Converted number: {number}")
#     except ValueError:
#         print("Invalid input! Please enter a valid integer.")
# convert_to_integer()

# Check -ve number on list.
# def check_negative():
#     try:
#         user_input = input("Enter a list of integers separated by spaces: ")
#         integers = list(map(int, user_input.split()))
#
#         for num in integers:
#             if num < 0:
#                 raise ValueError("Negative integers are not allowed.")
#
#         print("All integers are non-negative.")
#
#     except ValueError as e:
#         print(e)
# check_negative()
# Average Calculating
# def calc_average():
#     try:
#         user_input = input("Enter a list of integers separated by spaces: ")
#         integers = list(map(int, user_input.split()))
#
#         if len(integers) == 0:
#             raise ValueError("The list cannot be empty.")
#
#         average = sum(integers) / len(integers)
#         print(f"Average: {average}")
#
#     except ValueError as e:
#         print(f"Error: {e}")
#
#     finally:
#         print("Program has finished running.")
#
# calc_average()
def write_file():
    try:
        file_name = input("Enter the filename: ")
        with open(file_name, 'w') as file:
            file.write("Welcome to the file writing program!")
        print("File written successfully. Welcome!")

    except Exception as e:
        print(f"An error occurred: {e}")

write_file()