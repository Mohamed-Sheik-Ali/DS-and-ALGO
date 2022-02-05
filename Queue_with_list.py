queue = []

def enqueue():
    element = int(input("Enter an element: "))
    queue.append(element)
    print(f"The queue is => {queue}")

def dequeue():

    if not queue:
        print("Oops! There\'s nothing to remove here")
    else:
        e = queue.pop(0)
        print(f"{e} is removed")
        print(f"current queue is => {queue}")

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

