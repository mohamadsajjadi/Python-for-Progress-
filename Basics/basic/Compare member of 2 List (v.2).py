number = int(input())
counter = 0
expected_text = [item for item in input()]
entered_text = [member for member in input()]
i = 0
while True:
    if expected_text[i] != entered_text[i]:
        counter += 1
    i += 1
    if i == number:
        break
print(counter)
