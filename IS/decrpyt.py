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
    create_dictionary(input("Enter the key value: "))
    inp = input("Enter string to be decrypted:")
    op = ""
    for c in inp:
        for key, val in dictionary.items():
            if c == val:
                op += key

    print(op)