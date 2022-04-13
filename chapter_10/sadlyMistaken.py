##################
# David Wells    #
# Sadly Mistaken #
#  4/13/2022     #
##################

song = ('/Users/david.wells/Desktop/pythonCrashCourse/chapter_10/SadlyMistaken.txt')

with open(song) as s:
	lyrics = s.readlines()

pi_string = ''
for line in lyrics:
	pi_string += line

print(pi_string)