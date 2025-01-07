from firstTest import firstTest

### Main function that performs the test battery
def allTests():
	# Init Number Errors Found variable
	var nbrErrors = 0

	# Performs the first test
	if firtTest("Nathan") != True:
		nbrErrors++

	# Check if there is any Errors found
	if nbrErrors == 0:
		print ("SUCCESS")
	else:
		print ("There is ", nbrErrors, "Errors")
