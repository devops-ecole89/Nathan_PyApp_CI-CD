from tests.firstTest import firstTest

### Main function that performs the test battery
def allTests():
	# Init Number Errors Found variable
	nbrErrors = 0

	# Performs the first test
	if firstTest("Nathan") != True:
		nbrErrors+=1

	# Check if there is any Errors found
	if nbrErrors == 0:
		print ("SUCCESS")
	else:
		print ("There is ", nbrErrors, "Errors")
