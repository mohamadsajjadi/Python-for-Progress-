#in this program, we want to print big Multiplication Table
inp = int(input())
for i in range(1, inp + 1):
    for j in range(1, inp + 1):
        print(i * j, end=" ")
    print("\n")
