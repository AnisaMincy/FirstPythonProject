print ("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("How old are you? "))
#variables for resources in the game
health = 20
coin = 100
metal = 0
wood = 0
food = 15

print("Hello", name, "you are", age, "years old!")
if age <= 5:
	print("You are not old enough to play this game!:(")
elif age >= 6:
	print("You are old enough to play!")
	play = input("Are you ready to play? Yes or no ").lower()
	if play == "yes":
		print("Get ready to play the game!")
		print("                  ")
		weapon = input("Choose a weapon! [sword/axe/club] ").lower()
		print("        ")
		print("These are your resources:")
		print("Health:", health,)
		print("Coin:", coin,)
		print("Metal:", metal,)
		print("Wood:", wood,)
		print("Weapon:", weapon,)
		print("Food:", food,)
		print("                     ")
		direction = input("Which way do you want to go? left, right, or forward? ").lower()

		if direction == "left":
			print("You turn left and come upon a rickety bridge, what do you do?")
			bridge = input("dart across, walk across slowly, or turn back around. [dart/walk/back] " ).lower()
			#At the bridge
			if bridge == "dart":
				print("        ")
				print("You quickly dart across the bridge and make it to the other side safely! You look at your surrondings and find a grassy field with a dirt path going down the middle. What do you do?")
				path=input("Follow the path or venture on your own? [path/venture] ").lower()
				if path == "path":
					print("             ")
					print("You walk down the dirt path and along the way you find some wood and an apple tree.")
					wood+= 4
					food+= 10
					print("       ")
					print("Wood:", wood,)
					print("Food:", food,)
					print("You keep walking down the path and you soon reach a house. What do you do?")
					house = input("Do you enter the house or keep walking? [enter/walk] ")
					if house == "enter":
						print(" ")
						print("You knock on the door of the house and the door swings open. You call out, but no one seems to be inside. What do you do?")
						house_entrance = input("Do you stay inside for the night or leave? [stay/leave] ")
					elif house == "walk":
						print(" ")
						print("You walk away from the house and keep going down the dirt path.")
				elif path == "venture":
					print("         ")
					print("You venture off into the field and cross paths with a wild boar! What do you do?")
					wild_boar= input("Stay and fight or run away? [fight/run] ").lower()
					#wild boar
					if wild_boar == "fight":
						print("        ")
						print("You brandish your weapon and charge the wild boar. You got roughed up a bit,")
						print("       ")
						health-= 3
						print("Health:", health,)
						if health == 0:
							print("You ran out of health!")
							print("GAME OVER")
						else:
							print("           ")
							print("but you manage to defeat the boar and find dinner!")
							print("     ")
							food += 4
							print("Food:", food,)
			elif bridge == "walk":
				print("            ")
				print("You walk slowly and carefuly across the bridge. As you slowly walk across, the bridge gives under your weight and you fall into the river below it. You are swept downstream and get hit by many branches before you get to safety.")
				print("         ")
				health -= 5
				print("Health:",health)
				print("            ")
				if health == 0:
					print("You ran out of health!")
					print("GAME OVER!")
				else:
					print("You finally find your way back to shore and find yourself at the edge of a dark forest. What do you do?")
					edge_forest= input("Get some sleep or go into the forest? [sleep/forest] ").lower()
					if edge_forest == "sleep":
						print("You get a good night's rest and wake up feeling better!")
						print("        ")
						health += 2
						print("Health:", health)
					elif edge_forest == "forest":
						print("You gather your strength and make your way into the dark forest. What do you do?")
						dark = input("Do you stop and chop some wood or keep walking? [chop/walk] ").lower()
						if dark == "chop":
							print("        ")
							print("You bring out your", weapon, "and start chopping at a tree.")
							if weapon == "sword":
								print("     ")
								print("Since you have a sword you get very little wood and angry about how much time you wasted.")
								print(" ")
								wood += 5
								health -= 5
								print("Wood:", wood)
								print("Health:", health)
								print(" ")
								print("You are cold, tired, and in the middle of the forest. What do you do?")
								cold_tired = input("Do you make a fire with the small amount of wood you have, head back to the shore, or keep pushing forward? [fire/shore/forward] ").lower()
								if cold_tired == "fire":
									print(" ")
									print("You take your wood and manage to make a fire! It took five pieces of wood but it was worth it because now you are warm!")
									print(" ")
									wood-= 5
									health += 3
									print("Wood:", wood)
									print("Health:", health)
									print(" ")
									if health == 0:
										print("You ran out of health!")
										print("GAME OVER!")
									else:
										print("Now that you are warm, what do you do?")
										warm_forest = input("Do you get some rest or keep going forward? [rest/forward] ").lower()
										if warm_forest == "rest":
											print("You put out the fire and get some rest")
								if cold_tired == "shore":
									print(" ")
									print("You turn around and head in the direction you think you came from. After hours of walking it becomes apparent to you that you have no idea where you are and the shore is nowhere in sight. What do you do?")
									lost_forest = input("Do you wait until the morning or keep going forward? [wait/forward] ").lower()
							elif weapon == "axe":
								print("    ")
								print("Since you have an axe, you have are able to get a lot of wood!")
								wood += 15
								print("Wood:", wood)
							elif weapon == "club":
								print(" ")
								print("Since you have a club, you are not able to get any wood at all.")
						elif dark == "walk":
							print(" ")
							print("You keep walking and it is not long before you start shivering.")
			elif bridge == "back":
				print("You decide it's way too risky and walk back to where you came from.")
		elif direction == "right":
			print("You turn left and approach a small cave what do you do?")
			cave = input("Walk inside or turn around. [inside/around] " ).lower()
			if cave == "inside":
				print("You walk inside the pitch black cave and try to feel around. You find a crate full of metal! ")
				print(" ")
				metal += 15
				print("Metal:", metal)
				print(" ")
				print("You feel around, but don't feel anymore metal. What do you do?")
				cave_metal = input("Do you keep going forward or do you leave the cave [forward/leave] ").lower()
				print(" ")
				if cave_metal == "forward":
					print("Despite not being able to see, you still stumble forward in the dark.")
				elif cave_metal == "leave":
					print("You turn around and leave the cave not wanting to hurt yourself stumbling in the dark.")
		elif direction == "forward":
			print("You walk forward and approach a small town, what do you do?")
			town = input("Walk into town or turn back. ").lower()
			if town == "walk into town":
				print("               ")
				print("You walk into town and meet some friendly people! They give you some money and food for your journey!")
				coin += 50
				food += 5
				print("             ")
				print("Coin:",coin,)
				print("Food:",food,)
		elif town == "turn back":
			print("You turn around and go back to where you started.")

	else:
		print("Bye", name)
