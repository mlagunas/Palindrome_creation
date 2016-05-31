import sys

def usage():
	print "USAGE"
	print "python palindrome.py text"
	print "	 text is the list of characters we will transform into a palindrome"

def isPalindrome(input):
 	return str(input) == str(input)[::-1]

# A Dynamic Programming based Python program for LPS problem
# returns the length of the longest palindromic subsequence (LPS) in
# the given input
def lps(input):
	# initialize with 1 for length 1
	n = len(word) + 1
	num_chars = [[0]*n,[1]*(n-1)] + [[None]*(n-i) for i in range(2, n)]

	for i in range(2, n): #word length from 2 to len(word)
		for j in range(n - i):
			if word[j] == word[j + i - 1]:
				num_chars[i][j] = num_chars[i-2][j+1] + 2
			else:
				a = num_chars[i-1][j]
				b = num_chars[i-1][j+1]
				if a > b : num_chars[i][j] = a
				else: num_chars[i][j] = b

	# build the solution
	palindrome = []
	mirror = ''
	j = 0
	for i in range(n-1, 0, -1):
		if word[j] == word[j + i - 1]:
			if i == 1:
				mirror = word[j]
			else:
				palindrome.append(word[j])
				if i == 2:
					break
			j += 1
		elif num_chars[i-1][j] < num_chars[i-1][j+1]:
			j += 1
	return num_chars[-1][0], ''.join(palindrome) + mirror + ''.join(reversed(palindrome))

# It generates a new palindrome from a given input. It uses the
# logest palindromic subsequence to calculate it. The algorithm
# reduces the input until it has the same form as the lps. It prints
# every step it takes to generate it
def makePalindrome(input, before = "", ops = 0):
	if isPalindrome(input):
		print "Number of operations -- 0")
		print "Input string -- " +input
		print "Final result -- " + input
	elif len(input)%2==0:
		print "Input string -- " +input
		input = input[len(input)-1] + input
		makePalindrome(input,  "Add " + input[len(input)-1] + " in pos " + str(0) + " -- "+ input, ops+1)
	else:
		lpsNum, lpsRes = lps(input)
		print "Number of operations -- " +str(len(input) - lpsNum + ops)
		if before != "":
			print before
		else:
			print "Input string -- " +input
		j = 0
		i = 0
		for c in input:
			if j != len(lpsRes) and c == lpsRes[j]:
				j+= 1
				i+= 1
			else:
				if len(input)-i<=len(lpsRes)-j:
					input = input[:i] +lpsRes[j]+ input[i+1:]
					print "Change pos " + str(i+1) + " for "+lpsRes[j]+" -- "+ input
					i+=1
					j+=1
				else:
					input = input[:i] + input[i+1:]
					print "Delete pos " + str(i+1) + " -- "+ input
		print "Final result: " + input
		return input

if len(sys.argv) == 2 :
	text = sys.argv[1]
	makePalindrome(text)
else:
	usage()
