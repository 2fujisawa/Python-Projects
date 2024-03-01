#functions are out of classes
#methods are usually from classes 

with open("story.txt", 'r')as textfile: #open function opens the txt file as textfile 
    story = textfile.read() #using read function to read the file and set it to the variable story, 'read() is a built in function 
    print(story)

    words = []
    startofword = -1 #setting -1 here in order to indicate that the start of the word hasn't started

    startingchar = "<"
    endingchar = ">"


for index, char in enumerate(story): #enumerates(goes through one by one) through the entire loop and sets the charater to a index
    if char == startingchar:  #if a character is equal to the starting character then this initiates
        startofword = index #the startofword is set to the index wher ethe starting chracter was found

    if char == endingchar and startofword != -1: #if the endingcharacter is found in the char and the start of the word has started then this statement will initiate
        word = story[startofword: index + 1] #sets the variable word with the string created from the index 
        words.append(word)
        startofword = -1
        

print("\n",words)

