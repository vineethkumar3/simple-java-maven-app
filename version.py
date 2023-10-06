import os

# Define the name of the environment variable
major = "majorVersion"


# Check if the environment variable exists
if major in os.environ:
    # Get the current value of the environment variable
    current_value = os.environ[major]
    print(f"Environment variable '{major}' found with value: {current_value}")
    
    # Update the value of the environment variable
    new_value = "1"
    os.environ[major] = new_value
    print(f"Updated '{major}' to '{new_value}'")
else:
    # Set the initial value if it doesn't exist
    initial_value = "initial_value"
    os.environ[major] = initial_value
    print(f"Environment variable '{major}' not found, created it with initial value: {initial_value}")

# You can use the environment variable further in your script or pipeline
# For example, print its value:
print(f"{major} is now set to: {os.environ[major]}")
