import random
dictionary = {}
nums = []
def create_dictionary(x):
    ctr = 97
    
    for _ in range(26):
        random.seed(x)
        while True:
            num = random.randrange(97, 123)
            if num not in nums:
                nums.append(num)
                dictionary[chr(ctr)] = chr(num)
                ctr += 1
                break


if __name__ == "__main__":
    key = input("Enter the key value: ")
    create_dictionary(key)
    inp = input("Enter the text to be encrypted:")
    op = ""
    for c in inp:
        op += dictionary[c]

    print(op)