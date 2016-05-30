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
			if (d[char]%2 == 0 and d[char] > maxcount):
				maxcount = d[char]
		else:
			d[char] = 1
	print maxcount
	for item in d:
		if d[item] == maxcount and maxcount >1:
			chars.append(item)
			break
	return chars;


def preCreatePalindrome(input, l = "", r = "", pos = 0, method_values = None):
	if  isPalindrome(input) or len(input) == 1:
		pal = l + input + r[::-1]
		print "Resultado ->" + pal
		return pal
	else:
		left = input[:len(input)/2]
		right = input[::-1][:len(input)/2]

		if len(input)%2 != 0:
			mid = input[len(input)/2]
			if left[0] == right[0]:
				return preCreatePalindrome(left[1:]+mid+right[1:], l + left[0], r + right[0], 1 + pos)
			else:
				print "Cambio pos " + str(pos) + " por " + right[0] + " -> " + l + right[0] + left[1:] + mid + right[1:] + right[0] + r
				return preCreatePalindrome(left[1:]+mid+right[1:], l + right[0], r + right[0], 1 + pos)

def createPalindrome(input):
	print "Cadena inical -> " + input
	preCreatePalindrome(input)

def MakePalindrome(input):
	input = "program"
	repeated = repeatedChar(input)
	if isPalindrome(input) or len(input) == 0:
		return input;
	#  If an input has repeated characters,
	#  use them to reduce the number of insertions
	elif len(repeated) > 0:
		shortestResult = "";
		for ch in repeated: #"program" -> { 'r' }
			# find boundaries
			ch = 'r'
			chpos = find (input, ch)
			iLeft = chpos[0] # "program" -> 1
			iRight = chpos[len(chpos)-1] # "program" -> 4
			# make a palindrome of the inside chars
			inside = input[iLeft + 1 : iRight] # "program" -> "og"

			insidePal = MakePalindrome(inside) # "og" -> "ogo"

			right = input[iRight+1:] # "program" -> "am"
			rightRev = right[::-1] # "program" -> "ma"
			left = input[:iLeft] # "program" -> "p"
			leftRev = left[::-1] # "p" -> "p"

			# Shave off extra chars in rightRev and leftRev
			#   When input = "message", this loop converts "meegassageem" to "megassagem",
			#     ("ee" to "e"), as long as the extra 'e' is an inserted char
			while len(left) > 0 and len(rightRev) > 0 and left[left.Length - 1] == rightRev[0]:
				rightRev = rightRev.Substring(1);
				leftRev = leftRev.Substring(1);

			# piece together the result
			result = left + rightRev + ch + insidePal + ch + right + leftRev;

			# find the shortest result for inputs that have multiple repeated characters
			if shortestResult == "" or len(result) < len(shortestResult):
				shortestResult = result;
		return shortestResult;
	else:
		# For inputs that have no repeated characters,
		# just mirror the characters using the last character as the pivot.
		for i in range (2,len(input)):
			input += input[len(input)-2-i]
		return input;


repeatedChar("stacckecxchange")
input = "arsas"
createPalindrome("arsas")
