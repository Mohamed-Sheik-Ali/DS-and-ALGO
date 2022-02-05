stack = []

def push():
    element = input("Enter the element: ")
    stack.append(element)
    print(stack)

def pop():
    if not stack:
        print("Oops! Stack is empty")
    else:
        e = stack.pop()
        print(f"{e} is popped from the stack")
        print(f"Current stack is => {stack}")

while True:

    print("Select an operation: 1) PUSH.  2) POP. 3) QUIT.")
    choice = int(input("Enter a choice 1/2/3: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print("Oops! Operation doesn\'t exist.")