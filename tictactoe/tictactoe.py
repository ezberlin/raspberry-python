import os, time, random
from getkey import getkey, keys
key = getkey()
#if key == keys.UP:
	# Handle the UP key
#elif key == keys.DOWN:
	# Handle the DOWN key
#elif key == 'a':
	# Handle the `a` key
#elif key == 'Y':
	# Handle `shift-y`

os.system("clear")

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
	if move in ["1","2","3","4","5","6","7","8","9"]:
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

def nearDeath(progress, side):
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
			near_deaths.append(near_death_sheet[near_death])

	if not len(near_deaths) == 0:
		return near_deaths

def bot(progress, side, difficulty):
	occupied = []
	for spot in range(0, 9):
		if progress[spot]:
			occupied.append(spot)

	if difficulty == 0:
		options = []
		for spot in range(0, 9):
			if not spot in occupied:
				options.append(spot)
		return random.choice(options)

	else:
		if nearDeath(progress, side):
			return random.choice(nearDeath(progress, side))
		elif nearDeath(progress, 3 -side):
			return random.choice(nearDeath(progress, 3 -side))
		else:
			priority_0 = [4]
			priority_1 = [0, 2, 6, 8]
			priority_2 = [1, 3, 5, 7]
			if 4 in occupied:
				del priority_0[0]
			for spot in priority_1:
				if spot in occupied:
					del priority_1[priority_1.index(spot)]
			for spot in priority_2:
				if spot in occupied:
					del priority_2[priority_2.index(spot)]


			if len(priority_0) != 0:
					return random.choice(priority_0)

			elif difficulty == 1:
				if len(priority_2) != 0:
					return random.choice(priority_2)
				else:
					return random.choice(priority_1)

			else:
				if len(priority_1) != 0:
					return random.choice(priority_1)
				else:
					return random.choice(priority_2)
#keyboard.is_pressed(key)
#keyboard.wait(key)

quit = 0
cursor = 4

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
		progress = [0,0,0,0,0,0,0,0,0]
		for turn in range(0, 9):
			done = False
			ticks = 0
			while done == False:
				refresh()
				if ((ticks - (ticks%10))/10) % 2 == 0:
					drawBoard(progress, cursor)
				else:
					drawBoard(progress)
				if turn % 2 == 0:
					print("It's X's turn. Choose the right square with the arrow keys and press Enter.")
					time.sleep(0.1)
					if key == keys.UP:
						if cursor > 2:
							cursor = cursor-3
						else:
							cursor = cursor+6
					if key == keys.DOWN:
						if cursor < 6:
							cursor = cursor+3
						else:
							cursor = cursor-6
					if key == keys.LEFT:
						if cursor % 3 > 0:
							cursor = cursor-1
						else:
							cursor = cursor+2
					if key == keys.RIGHT:
						if cursor % 3 < 2:
							cursor = cursor+1
						else:
							cursor = cursor-2


	if home.upper() == "B":
		refresh()

