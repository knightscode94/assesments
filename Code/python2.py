# INSTRUCTIONS

# In case it is not clear, the Question appears first, then examples, then any hints and finally the function that you need to complete appears underneath:

# <QUESTION>

# <EXAMPLES>

# <HINT>

# You are allowed access to the internet for this assessment, you can also use the DOCUMENTATION that comes bundled with your Python installation.  You should already be comfortable accessing this documentation, but to summarise:

# Access Python from you CLI by typing python or python3

# Type help() or for example help(str) on your Python terminal

# To leave a Python terminal type exit()

# <QUESTION 1>

# Given a string, return a string where for every char in the original string, there are three chars.

# <EXAMPLES>

# one("The") → "TTThhheee"
# one("AAbb") → "AAAAAAbbbbbb"
# one("Hi-There") → "HHHiii---TTThhheeerrreee"

# <HINT>
# How does a for loop iterate through a string?

def one(input):
    input = list(input)
    output = [item for item in input for i in range(3)]

    return ''.join(output)

    # <QUESTION 2>

    #  Write a function which returns the boolean True if the input is only divisible by one and itself.

    # The function should return the boolean False if not.

    # <EXAMPLES>

    # two(3) → True
    # two(8) → False

    # <HINT>
    # What operator will give you the remainder?
    # Use your CLI to access the Python documentation and get help manipulating strings - help(range).


def two(input):
		if input > 1:
			for i in range(2, input//2):
				if (input % i) == 0:
					return False
					break
			else:
				return True
		else:
			return False

# <QUESTION 3>

# Write a function which takes an integer input, a, and returns the sum a+aa+aaa+aaaa.

# So if 2 was the input, the function should return 2+22+222+2222 which is 2468.

# <EXAMPLES>

# three(9) → 11106
# three(5) → 6170

# <HINT>
# What happens if you multiply a string by a number?


def three(a):
	a=a
	aa=(a*10)+a
	aaa=(a*100)+aa
	aaaa=(a*1000)+aaa
	return a+aa+aaa+aaaa


    # <QUESTION 4>

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


def four(input1, input2):
	output = [] 
	for x in range(max(len(input1),len(input2))):
		output.append(input1[x] if x < len(input1) else '')
		output.append(input2[x] if x < len(input2) else '')
	return ''.join(output)


    # <QUESTION 5>

    # Write a function to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

    # <EXAMPLES>

    # five() → [100,102,122,198,200]
    # five() → [108,104,106,188,200]
    # five() → [154,102,132,178,164]

    # <HINT>
    # There is a module which can be used to generate random numbers, this module is called random.
    # The random module contains a function called randint.


def five():
    return []

    # <QUESTION 6>

    # Given a string, return the boolean True if it ends in "py", and False if not.

    # Ignore Case.

    # For Example:

    # six("ilovepy") → True
    # six("welovepy") → True
    # six("welovepyforreal") → False
    # six("pyiscool") → False

    # <HINT>
    # There are no hints for this question.


def six(input):
	input = input.islower()
	if input.endswith("py"):
		return True
	else:
		return False

    # <QUESTION 7>

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
	first = [a,b,c]
	second = sorted(first)
	if second[0] - second[1] == second[1] - second[2]:
		return True
	else:
		return False


    # <QUESTION 8>

    # Given a string and an integer, n, return a string that removes n letters from the 'middle' of the string.

    # The string length will be at least n, and be odd when the length of the input is odd, so there will always be a 'middle'.

    # <EXAMPLES>

    # eight("Hello", 3) → "Ho"
    # eight("Chocolate", 3) → "Choate"
    # eight("Chocolate", 1) → "Choclate"

    # <HINT>
    # Use the cli to access the documentation help(str.replace)


def eight(input, a):
	middle = len(input)%2
	return input.replace(middle, a)

pass

    # <QUESTION 9>

    # Given two string inputs, if one can be made from the other return the boolean True, if not return the boolean False.

    # <EXAMPLES>

    # nine("god", "dog") → True
    # nine("tree", "tiredest") → True
    # nine("cat", "dog") → False
    # nine("tripping", "gin") → True

    # <HINT>
    # There are no hints for this question.


def nine(string1, string2):
	len1 = len(string1)
	len2 = len(string2)
	if (len1 != len2):
		return False
	prev = -1
	current = -1
	count = 0
	i = 0
	while i < len1:
		if (string1[i] != string2[i] ):
			count = count + 1
			if (count > 2):
				return False
			prev = current 
			current = i
		i = i + 1
	return (count == 2 and string1[prev] == string2[current] 
               and string1[current] == string2[prev])

    # <QUESTION 10>

    # Write a function which takes 2 integers greater than 0, X,Y as input and generates a 2-dimensional array.

    # The element value in the i-th row and j-th column of the array should be i*j.

    # <EXAMPLES>

    # ten(3,2) → [[0,0,0],[0,1,2]]
    # ten(2,1) → [[0,0]]
    # ten(3,4) → [[0,0,0],[0,1,2],[0,2,4],[0,3,6]]

    # <HINT>
    # Think about nesting for loops.


def ten(X, Y):
	multi_list = [[0 for y in range(Y)] for x in range(X)]
	for x in range(X):
		for y in range(Y):
			multi_list[x][y]= x*y
	return multi_list
