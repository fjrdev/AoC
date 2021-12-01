import re

raw_data = []
f = open('passwords.txt', 'r')
raw_data = f.readlines()

correct_pw = 0

# iterate through list and run validation test for each entry:
for elem in raw_data:

    elem = list(elem)

    # extract the defined char limit at beginning of each entry
    raw_limit_string = "" 
    for _ in range(0, len(elem)):
        if elem[0] == " ":
            del elem[0]
            break
        raw_limit_string += elem[0]
        del elem[0]

    # extract limits off raw_limit_strings
    work_limit_list = re.findall("[0-9]+", raw_limit_string)
    work_limit_list = list(map(int, work_limit_list))
    
    min_occ = work_limit_list[0]
    max_occ = work_limit_list[1]

    # extract char off of elem
    looked_char = elem[0]
    for _ in range(0, 3):
        del elem[0]
    
    # look for right apperance of looked_char in elem:
    real_occ = elem.count(looked_char)
    if real_occ < min_occ or max_occ < real_occ:
        continue
    
    correct_pw += 1

print(correct_pw)
