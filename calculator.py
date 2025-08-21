def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero NOT POSIBLE"
    return a / b

if __name__ == "__main__":
    print("Welcome to the calculator!")
    print("2+3=", add(2, 3))
    print("2-3=", subtract(2, 3))
    print("2*3=", multiply(2, 3))
    print("2/3=", divide(2, 3))
    print("2/0=", divide(2, 0))
    