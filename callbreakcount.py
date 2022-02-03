## -*- coding: utf-8 -*-
# Program Name: callbreakcount.py
# Authors: Z10  @jg0213
# Date: 2-2-22
# Program Description: Count the score after each round, total 5 round and highest scorer wins
import time
n1 = int(input('How many players do you have?'))
time.sleep(1)
unable = ("not possible to play, need 4 players")
able = ('thats awesome, lets play, Time to get player\'s names')
# need to figure out the loop back-go back up
if n1 == int(4):
	print(able)
else:
	print(unable)
	exit()

P1 = input("What is the name of Player 1?")
time.sleep(0)
P2 = input("What is the name of Player 2?")
time.sleep(0)
P3 = input("What is the name of Player 3?")
time.sleep(0)
P4 = input("What is the name of Player 4?")
time.sleep(0)


print(f' \n Welcome to the Card Game Called CALL BREAK \n {P1} {P2} {P3} {P4}')

# Shuffle card and distribute
# BID SCORE: Player1_bid, Player2_bid..

# ROUND1
# for _ in itertools.repeat(None, 5):
p1total = 0
p2total = 0
p3total = 0
p4total = 0

for X in range(1, 3):

	#print(f'How does it look for round {X} ?')
	P1_b1 = int(input(f'how much bid do {P1} want to call for?'))
	time.sleep(.5)
	P2_b1 = int(input(f'how much bid do {P2} want to call for?'))
	time.sleep(.5)
	P3_b1 = int(input(f'how much bid do {P3} want to call for?'))
	time.sleep(.5)
	P4_b1 = int(input(f'how much bid do {P4} want to call for?'))
	time.sleep(.5)
	# # check the total
	# if P1_b1 + P2_b1 + P3_b1 + P4_b1 > 13:
	# 	print('The game is dangerous, at least one person will fail')
	# elif P1_b1 + P2_b1 + P3_b1 + P4_b1 == 13:
	# 	print('the game is tight')
	#
	# 	bid_score = (P1_b1 + P2_b1 + P3_b1 + P4_b1)
	# 	print(bid_score)
	# #print(f'How much did you all score in round {X} ?')

	for i in range(1):

		P1_a1 = int(input(f'how much {P1} scored?'))
		P2_a1 = int(input(f'how much {P2} scored?'))
		P3_a1 = int(input(f'how much {P3} scored?'))
		P4_a1 = int(input(f'how much {P4} scored?'))
		score = P1_a1 + P2_a1 + P3_a1 + P4_a1

		if score != 13:
			print('The scores are wrong, total should be 13')
			continue


		else:
			print('lets see the round total')

		# finalize Round 1 score FOR EACH PLAYER

		if P1_b1 == P1_a1:
			P1_R1 = P1_a1
		elif P1_b1 > P1_a1:
			P1_R1 = -(P1_b1)
		else:
			P1_R1 = P1_b1 + (P1_a1 - P1_b1) / 10

		if P2_b1 == P2_a1:
			P2_R1 = P2_a1
		elif P2_b1 > P2_a1:
			P2_R1 = -(P2_b1)
		else:
			P2_R1 = P2_b1 + (P2_a1 - P2_b1) / 10

		if P3_b1 == P3_a1:
			P3_R1 = P3_a1
		elif P3_b1 > P3_a1:
			P3_R1 = -(P3_b1)
		else:
			P3_R1 = P3_b1 + (P3_a1 - P3_b1) / 10

		if P4_b1 == P4_a1:
			P4_R1 = P4_a1
		elif P4_b1 > P4_a1:
			P4_R1 = -(P4_b1)
		else:
			P4_R1 = P4_b1 + (P4_a1 - P4_b1) / 10

		print(P1_R1)
		print(P2_R1)
		print(P3_R1)
		print(P4_R1)

	p1total = p1total + P1_R1
	p2total = p2total + P2_R1
	p3total = p3total + P3_R1
	p4total = p4total + P4_R1

	time.sleep(1)
	print(f' Total score for  {P1} is {p1total} \n Total score for {P2} is {p2total} \n Total score for {P3} is {p3total} \n Total score for player{P3} is {p4total}')

# 	s3 = P1_R1
# elif X == 4:
# 	s4 = P1_R1
# elif X == 5:
# 	s5 = P1_R1
# else:
# 	print('done')

# sumtotal=(s1+s2+s3+s4+s5)
# print(sumtotal)
