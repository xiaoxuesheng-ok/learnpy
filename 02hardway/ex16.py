from sys import argv

script, filename = argv

print(f"We are going to erase {filename}")
print("if you do not want that ,hit CTRL-C(^C)")
print("if you do want that,hit return.")

input("?")

print("opening the file...")
target = open(filename,'w')

print("Truncating the file . goodbye!")
target.truncate()

print("Now i am going to ask you for three lines.")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print("i am going to write these to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("and finally,wo close it ")

target.close()
