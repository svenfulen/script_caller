# Example script that writes to a file given arguments

import sys

# filename is the file to write to
# text is the text to write to the file
filename = None
text = None

# Check that the right number of arguments were given
if len(sys.argv) < 4:
    print("Usage: write_file.py --filename [filename] --text [text]")
    sys.exit(1)

# Get the arguments from the command line
for idx, arg in enumerate(sys.argv):
    if arg == "--text":
        text = sys.argv[idx + 1]
    elif arg == "--filename":
        filename = sys.argv[idx + 1]

# Provide output to the console
print("Writing file...")
print("filename: " + filename)
print("text: " + str(text))

# Write the file
f = open(("./callable_scripts/" + filename), "a")
f.write(text)
f.close()