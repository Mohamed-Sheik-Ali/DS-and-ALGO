import time

start = time.time()


def locate_card(cards, query):

    print(f"cards: {cards}, Length of card: {len(cards)}")
    print(f"query: {query}")

    position = 0

    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1


test = {
    "inputs": {
        "cards": [10, 9, 8, 7, 6, 4, 2, 1, 0],
        "query": 4
    },
    "output": 5
}

time.sleep(1)

end = time.time()

print(locate_card(**test["inputs"]))
print(f"Execution Time is {end - start}")

# <-- BIG-O Notation => O(N) -->
