# workout tracking for original P90X training sets
# version 1 - record reps for all exercises, do some math, write to csv
# pull data from previous csv maybe version 2

import csv, sys
from datetime import date
today = date.today()

def chest_back_day():
	print("\n\nWelcome to Chest & Back Day\n\nI hope you decided to bring it today, but I guess\nthere's only one way to find out....\nLET'S DO THIS SHIT\nROUND ONE\n\n")
	round_one = {}
	round_one['Standard Pushups']= int(input("Round 1 Standard Push Ups: "))
	round_one['Wide Pullups'] = int(input("Round 1 Wide Front Pull-Ups: "))
	round_one['Military Pushups'] = int(input("Round 1 Military Push Ups: "))
	round_one['Chin Ups'] = int(input("Round 1 Chin Ups: "))
	round_one['Wide Pushups'] = int(input("Round 1 Wide Fly Push Ups: "))
	round_one['Close Pullups'] = int(input("Round 1 Close Overhand Pull Ups: "))
	round_one['Decline Pushups'] = int(input("Round 1 Decline Push Ups: "))
	round_one['Heavy Pants'] = int(input("Round 1 Heavy Pants: "))
	round_one['Diamond Pushups'] = int(input("Round 1 Diamond Push Ups: "))
	round_one['Lawn Mowers'] = int(input("Round 1 Lawn Mowers: "))
	round_one['Dive Bombers'] = int(input("Round 1 Dive Bombers: "))
	round_one['Back Flys'] = int(input("Round 1 Back Flys: "))

	rd_one_push_tot = round_one['Standard Pushups'] + round_one['Military Pushups'] + round_one['Wide Pushups'] + round_one['Decline Pushups'] + round_one['Diamond Pushups']
	rd_one_pull_tot = round_one['Wide Pullups'] + round_one['Chin Ups'] + round_one['Close Pullups'] 
	print("\nFantastic workout so far!")
	print("\n\nIt's time for Round 2. This is where you improve. Let's do it!\n\nROUND 2!!\n")
	# Round 2 #
	round_two = {}
	round_two['Wide Pullups'] = int(input("Round 2 Wide Front Pull-Ups: "))
	round_two['Standard Pushups'] = int(input("Round 2 Standard Push Ups: "))
	round_two['Chin Ups'] = int(input("Round 2 Chin Ups: "))
	round_two['Military Pushups'] = int(input("Round 2 Military Push Ups: "))
	round_two['Close Pullups'] = int(input("Round 2 Close Overhand Pull Ups: "))
	round_two['Wide Pushups'] = int(input("Round 2 Wide Fly Push Ups: "))
	round_two['Heavy Pants'] = int(input("Round 2 Heavy Pants: "))
	round_two['Decline Pushups'] = int(input("Round 2 Decline Push Ups: "))
	round_two['Lawn Mowers'] = int(input("Round 2 Lawn Mowers: "))
	round_two['Diamond Pushups'] = int(input("Round 2 Diamond Push Ups: "))
	round_two['Back Flys'] = int(input("Round 2 Back Flys: "))
	round_two['Dive Bombers'] = int(input("Round 2 Dive Bombers: "))
	rd_2_push_tot = rd_one_push_tot + round_two['Standard Pushups'] + round_two['Military Pushups'] + round_two['Wide Pushups'] + round_two['Decline Pushups'] + round_two['Diamond Pushups']
	rd_2_pull_tot = rd_one_pull_tot + round_two['Wide Pullups'] + round_two['Chin Ups'] + round_two['Close Pullups']
	

	totals = {}
	for key in round_one.keys():
		if key in round_two:
			totals[key] = round_one[key] + round_two[key]
	print("\n\nBOOM BABY! That's what I'm talkin' about!!\n\nHere's what you accomplished today: \n")
	for key, value in totals.items():
		print(key, '-', value)

	# WRITE TO CSV #
	filename = "chest_back_day_" + str(today)+'.csv'
	fieldnames = [i for i in totals.keys()]
	with open(filename, 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
		writer.writeheader()
		writer.writerow(round_one)
		writer.writerow(round_two)
		writer.writerow(totals)
	
	
	whatnext = input("Press Enter to Continue...")
	main()


def legs_back_day():
	legs_back = {}
	legs_back['Balanced Lunges']  = int(input("Balanced Lunges: "))
	legs_back['Calf Raise Squats'] = int(input("Calf Raise Squats: "))
	legs_back['Chin Ups'] = int(input("Chin Ups: "))
	legs_back['Super Skaters'] = int(input("Super Skaters: "))
	legs_back['Wall Squats'] = True if input("Wall Squats completed? Y/N: ") == 'y' else False
	legs_back['Wide Pullups'] = int(input("Wide Pullups: "))
	legs_back['Step Back Lunge'] = int(input("Step Back Lunge: "))
	legs_back['Alt Side Lunge'] = int(input("Alternating Side Lunge: "))
	legs_back['Close Pullups'] = int(input("Close Grip Pullups: "))
	legs_back['Single Wall Squat'] = True if input("Single Leg Wall Squats completed? Y/N: ")== 'y' else False
	legs_back['Deadlift Squats'] = int(input("Deadlift Squats: "))
	legs_back['Switch Pullups'] = int(input("Switch Grip Pullups (total): "))
	legs_back['Three Way Lunge'] = int(input("Three Way Lunge: "))
	legs_back['Sneaky Lunge'] = int(input("Sneaky Lunge: "))
	legs_back['Chin Ups'] += int(input("Chin Ups: "))
	legs_back['Chair Salutations'] = True if input("Chair Salutations completed? Y/N: ") == 'y' else False
	legs_back['Toe Roll Lunge'] = int(input("Toe Roll Lunge: "))
	legs_back['Wide Pullups'] += int(input("Wide Pullups: "))
	legs_back['Groucho Walk'] = int(input("Groucho Walk: "))
	legs_back['Calf Raises'] = int(input("Total Calf Raises: "))
	legs_back['Close Pullups'] += int(input("Close Grip Pullups: "))
	legs_back['Speed Squats'] = int(input("Siebers-Speed Squats: "))
	legs_back['Switch Pullups'] += int(input("Switch Grip Pullups (total): "))


	# WRITE TO CSV #
	filename = "leg_back_day_" + str(today)+'.csv'
	fieldnames = [i for i in legs_back.keys()]
	with open(filename, 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
		writer.writeheader()
		writer.writerow(legs_back)


	print("\nEXCELLENT work today!\n\nYou completed {}".format(legs_back))
	whatnext = input("Press Enter to Continue...")
	main()

def main():
	print("\nTime......To......WORK THE FUCK OUT!!!!!!!\n\nWhat are we feeling...\n")
	print("1 - Chest & Back\n2 - Legs & Back\n3 - Shoulders & Arms\n4 - Core Synergistics\n5 - Chest, Shoulders, Triceps\n6 - Back & Biceps\n7 - Ab Ripper\n'Q' - Today is DONE\n")
	program = input()
	if program.lower() == 'q':
		sys.exit("I better see you tomorrow you big pussy...")
	elif program.lower() == '1':
		chest_back_day()
	elif program.lower() == '2':
		legs_back_day()
	elif program.lower() == '3':
		shoulders_arms_day()
	elif program.lower() == '4':
		core_synergistics_day()
	elif program.lower() == '5':
		chest_shoulders_tris()
	elif program.lower() == '6':
		back_biceps_day()
	elif program.lower() == '7':
		ab_ripper()
	sys.exit('fix this shit')

main()