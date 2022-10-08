import sys

filename = None
text = None

if len(sys.argv) < 4:
    print("Usage: write_file.py --filename [filename] --text [text]")
    sys.exit(1)

filename = sys.argv[1]

for idx, arg in enumerate(sys.argv):
    if arg == "--text":
        text = sys.argv[idx + 1]
    elif arg == "--filename":
        filename = sys.argv[idx + 1]

print("filename: " + filename)
print("text: " + str(text))

f = open(("./callable_scripts/" + filename), "a")
f.write(text)
f.close()