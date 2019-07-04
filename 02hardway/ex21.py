def add(a,b):
    print(f"adding {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"subtract {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"multiply {a} * {b}")
    return a * b

def devide(a,b):
    print(f"devide {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = devide(100,2)

print(f"Age:{age},height:{height},weight:{weight},iq:{iq}")

# a puzzle foe the extra credit,type it in anyway

print("here is puzzle")

what = add(age,subtract(height,multiply(weight,devide(iq,2))))

print("that becomes:",what,"can you do it by hand ? ")
