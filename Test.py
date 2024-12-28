# a = []
# val = int(input("How many Books you want to add : "))
# for i in range(val):
#     book = input("Enter Name of book : ")
#     a.append(book)
# selection = int(input("1 for yes and 0 for no"))
# if (selection == 1):
#     for val in range(val):
#         print(a[val])
# if (selection == 0):
#     quit()
# print(len(a))

# b = []
# while True:
#     add = input("Enter Name of Books : ")
#     b.append(add)

import csv

def remove_line_from_csv(filename, line_number):
  """
  Removes a specific line from a CSV file.

  Args:
    filename: The name of the CSV file.
    line_number: The 1-based index of the line to remove (e.g., 1 for the first line).

  Raises:
    ValueError: If the line_number is invalid (e.g., negative or greater than the number of lines).
  """

  if line_number <= 0:
    raise ValueError("Line number must be a positive integer.")

  with open(filename, 'r') as infile:
    reader = csv.reader(infile)
    data = list(reader)

  if line_number > len(data):
    raise ValueError("Line number is out of range.")

  del data[line_number - 1]  # Adjust for 0-based indexing

  with open(filename, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(data)

# Example usage:
filename = 'storedData.csv'
line_to_remove = 2  # Remove the second line

try:
  remove_line_from_csv(filename, line_to_remove)
  print(f"Line {line_to_remove} removed from {filename}")
except ValueError as e:
  print(f"Error: {e}")