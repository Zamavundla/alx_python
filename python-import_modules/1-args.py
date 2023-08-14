import sys

if __name__ == "__main__":

# Get the number of arguments
  num_args = len(sys.argv) - 1

# Print the number of arguments and the corresponding text
if num_args == 0:
    print("0 arguments.")
elif num_args == 1:
    print("1 argument:")
else:
    print(f"{num_args} arguments:")

# Print the list of arguments with their positions
for i, arg in enumerate(sys.argv[1:], 1):
    print(f"{i}: {arg}")
