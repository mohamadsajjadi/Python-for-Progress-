number = int(input())
expected_text = [item for item in input()]
entered_text = [member for member in input()]
final_list = []
for a, b in zip(expected_text, entered_text):
    if a == b:
        final_list.append(a)
print(len(expected_text) - len(final_list))
