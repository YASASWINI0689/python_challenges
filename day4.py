data = [10, "Python", "", 25, "Loop", 40]

number_list = [0] * len(data)
string_list = [""] * len(data)

n_index = 0
s_index = 0

for item in data:
    if type(item) == int or type(item) == float:
        number_list[n_index] = item
        n_index = n_index + 1
    elif type(item) == str:
        if item != "":
            string_list[s_index] = item
            s_index = s_index + 1

num_count = n_index
str_count = s_index

name = "Yasaswini"

if len(name) % 2 != 0:
    if n_index > 0:
        n_index = n_index - 1
    if s_index > 0:
        s_index = s_index - 1
else:
    if n_index > 0:
        for i in range(1, n_index):
            number_list[i-1] = number_list[i]
        n_index = n_index - 1
    if s_index > 0:
        for i in range(1, s_index):
            string_list[i-1] = string_list[i]
        s_index = s_index - 1

final_numbers = []
for i in range(n_index):
    final_numbers = final_numbers + [number_list[i]]

final_strings = []
for i in range(s_index):
    final_strings = final_strings + [string_list[i]]

print("Numbers List:", final_numbers)
print("Strings List:", final_strings)
print("Total Numbers:", num_count)
print("Total Strings:", str_count)
