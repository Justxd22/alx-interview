#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3]))) # ben
print("Winner: {}".format(isWinner(3, [4, 5, 1]))) # ben 
print("Winner: {}".format(isWinner(2, [10, 20]))) # ben
print("Winner: {}".format(isWinner(4, [7, 6, 8, 9]))) # ben
print("Winner: {}".format(isWinner(3, [10, 15, 12]))) # ben
print("Winner: {}".format(isWinner(2, [6, 7]))) # maria out: none
print("Winner: {}".format(isWinner(3, [9, 10, 12]))) # maria  out: ben
print("Winner: {}".format(isWinner(2, [14, 15]))) # maria out: ben