import random

# INSTRUCTIONS

# In case it is not clear, the Question appears first, then examples, then any hints and finally the function that you need to complete appears underneath:

# <QUESTION>

# <EXAMPLES>

# <HINT>

# You are NOT allowed access to the internet for this assessment, instead you should use the DOCUMENTATION that comes bundled with your Python installation.  You should already be comfortable accessing this documentation, but to summarise:

# Access Python from you CLI

# Type help() or for example help(str)

#===================================================================================================================================================

# <QUESTION 1> - Done

# Given a string, return a string where for every char in the original string, there are three chars.

# <EXAMPLES>

# one("The") → "TTThhheee"
# one("AAbb") → "AAAAAAbbbbbb"
# one("Hi-There") → "HHHiii---TTThhheeerrreee"

# <HINT>
# How does a for loop iterate through a string?


def one(string):
    charList = []

    for char in string:                 #Iterates through each character
        for i in range(3):              #Iterates 3 times per character
            charList.append(char)
    
    outputString = "".join(charList)    #Makes the list into one string

    return outputString



#===================================================================================================================================================

    # <QUESTION 2> - Done

    #  Write a function which returns the boolean True if the input is only divisible by one and itself.

    # The function should return the boolean False if not.

    # <EXAMPLES>

    # two(3) → True
    # two(8) → False

    # <HINT>
    # What operator will give you the remainder?
    # Use your CLI to access the Python documentation and get help manipulating strings - help(range).


def two(num):
    # return
    for i in range(1, num+1):
        if i == num or i == 1:
            continue
        else:
            if num % i == 0:
                return False
    
    return True


#===================================================================================================================================================

    # <QUESTION 3> - Done

    # Write a function which takes an integer input, a, and returns the sum a+aa+aaa+aaaa.

    # So if 2 was the input, the function should return 2+22+222+2222 which is 2468.

    # <EXAMPLES>

    # three(9) → 11106
    # three(5) → 6170

    # <HINT>
    # What happens if you multiply a string by a number?


def three(a):
    sum = 0

    for i in range(1, 5):
        stringNum = str(a)
        newNum = int(stringNum * i)
        sum = sum + newNum

    return sum


#===================================================================================================================================================

    # <QUESTION 4> - Done

    # Given two Strings of equal length, 'merge' them into one String.

    # Do this by 'zipping' the Strings together.

    # Start with the first char of the first String.
    # Then add the first char from the second String.
    # Then add the second char from the first String.
    # And so on.

    # Maintain case.

    # You will not encounter whitespace.

    # <EXAMPLES>

    # four("String","Fridge") → "SFtrriidngge"
    # four("Dog","Cat") → "DCoagt"
    # four("True","Tree") → "TTrrueee"
    # four("return","letter") → "rleettutrenr"

    # <HINT>
    # Use your CLI to access the Python documentation and get help manipulating strings - help(list.insert).
    # How would you seperate a string into characters?


def four(string1, string2):
    zipped = zip(string1, string2)
    newList = []

    for aTuple in zipped:
        newList.append("".join(aTuple))

    newString = "".join(newList)

    return newString


#===================================================================================================================================================

    # <QUESTION 5> - Done

    # Write a function to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

    # <EXAMPLES>

    # five() → [100,102,122,198,200]
    # five() → [108,104,106,188,200]
    # five() → [154,102,132,178,164]

    # <HINT>
    # There is a module which can be used to generate random numbers, this module is called random.
    # The random module contains a function called randint.


def five():
    finalList = []

    while(len(finalList) != 5):
        randomNum = random.randint(100, 200)

        if randomNum % 2 == 0:
            finalList.append(randomNum)

    return finalList


#===================================================================================================================================================

    # <QUESTION 6> - Done

    # Given a string, return the boolean True if it ends in "py", and False if not.

    # Ignore Case.

    # For Example:

    # six("ilovepy") → True
    # six("welovepy") → True
    # six("welovepyforreal") → False
    # six("pyiscool") → False

    # <HINT>
    # There are no hints for this question.

def six(string):
    stringLowered = string.lower()

    if stringLowered.endswith("py"):
        return True
    return False

#===================================================================================================================================================


    # <QUESTION 7> - Done

    # Given three ints, a b c, one of them is small, one is medium and one is large.

    # Return the boolean True if the three values are evenly spaced, so the
    # difference between small and medium is the same as the difference between
    # medium and large.

    # Do not assume the ints will come to you in a reasonable order.

    # <EXAMPLES>

    # seven(2, 4, 6) → True
    # seven(4, 6, 2) → True
    # seven(4, 6, 3) → False
    # seven(4, 60, 9) → False

    # <HINT>
    # There is a function for lists called sort.
    # Use the cli to access the documentation help(list.sort)


def seven(a, b, c):
    numList = []
    numList.append(a)
    numList.append(b)
    numList.append(c)
    numList.sort()

    if (numList[2] - numList[1]) == (numList[1] - numList[0]):
        return True

    return False


#===================================================================================================================================================

    # <QUESTION 8> - Done

    # Given a string and an integer, n, return a string that removes n letters from the 'middle' of the string.

    # The string length will be at least n, and be odd when the length of the input is odd, so there will always be a 'middle'.

    # <EXAMPLES>

    # eight("Hello", 3) → "Ho"
    # eight("Chocolate", 3) → "Choate"
    # eight("Chocolate", 1) → "Choclate"

    # <HINT>
    # Use the cli to access the documentation help(str.replace)


def eight(string, num):
    middleIndex = (len(string)/2)
    amountToRemovePerSide = int((num-1) / 2)

    startWord = string[ : int(middleIndex-amountToRemovePerSide)]
    endWord = string[int(middleIndex+amountToRemovePerSide+1) : ]
    finalWord = startWord + endWord

    return finalWord


#===================================================================================================================================================

    # <QUESTION 9> - Done

    # Given two string inputs, if one can be made from the other return the boolean True, if not return the boolean False.

    # <EXAMPLES>

    # nine("god", "dog") → True
    # nine("tree", "tiredest") → True
    # nine("cat", "dog") → False
    # nine("tripping", "gin") → True

    # <HINT>
    # There are no hints for this question.


def nine(string1, string2):
    # make sure string1 is the shortest of the two
    
    if len(string1) > len(string2):
        temp = string2
        string2 = string1
        string1 = temp

    string2CharList = list(string2)
    counter = 0

    for char in string1:
        if char in string2CharList:
            string2CharList.remove(char)
            counter = counter + 1

    if counter == len(string1):
        return True

    return False


#===================================================================================================================================================

    # <QUESTION 10> - Done

    # Write a function which takes 2 integers greater than 0, X,Y as input and generates a 2-dimensional array.

    # The element value in the i-th row and j-th column of the array should be i*j.

    # <EXAMPLES>

    # ten(3,2) → [[0,0,0],[0,1,2]]
    # ten(2,1) → [[0,0]]
    # ten(3,4) → [[0,0,0],[0,1,2],[0,2,4],[0,3,6]]

    # <HINT>
    # Think about nesting for loops.


def ten(a, b):
    outerList = []

    for i in range(b):
        innerList = []
        for j in range(a):
            innerList.append(i*j)

        outerList.append(innerList)
    return outerList