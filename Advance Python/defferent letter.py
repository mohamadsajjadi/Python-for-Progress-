# input
# 4
# ali
# karim
# abbas
# mohammad

# result
# 5
# Print A number on the only output line that is equal to the number of different letters in the selected name.

n = int(input())
max = 0
for i in range(n):
    t = ''
    my_input = input()
    for char in my_input:
        if char not in t:
            t += char
    if len(t) > max:
        max = len(t)
print(max)
