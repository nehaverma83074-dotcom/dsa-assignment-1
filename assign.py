# Algorithmic Efficiency & Recursion Toolkit (AERT)

# -----------------------------
# Part A: Stack ADT
# -----------------------------

class StackADT:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# -----------------------------
# Part B: Factorial (Recursive)
# -----------------------------

def factorial(n):
    if n < 0:
        return "Invalid Input"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


# -----------------------------
# Fibonacci
# -----------------------------

naive_calls = 0
memo_calls = 0

def fib_naive(n):
    global naive_calls
    naive_calls += 1

    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)


memo = {}

def fib_memo(n):
    global memo_calls
    memo_calls += 1

    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fib_memo(n-1) + fib_memo(n-2)

    return memo[n]


# -----------------------------
# Part C: Tower of Hanoi
# -----------------------------

def hanoi(n, source, auxiliary, destination):
    if n == 1:
        move = f"Move disk 1 from {source} to {destination}"
        print(move)
        return

    hanoi(n-1, source, destination, auxiliary)

    move = f"Move disk {n} from {source} to {destination}"
    print(move)

    hanoi(n-1, auxiliary, source, destination)


# -----------------------------
# Part D: Recursive Binary Search
# -----------------------------

def binary_search(arr, key, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid

    elif key < arr[mid]:
        return binary_search(arr, key, low, mid-1)

    else:
        return binary_search(arr, key, mid+1, high)


# -----------------------------
# MAIN FUNCTION (Test Cases)
# -----------------------------

def main():

    print("----- Factorial Tests -----")
    for n in [0,1,5,10]:
        print(f"factorial({n}) =", factorial(n))


    print("\n----- Fibonacci Tests -----")
    for n in [5,10,20,30]:

        global naive_calls
        naive_calls = 0
        naive_result = fib_naive(n)

        global memo_calls
        memo_calls = 0
        memo.clear()
        memo_result = fib_memo(n)

        print(f"\nFibonacci({n})")
        print("Naive Result:", naive_result)
        print("Naive Calls:", naive_calls)

        print("Memo Result:", memo_result)
        print("Memo Calls:", memo_calls)


    print("\n----- Tower of Hanoi (N=3) -----")
    hanoi(3, 'A', 'B', 'C')


    print("\n----- Binary Search Tests -----")

    arr = [1,3,5,7,9,11,13]

    tests = [7,1,13,2]

    for key in tests:
        result = binary_search(arr, key, 0, len(arr)-1)
        print(f"Search {key} -> index:", result)

    arr2 = []

    result = binary_search(arr2, 5, 0, len(arr2)-1)
    print("Search in empty array:", result)


if __name__ == "__main__":
    main()