s=raw_input("\nEnter the string")
def countX(s):
	l=len(s)
	if(l==0):
		return 0
	elif(s[l-1]=='x'):		
		return 1+countX(s[:(l-1)])
	else:
		return countX(s[:(l-1)])
print "\nThe number of 'x's in the given string is: ",countX(s)
raw_input("\nPress enter to finish")