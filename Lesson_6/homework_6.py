#  Task 1
proposed_string :str = input("Provide your string here please: ")

unique_counter : int = sum([1 for char in proposed_string if proposed_string.count(char) == 1])

print(unique_counter)

if unique_counter > 10:
    print(True)
else:
    print(False)

#  Task 2

is_correct_srt: bool = False
while not is_correct_srt:
    provided_word : str = input("Provide your wordp please: ").lower()

    if provided_word.find("h") != -1:
        is_correct_srt = True

#  Task 3
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

desired_list : list [str] = [item for item in lst1 if isinstance(item, str)]

print(desired_list)

#  Task 4

provided_list : list[int] = [1,2,3,4,5,6,7,8,9,10]

result : int = sum([integer for integer in provided_list if integer % 2 == 0 ])

print(result)