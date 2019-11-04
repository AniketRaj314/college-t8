# list in mutable
def lists():
    list1 = [9, 3, 2, 0, -2]
    print(list1[4])
    list1.sort()
    print(list1)
    list1.append(3)
    print(list1)

    list2 = [9, 2, 3, "Hello", [2, 3, "Python is amazing"]]
    print(list2[4][1])

# tuple is immutable
def tuples():
    tuple1 = (1, 2, 3, 4, 1)
    try:
        tuple1[1] = 1
    except:
        print("Tuple is immutable")
    print(tuple1)

# Sets (No repetitions in list)
def sets():
    set1 = {1, 2, 3, 4}
    print(set1)
    set1.add(9)
    print(set1)
    set1.add(1)
    # Repetition is ignored
    print(set1)

# Dictionaries
def dicts():
    string = "hello i am aniket raj i am in mit"
    words = string.split(' ')
    ctr = {}
    for word in words:
        if word in ctr:
            ctr[word] += 1
        else:
            ctr[word] = 1

    print(ctr)

    details = {
        "name": "aniket raj",
        "prn": 1032170250,
        "attendance": 100.00
    }

dicts()