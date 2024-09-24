first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# 1 first_result
first_result = [len(s) for s in first_strings if len(s) >= 5]

# 2 second_result
second_result = [(s1, s2) for s1 in first_strings for s2 in second_strings if len(s1) == len(s2)]

# 3 third_result
combined_strings = first_strings + second_strings
third_result = {s: len(s) for s in combined_strings if len(s) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)