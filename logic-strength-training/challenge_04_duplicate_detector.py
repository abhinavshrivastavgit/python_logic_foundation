# challenge_04_duplicate_detector.py
list_A = ["Alice","Bob","Charlie"]
list_B = ["Bob", "David", "Alice "]

for name in list_A:
    if name in list_B:
        print(name)