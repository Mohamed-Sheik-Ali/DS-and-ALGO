from collections import deque

queue = deque()

def enqueue():

    element = int(input("Enter an element: "))
    queue.appendleft(element)
    print(f"Queue is: {queue}")

def dequeue():

    if not queue:
        print("Oops! Queue is empty")
    else:
        e = queue.pop()
        print(f"{e} is removed")
        print(f"{queue} is the current queue")

while True:

    print("What are you going to do? 1/2/3: 1) Enqueue.  2) Dequeue. 3) Exit.")
    print("")
    choice = int(input("Enter a choice 1/2/3: "))

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        break
    else:
        print("Enter the correct operation.")
