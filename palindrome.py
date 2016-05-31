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
			if (d[char] > maxcount):
				maxcount = d[char]
		else:
			d[char] = 1
	for item in d:
		if d[item] == maxcount and maxcount >1:
			chars.append(item)

	return chars;

def makeItDin(strL, strR, method_values = None):
	if strL[0] != strR[0]:
		return strL[0]
	elif len(strL) > len(strR):
		return strL[0]:

	else:
		if len(strL)>len(strR) in method_values:
			method_values[strL-1+strR] = makeItDin(strL[1:], strR, method_values)

def makeIt(strL, strR, mid_chars, offsetL="", offsetR="", res = "", pos = 1, comments = 0):
	if len(strR) > 0 and len(strL) > 0:
		if len(strL) > len(strR):
			if strL[0] == strR[0]: #Equal value, add to the result and go ahead
				return makeIt(strL[1:], strR[1:], mid_chars, offsetL, offsetR, res + strL[0], pos+1, comments)
			else:
				res += strL[0]
				string =  offsetL + strL + mid_chars + (res + strR)[::-1] + offsetR
				comment = "Insert '" +strL[0]+ "' on pos " + str(pos+len(mid_chars)+len(offsetL)) +" -- "+ string
				return comment + '\n' +makeIt(strL[1:], strR, mid_chars, offsetL, offsetR, res, pos +1, comments+1)
		elif len(strR) > len(strL):
			if strL[0] == strR[0]:
				return makeIt(strL[1:], strR[1:], mid_chars, offsetL, offsetR, res + strL[0], pos+1, comments)
			else:
				res += strR[0]
				string = offsetL + res + strL + mid_chars + (res + strR[1:])[::-1] + offsetR
				comment = "Insert '" +strR[0]+ "' on pos " + str(len(offsetL)+pos)  +" -- "+ string
				return comment + '\n' + makeIt(strL, strR[1:], mid_chars, offsetL, offsetR, res, pos +1, comments+1)
		if strL[0] != strR[0]:
			string = offsetL + res + strR[0] + strL[1:] + mid_chars + (res + strR)[::-1] + offsetR
			comment = "Change pos '" +str(len(offsetL)+pos)+ "' for " +strR[0]+ " -- " + string
			return comment + '\n' + makeIt(strL[1:], strR[1:], mid_chars, offsetL, offsetR, res + strR[0], pos +1, comments+1)
		if strL[0] == strR[0]:
			return makeIt(strL[1:], strR[1:], mid_chars, offsetL, offsetR, res + strL[0], pos+1, comments)
	else:
		if len(strL) > len(strR):
			res += strL[0]
			string = offsetL + strL + mid_chars + (res + strR)[::-1] + offsetR
			comment = "Insert '" +strL[0]+ "' on pos " + str(pos+len(mid_chars)+len(offsetL)) +" -- "+ string
			return comment + '\n' + makeIt(strL[1:], strR, mid_chars, offsetL, offsetR, res, pos +1, comments+1)
		elif len(strR) > len(strL):
			res += strR[0]
			string = offsetL + res + strL + mid_chars + (res + strR[1:])[::-1] + offsetR
			comment = "Insert '" +strR[0]+ "' on pos " + str(len(offsetL)+pos)  +" -- "+ string
			return comment + '\n' + makeIt(strL, strR[1:], mid_chars, offsetL, offsetR, res, pos +1, comments+1)
		else:
			return "|" + str(comments) +"|"+ res + mid_chars + res[::-1]

def preMake(input, offsetL="", offsetR=""):
	repeated = repeatedChar(input)
	if isPalindrome(input) or len(input) == 0:
		return "",0,input;
		#  If an input has repeated characters,
	#  use them to reduce the number of insertions
	elif len(repeated) > 0:

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
			x = preMake(inside, left+ch, ch+right)
			t, n, insidePal = x # "og" -> "ogo"

			text, number, result = makeIt(left, right, ch+insidePal+ch, offsetL, offsetR).split("|")
			number = int(number)
			text = t + text
			number += int(n)

		return text, number, result
	else:
		if len(input)%2 == 0:
			text, number, input = makeIt(input[:len(input)/2], input[len(input)/2], "", offsetL, offsetR).split("|")
		else:
			text, number, input = makeIt(input[:len(input)/2], input[len(input)/2+1:], input[len(input)/2], offsetL, offsetR).split("|")
		return text, number, input

def MakePalindrome(input):
	text = preMake(input)
	print "Minimum number -- " + str(text[1])
	print "Input text -- " + input
	print text[0]
	print "Result -- " + text[2]

makeIt("st", "asdfgh","")
makeIt("st", "asdfgh","").split("|")[0]
makeIt("st", "asdfgh","").split("|")[1]
makeIt("st", "asdfgh","").split("|")[2]
a,b,c = (1,2,3)
str(preMake("holo"))
MakePalindrome("holo")
MakePalindrome("stackexchange")




















makeIt("asdasd","fgh","")
MakePalindrome("stackexchange")
