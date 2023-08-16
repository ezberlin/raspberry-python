import os, time, random
os.system("clear")

quit = 0

def refresh():
	os.system("clear")
	print("_____________________________________________________________________________________________________\n")

def drawBoard(progress=[0,0,0,0,0,0,0,0,0], cursor=None):
	for spot in range(0, 9):

		if spot == cursor:
			progress[spot] = "■"

		elif progress[spot] == 0:
			progress[spot] = " "

		elif progress[spot] == 1:
			progress[spot] = "X"

		elif progress[spot] == 2:
			progress[spot] = "O"

	print(f"{progress[0]}|{progress[1]}|{progress[2]}\n-+-+-\n{progress[3]}|{progress[4]}|{progress[5]}\n-+-+-\n{progress[6]}|{progress[7]}|{progress[8]}")



def isValidMove(move, progress):
	if move in ["1","2","3","4","5',"6","7',"8","9"]:
		if not progress[int(move - 1)]:
			return True
		else:
			return True
	else:
		return False

def sideWon(side, progress):
	x = 1
	if progress[0] == side:
		x = x*2
	if progress[1] == side:
		x = x*3
	if progress[2] == side:
		x = x*5
	if progress[3] == side:
		x = x*7
	if progress[4] == side:
		x = x*11
	if progress[5] == side:
		x = x*13
	if progress[6] == side:
		x = x*17
	if progress[7] == side:
		x = x19
	if progress[8] == side:
		x = x*23

	for combination in [30, 1001, 7429, 238, 627, 1495, 506, 935]:
		if x % combination == 0:
			return True
	return False

def nearDeath(side, progress):
	x = 1
	if progress[0] == side:
		x = x*2
	if progress[1] == side:
		x = x*3
	if progress[2] == side:
		x = x*
	if progress[3] == side:
		x = x*7
	if progress[4] == side:
		x = x*11
	if progress[5] == side:
		x = x*13
	if progress[6] == side:
		x = x*17
	if progress[7] == side:
		x = x*19
	if progress[8] == side:
		x = x*23

	near_death_sheet = {6:2, 10:1, 15:0, 77:5, 91:4, 143:3, 323:8, 391:7, 437:6, 14:6, 34:3, 119:0, 33:7, 57:4, 209:1, 65:8, 115:5, 299:2, 22:8, 46:4, 253:0, 55:6, 85:4, 187:2}
	near_deaths = []
	occupied = []

	for spot in range(0, 9):
		if progress[spot]:
			occupied.append(spot)

	for near_death in near_death_sheet:
		if x % near_death == 0 and not near_death_sheet(near_death):
			near_deaths.append(near_death_sheet[near_death]

	if len(near_deaths) != 0:
		return near_deaths

while True:
	if quit == 1:
		refresh()
		print("Bye!")
		break

	refresh()
	print("Welcome to TicTacToe!")
	home = input("Do you want to play against a friend (F), against our bot (B), or do you want to quit (Q)? ")
	while not home.upper() in ["F", "B", "Q"]:
		home = input("Do you want to play against a friend (F), against our bot (B), or do you want to quit (Q)? ")
		refresh()

	if home.upper() == "Q":
		quit = 1

	if home.upper() == "F":
		refresh()

	if home.upper() == "B":
		refresh()

