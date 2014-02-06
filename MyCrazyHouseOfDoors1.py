import random

prize = ['head exploding', 'poop pie', 'free ride on the exploading rocket train', 'pet little floppy tongue ghost', 'book of insults', 'book of jokes', 'map of the way out of the house', 'magical bubble gum', 'enchanted tooth pick', 'used toilet paper', 'moldy sandwich', 'Excalibur', 'head chopped off and mounted on a steak', 'rotten brain', 'chest of gold', 'dragon statue', 'friendly dragon to fly on', 'HUG!', 'GIANT dimond', 'pet sea serpent', 'baby parasite that is going to eat your braens', 'worst videogame ever', 'random, shreaded, common traiding card', 'jar of dirt']

reward = random.choice(prize)

credits = """
-CREDITS-
game story by Isaiah Paul Williams
directed by Isaiah Paul Williams
programmed by Isaiah Paul Williams
credits by Isaiah Paul Williams
The End...
... by Isaiah Paul Williams
"""
line = "*"*60

print line
print "Welcome to 'My Crazy house of Doors'."
print line
print """
This is the game where you enter random
doors just to see what happens.
-BEEE WARNED!!!!!-
You may die behind a door!
Or worse... you might be trapped forever....
Well if that does not happen you will obtain
the 'ULTIMATE UNKOWN MYSTERIOUS EPICLY FANTASTIC
VALUABLE ODDILY AMAZINGLY SURPRIZING PRIZE'
-Good Luck
"""
print "********************"
print "You enter the house and see 3 doors. What do you do?"
print """
1-Enter door 1
2-Enter door 2
3-Enter door 3
4-Run away screaming at the top of your lungs!
"""

door = raw_input("Choose Wisely>>>")

if door == "1":
	print line
	print "You see two more doors. What do you do?"
	print """
	1-enter door 1
	2-enter door 2
	3-give up...
	"""
	
	door1 = raw_input(">>>")
	
	if door1 == "3":
		print line
		print "You turned back and found yourself in a blank expance."
		print "you are trapped... game over."
		print credits
	if door1 == "1":
		print line
		print "You walk into the room and look up. \nA knife stabs your face and you die... \nGame over"
		print credits
	if door1 == "2":
		print line
		print "you enter a hall with 5 moor doors. What do you do?"
		print "1-enter door 1"
		print "2-enter door 2"
		print "3-enter door 3"
		print "4-enter door 4"
		print "5-enter door 5"
		print "6-give up and die"
		
		door1_2 = raw_input("Hard Choice >>>")
		
		
		if door1_2 == "6":
			print line
			print "you faint and die"
			print "GAME OVER SCARDY CAT!"
			print credits
		elif door1_2 == "1":
			print line
			print "The door comes to life and eats you!"
			print "GAME OVER... You are now lunch."
			print credits
		elif door1_2 == "2":
			print line
			print "The door comes to life and eats you!"
			print "GAME OVER... You are now lunch."
			print credits
		elif door1_2 == "4":
			print line
			print "The door comes to life and eats you!"
			print "GAME OVER... You are now lunch."
			print credits
		elif door1_2 == "5":
			print line
			print "The door comes to life and eats you!"
			print "GAME OVER... You are now lunch."
			print credits
		elif door1_2 == "3":
			print line
			print "You enter an odd dark room with two doors. What do you do?"
			print """
			1-enter door 1
			2-enter door 2
			3-lay down and rest(you deserve it)
			"""
			
			door124 = raw_input("BEWARE!!!>>>")
			
			if door124 == "2":
				print line
				print "you see a friendly dragon and it ,by accident\n, sneezes on you, roasting your body..."
				print "GAME OVER!!! YOU LOOSE!!!"
				print credits
			elif door124 == "3":
				print line
				print "You awaken, and before you eyes the doors vanish!"
				print "you are forever trapped... Game over!"
				print credits
				
			elif door124 == "1":
				print line
				print "you enter a room with 100 doors!" 
				
				door100 = raw_input('Coose a number')
				
				if door100 == "27":
					print "You see a huge monster. looks at you and says"
					print"'you puny little thing. Choose your weapon and fight me!'"
					print "you see three weapons. You cannot escape!"
					print """
					1-Rocket Launcher
					2-Tooth Pick
					3-Excalibur
					"""
					
					boss1 = raw_input("I can't watch... your going to DIE!>>>")
				
					if boss1 == "3":
						print line
						print "You grab the Legendary Blade Excalibur..."
						print "but you can not pull it out of the stone!"
						print "The monster steps on you and you die"
						print "Game Over!!!"
						print credits
					elif boss1 == "1":
						print line
						print "You pull the trigger only to lean the \nhard way that its has no ammo!"
						print "The monster laughs and then eats you."
						print "game over looser..."
						print credits
					elif boss1 == "2":
						print line
						print "The monster laughs at you as you prick it with the tooth pick"
						print "The monsters laughing stops and he turnes to dust!"
						print "**********"
						print "You win! I always knew you could!"
						print "Enjoy your %s" % reward
						print credits
				
				else:
					print line
					print "you open door %s and a jet of flame engulfs you and you die." % door100
					print "Game Over... too bad... so sad... I bet you are MAD..."
					print credits
elif door == "3":
	print line
	print "the door locks behind you. You see three switches"
	print "1-pull the red switch"
	print "2-pull the blue switch"
	print "3-pull the purple switch"
	
	switch = raw_input('What do you do?>>>')
	
	if switch == "1":
		print line
		print "You burst into flame and die!"
		print "Game over 'Hot Shot'"
		print credits
	elif switch == "2":
		print line
		print "You become a human popcical"
		print "game over 'sucker'! You have to stay here and forever 'cool it'"
		print credits
	elif switch == "3":
		print line
		print "You decide to pull the purple switch."
		print "A trap door opens up and you fall into an underground cavern."
		print "you see 5 caves..."
		print "1-enter cave 1"
		print "2-enter cave 2"
		print "3-enter cave 3"
		print "4-enter cave 4"
		print "5-enter cave 5"
		
		cave = raw_input('What kind of "cave person" are you?>>>')
		
		if cave == "4":
			print line
			print "You emerge in a large mettle room with three doors"
			print "You think you should enter one, they each have writing on them."
			print "1-enter the door that says 'open me'"
			print "2-enter the door that says 'EXIT' in flashing letters."
			print "3-enter the door that says 'Boss Battle in here'"
			
			wdoor = raw_input('one might be a way out...>>>')
			
			if wdoor == "2":
				print line
				print "open the door that says 'EXIT' and you get pulled through"
				print "a worm hole and tossed into the vacuum of space were you die."
				print "Game Over space man!"
				print credits
			elif wdoor == "3":
				print line
				print "You see a giant robot and the door locks behind you"
				print "You see three weapons."
				print "1-plasma cannon"
				print "2-feather"
				print "3-Light-Sabre"
				
				fakeboss1 = raw_input('YOU CAN DO THIS!!!>>>')
				
				if fakeboss1 == "1":
					print line
					print "You fire the plasma cannon and the robots head gets blown off"
					print "Suddenly, it leans your way and falls on top of you!"
					print "I guess you killed it... You still get a GAME OVER, however..."
					print credits
				elif fakeboss1 == "2":
					print line
					print "You try to tickle it with the feather... no efect."
					print "It steps on you and you die..."
					print "I was sure that would work... O well. GAME OVER!!!"
					print credits
				elif fakeboss1 == "3":
					print line
					print "Seeing that you are a Jedi the robot turns its hand into an even bigger"
					print "Light-Sabre and cuts your head off from a distance..."
					print "The Force is not strong with this one... GAME OVER"
					print credits
				
			elif wdoor == "1":
				print line
				print "You enter a room with unlimited doors..."
				print "the door locks behind you so you must choose a door."
				
				undoor = raw_input('Just choose any number and go that way!>>>')
				
				if undoor == "1997":
					print line
					print "you enter door 1997 and find a large eyeball"
					print "It shoots a laser at the door, welding it shut."
					print "You have to fight!"
					print "There are 2 weapons"
					print "1-Pepper spray"
					print "2-butter-knife"
					
					boss3 = raw_input('I cant watch!>>>')
					
					if boss3 == "1":
						print line
						print "You use the pepper spray"
						print "You make it really MAD and it ZAPS you."
						print "You lost that staring contest... GAME OVER!"
						print credits
					elif boss3 == "2":
						print line
						print "right as you hold out the butter-knife it shoots a beam at you."
						print "The beam hits the knife and bounced back striking the eye!"
						print"***************"
						print "You win! That was smart of you using the knife like a mirror to reflect the light."
						print "Now for your prize... enjoy your %s!" % reward
						print credits
					
				else:
					print line
					print "You enter door %s and you get sucked into a black hole and die..." % undoor
					print "You not coming 'BLACK' are you? GAME OVER"
					print credits
		else:
			print line
			print "You enter the cave and walk for awhile"
			print "up ahead you see something move..."
			print "You hear a growl and it pounces you..."
			print "The small flesh eating dinosuar (raptor) eats your head off!"
			print "You are now extinct ... game over..." 
			print credits
elif door == "2":
	print line
	print "the door locks behind you and you see two tunnles"
	print "1-enter the dark tunnel"
	print "2-enter the bright tunnel"
	
	tun = raw_input('hmmmm>>>')
	
	if tun == "1":
		print line
		print "You do not see the incoming train and you get hit!"
		print "GAME OVER... Ka-splat!"
		print credits
	elif tun == "2":
		print line
		print "you see two trains... what one do you wish to ride?"
		print "1-the steam engine"
		print "2-the rocket train!"
		
		train = raw_input('trains in a house?>>>')
		
		if train == "2":
			print line
			print "the rocket explodes and you die!"
			print "Game Over... don don dooooon!!!"
			print credits
		elif train == "1":
			print line
			print "The train pulls slowly away from the station"
			print "Up ahead you see a lava pit! The train is beginning to accelerate"
			print "and you can't stop it! You are about to plunge into lava!"
			print "What do you do!"
			print "1-jump off the train to the right"
			print "2-jump off the train to the left"
			print "3-stay put"
			
			trainw = raw_input('What to do!>>>')
			
			if trainw == "1":
				print line
				print "You leap from the train and get splattered \non a pole you did not see there."
				print "GAME OVER... at least you tried."
				print credits
			elif trainw == "2":
				print line
				print "In fright you bravely leap onto an unstable platform."
				print "The platform begins to crumble so you look around."
				print "you see:"
				print "1-a zip-line you could use"
				print "2-a rope you could swing from"
				print "3-another, equally rotten, platform"
				
				zip = raw_input('What do you choose?>>>')
				
				if zip == "1":
					print line
					print "You ride the zip-line over the lava pit and make it to the other side."
					print "You look ahead and see two doors:"
					print "1-a steal Door"
					print "2-an obsidian door"
					
					mdoors = raw_input('Whitch one do you enter?>>>')
					
					if mdoors == "1":
						print line
						print "You open the steal door and walk inside..."
						print "The room is dark at first."
						print "Is that a door on the other side?"
						print "1-check it out"
						print "2-this is to creepy... turn back!"
						
						aliandoor = raw_input('Should you check it out?>>>')
						
						if aliandoor == "1":
							print line
							print "You move closer to the door to check it out."
							print "The door flies open and you see an alian with a gun"
							print "in his hand. You turn to run for the opening."
							print "The steal door shuts itself and locks...."
							print "The lights come on and you see that you are in"
							print "Some kind of lab..."
							print "You are to remain there forever as an alian science experiment"
							print "GAME OVER!!! I guess curiosity killed the 'cat'..."
							print "or player in this case"
							print credits
						elif aliandoor == "2":
							print line
							print "Terrafied you run to the door."
							print "It slams shut and the lights come on."
							print "You turn around and see alian scientist coming into the room"
							print "You can never leave here"
							print "Game over... FEAR solves nothing."
							print credits
					
					elif mdoors == "2":
						print line
						print "You enter the obsidian door and it closed behind you"
						print "You walk down the long hall until you see a forked path."
						print "1-go right"
						print "2-go left"
						
						fork = raw_input('Both are to dark to see!>>>')
						
						if fork == "1":
							print line
							print "You turn right and walk forwhat feels like hours!"
							print "Up ahead you see a light."
							print "1-Go to the light!!!"
							print "2-turn back."
							
							light = raw_input('Is it a way out... or not>>>')
							
							if light == "1":
								print line
								print "You walk to the light only to realize that it is a trap."
								print "White, glowing tenticlals wrap around you and srush you!"
								print "Game Over! You went to the light at the end on the tunnel!"
								print credits
							elif light == "2":
								print line
								print "You try to turn back, but white, glowing tenticals reach out"
								print "of the light and crush you!"
								print "GAME OVER, you have been claimed by the light at the end of"
								print "the tunnel..."
								print credits
						elif fork == "2":
							print line
							print "you decide to go left."
							print "You see two HUGE doors"
							print "1-enter the black door"
							print "2-enter the white door"
							print "3-go back to the fork"
							
							Hdoor = raw_input('Look at the size of those things!>>>')
							
							if Hdoor == "3":
								print line
								print "You turn back and the grownd beneath your feet crumbles away..."
								print "Game Over... You have 'falled' me"
								print credits
							elif Hdoor == "1":
								print line
								print "The door locks behind you and you are trapped in the room"
								print "forever... to make things worse there is a giant bird that"
								print "thinks you are an egg!"
								print "GAME OVER, You'd be better off scrambled"
								print credits
							elif Hdoor == "2":
								print line
								print "The door locks behind you and you see a GIANT ghost"
								print "With a long floppy tongue"
								print "	'I Dare thee to beet meeeeeeeeee' it said"
								print "you see three weapons:"
								print "1-Grab the chain gun"
								print "2-Grab the Ray gun"
								print "3-Grab the golf-club"
								print "4-Insult"
								
								boss2 = raw_input('What to do... You are going to die... i Know it>>>')
								
								if boss2 == "1":
									print line
									print "You aim the chain gun and pull the trigger"
									print "you stare in terror as the bullets pass through the ghost"
									print "the ghost screams and you have a heart attack..."
									print "Game Over.................Freak"
									print credits
								elif boss2 == "2":
									print line
									print "you fire the ray gun and burn a hole in ghost"
									print "slowly the ghost vanishes into dust..."
									print "************"
									print "you win! I always knew you could! \nEnjoy your %s!" % reward
									print credits
								elif boss2 == "3":
									print line
									print "You swing the club at the ghost and pass inside of it."
									print "You sufocate and die..."
									print "GAME OVER.......GASP!!! I can't...brea..."
									print credits
								elif boss2 == "4":
									print line
									print "You say the most horible insult you know..."
									print "The ghost gets realy happy."
									print " 'Awwww you knowticed... thanks for the compliment.'"
									print "it said as it blushed. It then licked you and you"
									print "died from shock..."
									print "Game Over...JEARK...or 'sweety'... I'm confused..."
									print credits
							
				elif zip == "2":
					print line
					print "you grab the rope and swing with all your might."
					print "You land safely on a beam on the other side of the tunnel."
					print "You see:"
					print "1-a shoot that plunges downward"
					print "2-a ladder to clime upward"
					
					ladorsh = raw_input
					
					if ladorsh == "1":
						print line
						print "You slide down the shoot and get impailed by spikes..."
						print "GAME OVER. Didn't you ever play 'Shoots and Ladders'"
						print credits
					elif ladorsh == "2":
						print line
						print "you decide to climb the ladder."
						print "You realise to late that you are in a steam-vent"
						print "and the hot air gusts in you face... killing you."
						print "Game Over! I bet you are 'STEAMED'"
						print credits
					
				elif zip == "3":
					print line
					print "You leap to the other platform."
					print "As you land, you hear a sickening crack and you fall"
					print "to your demise..."
					print "Are you THAT stupid? GAME OVER"
					print credits
				
			elif trainw == "3":
				print line
				print "Stunned in fear... you stay put \nand the train plunges into lava and you die."
				print "Game Over, next time move your lazy butt!"
				print credits
elif door == "4":
	print line
	print "You darted out of the house screaming at the top of your lungs!"
	print "Game Over... a least you did not die..."
	print credits