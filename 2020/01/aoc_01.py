import re 

raw_data = []
f = open('data.txt', 'r')
raw_data = f.readlines()

# convert raw_data to string
string_data = "".join(raw_data)

# use regex to filter out the \n:
work_data = re.findall("[0-9]+", string_data)

# convert string to int:
work_data = list(map(int, work_data))

print(work_data)

result = 0
for x in range(0, len(work_data)):
    for y in range(x, len(work_data)):
        if work_data[x] + work_data[y] == 2020:
            result = work_data[x] * work_data[y]
            break
    if result > 0:
        break

print(result)
