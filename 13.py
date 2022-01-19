# Complete the script, so it generates the expected output using my_range as input data. Please note that the items of the expected list output are all strings
# my_range = range(1, 21)
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']


my_range = range(1,21)
# final_range = []

final_range = list(map(str, my_range))

print(final_range)
