# Function to find the length of the smallest substring

def smallestSubstring(S):
	res = 999999

	zero = 0
	one = 0
	two = 0

	zeroindex = 0
	oneindex = 0
	twoindex = 0
	for i in range(len(S)):
		if (S[i] == '0'):
			zero = 1
			zeroindex = i

		elif (S[i] == '1'):
			one = 1
			oneindex = i

		elif (S[i] == '2'):
			two = 1
			twoindex = i

		if (zero and one and two):
			res = min(res,
					max([zeroindex, oneindex, twoindex])
					- min([zeroindex, oneindex, twoindex]))
	if (res == 999999):
		return -1
	return res + 1

S = "01111"

print(smallestSubstring(S))

