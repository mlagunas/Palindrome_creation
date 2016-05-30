# solution with dynamic programming
def dynamic_programming(n_steps, method_values = None):

	if n_steps < 1: return 0
	elif n_steps == 1: return 1
	elif n_steps == 2: return 2
	else:
		# case where method_value list has not been initialized
		if(method_values == None):
			method_values = [-1] * n_steps

		# case when this method call has not been made
		if(method_values[n_steps-1] == -1):
			method_values[n_steps-1] = dynamic_programming(n_steps-1, method_values);
		if(method_values[n_steps-2] == -1):
			method_values[n_steps-2] = dynamic_programming(n_steps-2, method_values);
		print method_values, n_steps
		return method_values[n_steps-1] + method_values[n_steps-2];

dynamic_programming(6)
DEBUG = False

def find(lst, char):
	t = []
	for i,c in enumerate(lst):
		if char==c: t.append(i)
	return t

def isPalindrome(input):
	return input.find(input[::-1]) == 0

def repeatedChar(input):
	chars = []
	maxcount = 1
	d = {}
	for char in input:
		if char in d:
			d[char] += 1
			if (d[char]%2 == 0 and d[char] > maxcount):
				maxcount = d[char]
		else:
			d[char] = 1
	for item in d:
		if d[item] == maxcount and maxcount >1:
			chars.append(item)

	return chars;

def makeIt(strL, strR, mid_chars, offsetL="", offsetR="", res = "", pos = 1):
	if len(strR) > 0 and len(strL) > 0:
		if len(strL) > len(strR):
			if strL[0] == strR[0]: #Equal value, add to the result and go ahead
				return makeIt(strL[1:], strR[1:], mid_chars, offsetL, offsetR, res + strL[0], pos+1)
			else:
				res += strL[0]
				string =  offsetL + strL + mid_chars + (res + strR)[::-1] + offsetR
				print "Insert '" +strL[0]+ "' on pos " + str(pos+len(mid_chars)) +" -- "+ string
				return makeIt(strL[1:], strR, mid_chars, offsetL, offsetR, res, pos +1)
		elif len(strR) > len(strL):
			if strL[0] == strR[0]:
				return makeIt(strL[1:], strR[1:], mid_chars, offsetL, offsetR, res + strL[0], pos+1)
			else:
				res += strR[0]
				string = offsetL + res + strL + mid_chars + (res + strR[1:])[::-1] + offsetR
				print "Insert '" +strR[0]+ "' on pos " + str(len(offsetL)+pos)  +" -- "+ string
				return makeIt(strL, strR[1:], mid_chars, offsetL, offsetR, res, pos +1)
		if strL[0] != strR[0]:
			string = offsetL + res + strR[0] + strL[1:] + mid_chars + (res + strR)[::-1] + offsetR
			print "Change pos '" +str(len(offsetL)+pos)+ "' for " +strR[0]+ " -- " + string
			return makeIt(strL[1:], strR[1:], mid_chars, offsetL, offsetR, res + strR[0], pos +1)
		if strL[0] == strR[0]:
			return makeIt(strL[1:], strR[1:], mid_chars, offsetL, offsetR, res + strL[0], pos+1)
	else:
		if len(strL) > len(strR):
			res += strL[0]
			string = offsetL + strL + mid_chars + (res + strR)[::-1] + offsetR
			print "Insert '" +strL[0]+ "' on pos " + str(pos+len(mid_chars)) +" -- "+ string
			return makeIt(strL[1:], strR, mid_chars, offsetL, offsetR, res, pos +1)
		elif len(strR) > len(strL):
			res += strR[0]
			string = offsetL + res + strL + mid_chars + (res + strR[1:])[::-1] + offsetR
			print "Insert '" +strR[0]+ "' on pos " + str(len(offsetL)+pos)  +" -- "+ string
			return makeIt(strL, strR[1:], mid_chars, offsetL, offsetR, res, pos +1)
		else:
			return res + mid_chars + res[::-1]

def preMake(input, offsetL="", offsetR=""):
	repeated = repeatedChar(input)

	if isPalindrome(input) or len(input) == 0:
		return input;
		#  If an input has repeated characters,
	#  use them to reduce the number of insertions
	elif len(repeated) > 0:
		shortestResult = ""
		for ch in repeated: #"program" -> { 'r' }
			# find boundaries
			chpos = find(input, ch)
			iLeft = chpos[0] # "program" -> 1
			iRight = chpos[len(chpos)-1] # "program" -> 4

			right = input[iRight+1:] # "program" -> "am"
			rightRev = right[::-1] # "program" -> "ma"

			left = input[:iLeft] # "program" -> "p"
			leftRev = left[::-1] # "p" -> "p"

			# make a palindrome of the inside chars
			inside = input[iLeft + 1 : iRight] # "program" -> "og"
			insidePal = preMake(inside, left+ch, ch+right) # "og" -> "ogo"

			result = makeIt(left, right, ch+insidePal+ch, offsetL, offsetR)

			# Shave off extra chars in rightRev and leftRev
			#   When input = "message", this loop converts "meegassageem" to "megassagem",
			#     ("ee" to "e"), as long as the extra 'e' is an inserted char
			# while len(left) > 0 and len(rightRev) > 0 and left[len(left)- 1] == rightRev[0]:
			# 	rightRev = rightRev[1:]
			# 	leftRev = leftRev[1:]
			#
			# if DEBUG :
			# 	print "righ " + right
 			# 	print "left " + left
			# 	print "ch " + ch
			# 	print "righR " + rightRev
 			# 	print "inside pal " + insidePal
			# 	print "leftRev "+ leftRev

			# piece together the result
			# result = left + rightRev + ch + insidePal + ch + right + leftRev

			# find the shortest result for inputs that have multiple repeated characters
			if shortestResult == "" or len(result) < len(shortestResult):
				shortestResult = result
		return shortestResult
	else:
		# For inputs that have no repeated characters,
		# just mirror the characters using the last character as the pivot.
		# for i in range(len(input)-2,-1, -1):
		# 	print "Add " + str(input[i])+ " in position " +str(i)+ " -> " + str(input + input[i])
		# 	input += input[i]
		if len(input)%2 == 0:
			input = makeIt(input[:len(input)/2], input[len(input)/2], "", offsetL, offsetR)
		else:
			input = makeIt(input[:len(input)/2], input[len(input)/2+1:], input[len(input)/2], offsetL, offsetR)
		return input

def MakePalindrome(input):
	print "Input -- " + input
	palindrome = preMake(input)
	print "Result -- " + palindrome

MakePalindrome("program")
