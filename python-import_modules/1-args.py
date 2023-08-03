import sys

# Get the number of arguments
num_args = len(sys.argv) - 1

# Print the number of arguments
if num_args == 0:
    print("Number of argument(s): 0.")
else:
    print(f"Number of argument(s): {num_args}.")
    print("Arguments:")

    # Print the list of arguments with their positions
    for i, arg in enumerate(sys.argv[1:], 1):
        print(f"{i}: {arg}")
