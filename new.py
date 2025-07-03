def calculate_rectangle_area(length, width):
  """
  Calculates the area of a rectangle.

  Args:
    length: The length of the rectangle.
    width: The width of the rectangle.

  Returns:
    The area of the rectangle.
  """
  area = length * width
  return area

# Get input from the user
user_length = float(input("Enter the length of the rectangle: "))
user_width = float(input("Enter the width of the rectangle: "))

# Call the function and store the result
rectangle_area = calculate_rectangle_area(user_length, user_width)

# Print the result
print(f"The area of the rectangle is: {rectangle_area}")