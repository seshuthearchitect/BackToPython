n=input("\nEnter the bumnnies number")
def bunnyEars2(n):
	if(n<0):
		print "\nSory! Wrong input(negative values not allowed)"
	elif(n==0):
		return 0
	else:
		if(n%2==0):
			return 3+bunnyEars2(n-1)
		else:
			return 2+bunnyEars2(n-1)
print "\nThe number of ears are: ",bunnyEars2(n)

	