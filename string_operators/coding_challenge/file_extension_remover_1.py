# File Extension Remover

# File extensions are the short sequences of characters (usually three) that follow a period (.) at the end of filenames (like “readme.txt”).  Sometimes, you might want to work with just the base names, without their extensions (like “readme”).
# Imagine you're tasked with handling a list of filenames, where some have extensions and others don’t.
# Write a function named remove_extension that takes a single parameter: a string filename, and return the file's base name, regardless of whether it originally had an extension.

def remove_extension(filename):
    dot_index = filename.rfind('.') # finds the dot in the extension
    if dot_index == -1: # if the dot is at the end of the extension, print the filename
        return filename
    else: # print everything before the dot
        return filename[:dot_index]


filename = input("Enter a filename: ")
clean_filename = remove_extension(filename)
print(clean_filename)

