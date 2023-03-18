from sys import getsizeof 

def lists():
    # Bonus Tip 💡:  Iterating over multiple lists
    A = ["a", "b", "c", "d"]
    B = ["e", "f", "g", "h"]

    # Pythonic version 🐍: Use zip to get the values ✅
    for va, vb in zip(A, B):
        print(va, vb)

    # Pythonic version 🐍: Use a combination of zip and enumerate to get the index and the values ✅
    for i, (va, vb) in enumerate(zip(A, B)):
        print(i, va, vb)
    raise ValueError

lists()