import sys
from table import Table
    
# take a list of all typed in arguments, apart of first one (i.e. ignore filename)
player_names_from_terminal = sys.argv[1:] 
assert type(player_names_from_terminal) == list

# use like this, in terminal (in noteable use New > Terminal)
# python main.py Pawel Jen Micheala Kim 
# this has to point to the file location so more likely it will be 
# python ./python-course-pg-notes-23/lectures/card_game_objects/main.py Pawel Jen Micheala Kim 

a_table = Table(player_names_from_terminal)
a_table.play_the_game()