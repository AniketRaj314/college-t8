if __name__ == "__main__":
    # table = {}
    # n = int(input("Enter the number of items:"))
    # for i in range(n):
    #     table[int(input(f"Enter Weight for entry number {i+1}: "))] = int(input(f"Enter corresponding profit for entry number {i+1}: "))
    table = {10: 23, 20: 34, 30:66, 40: 20, 50: 10}
    p_by_w = {}
    for weight, profit in table.items():
        p_by_w[profit / weight] = weight
    k = int(input("Enter knapsack value: "))
    print(table)    
    print(p_by_w)
    sum = 0

    # Sort p_by_w by key here

    

    


    