def Binary_Search(low, high, condition):

    while low <= high:
        mid = (low + high) // 2
        result = condition(mid)

        if result == "found":
            return mid
        elif result == "left":
            high = mid - 1
        else:
            low = mid + 1
    return -1


def locate_card(cards, query):

    def condition(mid):
        if cards[mid] == query:

            if mid > 0 and cards[mid - 1] == query:
                return "left"
            else:
                return "found"

        elif cards[mid] < query:
            return "left"
        else:
            return "right"
    return Binary_Search(0, len(cards) - 1, condition)


tests = [{
    "inputs": {
        "cards": [10, 9, 8, 7, 6, 4, 2, 1, 0],
        "query": 6
    },
    "output": 4
}, {
    "inputs": {
        "cards": [19, 14, 10, 10, 10, 7, 6, 5, 3, 1],
        "query": 10
    },
    "output": 2
}, {
    "inputs": {
        "cards": list(range(100001, 0, -1)),
        "query": 2
    },
    "output": 99999
}]

for test in tests:

    Test_Cases = locate_card(**test["inputs"]) == test["output"]

    if Test_Cases == True:
        print(f"Test {tests.index(test)} Passed")
        print("")
    else:
        print(f"Test {tests.index(test)} Failed")

# <-- BIG-O Notation => O(log N) -->
