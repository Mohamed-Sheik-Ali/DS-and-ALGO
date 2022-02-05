from collections import deque

stack = deque()


def push():
    element = int(input("Enter an element: "))
    stack.appendleft(element)
    print(f"Stack is: {stack}")


def pop():
    if not stack:
        print("Stack is empty.")
    else:
        e = stack.popleft()
        print(f"{e} is popped from the stack")
        print(f"current stack {stack}")


while True:

    print("What are you going to do? 1/2/3: 1) PUSH.  2) POP. 3) QUIT.")
    print("")
    choice = int(input("Enter a choice 1/2/3: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        print(f"Final stack is: {stack}")
        break
    else:
        print("Oops! Operation doesn\'t exist.")

# WE CAN ALSO USE QUEUE MODULE
# FOR append() use put()
# FOR pop() use get()
