from mathz.add import add, multiply, divide
from mathz.train import train
from mathz.subtract import subtract

if __name__ == "__main__":
    print(f"Addition is: {add(1, 2)}")
    print(f"Multiplication is: {multiply(2, 5)}")
    print(f"Division is: {divide(20, 2)}")

    print('Training model ...')
    train()

    # call subtract here
    print(f"Subtracting two numbers: {subtract(99, 10)}")

