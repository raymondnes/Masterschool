import os # import os module

def remove_extension(filename):
    return os.path.splitext(filename)[0]

filename = input("Enter a filename: ")
clean_filename = remove_extension(filename)
print(clean_filename)

# By importing the os module, you can use its functions 
# and classes in your Python code. For example, 
# you can use os.path.splitext() to split a filename into its base name and extension, 
# or os.environ to access environment variables.
