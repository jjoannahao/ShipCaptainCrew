# CSE3120-Project: Ship, Captain, Crew!

## Game Rules
Two players compete to find the most loot: gold coins! Each player has 5 dice (represented by 5 numbers) that can be rolled, and each player has up to three rolls of these dice to find loot. 

However, players must first find their ship, their Captain, and their crew before any loot can be collected. If the player cannot find all the needed members in the correct order by the end of three rolls, they score no points.

The ship is represented by the number 6, the captain is represented by the number 5, and the crew is represented by the number 4. Players must find the necessary numbers in this order:
1. Ship (6)
2. Captain (5)
3. Crew (4)

After they are all found, the remaining numbers rolled are totaled up as the coins (loot) found by the player!

### Example of a Player Turn
Roll 1:
1, 3, 3, 4, __6__ → Ship is found! (6 is held)

Roll 2:
__4__, 4, __5__, 1, __6__ → Captain is found! Crew is found! (5 and 4 is held)
Loot: 5 gold coins! Keep coins? Y/n → N

Roll 3:
__4__, 2, __5__, 2, __6__
Loot: 4 gold coins! Player scores 4 points!

## How to Use The Program
Run the ```main.py``` file!

## Extra Feature
Leaderboard of winning scores (SQLite3 Database)
