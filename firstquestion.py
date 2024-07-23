def find_integers_with_two_occurrences_and_one_occurrence(num, arr):
    count_map = {}
    result = []


 # Count occurrences of each number in arr
    for number in arr:
        if number in count_map:
            count_map[number] += 1
        else:
            count_map[number] = 1

# Find numbers with exactly two occurrences and at least one occurrence of num
    for key, value in count_map.items():
        if value == 2 and key != num:
            result.extend([key, key])  # Add two occurrences of the number
        elif value >= 1 and key == num:
            result.append(key) 