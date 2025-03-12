# Lexicographical Maximum substring of string
# Given a string determine the alphabetically maximum substring
# Solution Ref: https://www.geeksforgeeks.org/lexicographical-maximum-substring-string/


# example:
# str = "zmlasidnflasdflknonztynl"
# output => "ztynl" (ans is not "zmlasidnflasdflknonztynl")

# Python 3 program to find the
# lexicographically maximum substring.
def LexicographicalMaxString(str):
	
	# loop to find the max lexicographic 
	# substring in the substring array
	mx = ""
	for i in range(len(str)):
		mx = max(mx, str[i:])

	return mx
