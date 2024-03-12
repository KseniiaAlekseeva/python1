###1 empty file __init
# import modules.module1
#
# modules.module1.guess_number(0, 50, 4)
###1 empty file __init

###2
from modules import guess_number
from modules import start_riddles
from modules import check_date
from modules import is_good_position, find_good_position

# print(guess_number(0, 50, 4))
# start_riddles()
# print(check_date("12.13.1234"))
print(is_good_position([[1, 1], [5, 2], [8, 3], [6, 4], [3, 5], [7, 6], [2, 7], [4, 8]]))
print(is_good_position([[2, 1], [5, 2], [8, 3], [6, 4], [3, 5], [7, 6], [2, 7], [4, 8]]))
pos = find_good_position(4)

###2
