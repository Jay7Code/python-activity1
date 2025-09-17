# 1. Storing User Information
# Variables are defined to hold user details using different data types.
name = "Arjay"                 # String
age = 21                       # Integer
city = "Malasiqui"             # String
student_status = True          # Boolean
user_height = 1.75             # Float

# Displaying the initial user information
print("==== USER INFORMATION ====")
print("Name: " + name)
print("Age: " + str(age))
print("City: " + city)
print("Student Status: " + str(student_status))


# 2. Performing Mathematical Operations
print("\n==== SIMPLE CALCULATION ====")

# Get two numbers from the user and convert them to float data type
input1 = float(input("Enter first number: "))
input2 = float(input("Enter second number: "))

# Perform various arithmetic operations
sum_result = input1 + input2  # Renamed from 'sum' to avoid conflict with built-in function
difference = input1 - input2
product = input1 * input2
quotient = input1 / input2
modulus = input1 % input2
exponentiation = input1 ** input2
floor_division = input1 // input2

# Display the results of the calculations using f-strings for cleaner output
print(f"\nResults for {input1} and {input2}:")
print(f"Sum ({input1} + {input2}) = {sum_result}")
print(f"Difference ({input1} - {input2}) = {difference}")
print(f"Product ({input1} * {input2}) = {product}")
print(f"Quotient ({input1} / {input2}) = {quotient}")
print(f"Modulus ({input1} % {input2}) = {modulus}")
print(f"Exponentiation ({input1} ** {input2}) = {exponentiation}")
print(f"Floor Division ({input1} // {input2}) = {floor_division}")


# 3. Demonstrating String Manipulation
print("\n==== STRING OPERATIONS ===")

# Concatenate strings to create a greeting
greeting = "Hello, " + name + " from " + city + "!"
print("Concatenated greeting: " + greeting)
print("-------------------------")

# Show different string methods
print("Name in uppercase:", name.upper())
print("Name in lowercase:", name.lower())
print("Name length:", len(name))

# Use an f-string to format a complex sentence with multiple variables
formatted_info = f"Formatted user info: {name} is {age} years old, {user_height}m tall, and lives in {city}."
print(formatted_info)


# 4. Verifying Data Types
print("\n=== DATA TYPE INFORMATION ===")
print(f"Type of 'name' ({name}):", type(name))
print(f"Type of 'age' ({age}):", type(age))
print(f"Type of 'user_height' ({user_height}):", type(user_height))
print(f"Type of 'student_status' ({student_status}):", type(student_status))
print(f"Type of 'sum_result' ({sum_result}):", type(sum_result))


# 5. Demonstrating Comparison Operations
print("\n=== COMPARISON OPERATIONS ===")
x = input1
y = input2
print(f"Is {x} equal to {y}? ", x == y)
print(f"Is {x} greater than {y}? ", x > y)
print(f"Is {x} less than or equal to {y}? ", x <= y)


print("\n=== ACTIVITY COMPLETE ===")