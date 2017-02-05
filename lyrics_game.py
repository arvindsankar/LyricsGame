from PyLyrics import *
import string

# Clear the text file
open('lyrics.txt', 'w').close()

print "INSTRUCTIONS: Open a new terminal window in the same folder as this program."
print "Type this command into the new terminal window: 'tail -f lyrics.txt'"
print "This will be your output terminal."

raw_input("Type OK when you are ready.")

success = False
while not success:
	try:
		song = raw_input("Enter Song name:\n")
		artist = raw_input("Enter Artist name:\n")
		lyrics = str(PyLyrics.getLyrics(artist, song)).split()
		success = True
	except:
		print "The song or arist you entered was not found. Try again."

lyrics = [lyric for lyric in lyrics if lyric[0] != "("]
guess_lyrics = [''.join(c.lower() for c in s if c not in string.punctuation) for s in lyrics]

index = 0
passes = 0

exit = False

print "STARTING GAME *******"
print "Enter Lyrics: \n \n"
while index < len(lyrics) and not exit:
	word = raw_input()
	guess = ""
	
	for c in word:
		if c not in string.punctuation:
			guess += c.lower()

	if guess == guess_lyrics[index]:
		f = open('lyrics.txt', 'w')
		f.write(lyrics[index] + "\n")
		f.close()
		index += 1

	if guess == "pass":
		f = open('lyrics.txt', 'w')
		f.write(lyrics[index] + "\n")
		f.close()
		index += 1
		passes += 1

	if guess == "EXIT":
		exit = True

open('lyrics.txt', 'w').close()


