'''
CHALLENGE DESCRIPTION:

The major element in a sequence with the length of L 
is the element which appears in a sequence more than L/2 times. 
The challenge is to find that element in a sequence.
'''

line = "92,19,19,76,19,21,19,85,19,19,19,94,19,19,22,67,83,19,19,54,59,1,19,19"


def major_element(line):
    line_array = line.split(",")
    minimum_count = len(line_array) / 2
    my_dict = {}
    flag = False
    # pu.db
    for num in line_array:
        count = 1
        if num in my_dict:
            count = my_dict.get(num)
            count += 1
        my_dict[num] = count
        if count >= minimum_count:
            return num
    if flag is False:
        return None

print(major_element(line))
