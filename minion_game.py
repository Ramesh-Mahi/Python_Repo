# Game Rules

# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string .

# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

# For better understanding, see the image below:

# banana.png

# Your task is to determine the winner of the game and their score.

# Function Description

# Complete the minion_game in the editor below.

# minion_game has the following parameters:

# string string: the string to analyze
# Prints

# string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
# Input Format

# A single line of input containing the string .
# Note: The string  will contain only uppercase letters: .

# Constraints



# Sample Input

# BANANA
# Sample Output

# Stuart 12




def minion_game(string):
    n = len(string)
    #formula to calculate the total substring present in the string
    comp = (n*(n+1))/2
    count_k = 0 #kevin score
    count_s = 0 #straut score
    count_k = sum([len(string[i::]) for i in range(len(string)) 
                                    if string[i] in 'AEIOU'])
                #getting the substring by getting the length of each sub string and adds it up
    count_s = comp-count_k
    
    if count_k == count_s:
        print("Draw")
    elif count_k > count_s:
        print("Kevin", int(count_k))
    else:
        print("Stuart", int(count_s))
        
if __name__ == '__main__':
    s = input()
    minion_game(s)

