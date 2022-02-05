stack = []

def push():
    if len(stack) == n:
        print("Looks like the stack is filled!")
        print("")
    else:
        element = input("Enter the element: ")
        print("")
        stack.append(element)
        print(stack)
        print("")

def pop():
    if not stack:
        print("Oops! Stack is empty")
    else:
        e = stack.pop()
        print(f"{e} is popped from the stack")
        print("")
        print(f"Current stack is => {stack}")
        print("")

n = int(input("Set the limit here: "))

while True:
    
    print("What are you going to do? 1/2/3: 1) PUSH.  2) POP. 3) QUIT.")
    print("")
    choice = int(input("Enter a choice 1/2/3: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print("Oops! Operation doesn\'t exist.")
