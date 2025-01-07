import sys
from flask import Flask
from tests.globalTests import allTests
app = Flask(__name__)

### Classic app just return Hello
@app.route("/")
def hello():
	return "<h1>hello<h1>"

### Main function launch the test app or the classic app
def main():
	# "-dev" flag send then start the test app with the allTests function
	if sys.argv[1] == "-dev":
		allTests()
	else: # Start the classic app
		app.run(host='0.0.0.0')

### Start the main function
if __name__ == "__main__":
	main()
