the_count = [1,2,3,4,5]
fruits = ["apple","oranges","prars","apricots"]
change = [1,'pennies',2,'dimes',3,'quarters']
# this first kind of for0loop goes thrugh a list

for num in the_count :
    print(f"this is count {num}")

# same as above

for fruit in fruits:
    print(f"this is {fruit}")


#also we can go throgh mixed lists too

element = []

for i in range(0,6):
    element.append(i)

for i in element :
    print(i)

element = range(0,10)

for i  in element:
    print(i)
