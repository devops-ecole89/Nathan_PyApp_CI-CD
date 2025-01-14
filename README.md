# Python Application with CI/CD

This is a small application made in Python with Flask for a CI/CD projects. The objective of this app is to do small unit test to check the CI/CD integrations.

---
## Installation
Install tools and dependencies for the application utilisation :
1. `sudo apt update && apt updrade`
2. `sudo apt install -y python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools`
3. `pip install flask`

---
## How to use
### Classic launch
1. `python src/servapp.py`: start the app
2. Acces to the app : http://127.0.0.1:5000/

### Test launch
1. `python src/servapp.py -dev` : start the app in test mode. The output will be the cmd but you can out it in a file with `> log.txt`.

---
## Files
```shell
/
├── .github/                  # GitHub workflows
│   └── workflows/
│       ├── dev-push.yml      # Workflow trigger by dev branch push. If tests Ok then push to staging
│       └── main-push.yml     # Workflow trigger by main branch push. Update the public Docker image
├── src/
│   ├── servapp.py            # Main file of the app
│   └── tests/                # Tests directory
│       ├── __init.py__       # File to add path for import
│       ├── globalTests.py    # Global function that trigger all tests. Execute by 'servapp.py -dev'
│       └── firstTest.py      # First and only test. Execute by allTests() in globalTests.py
└── README.md                 # Project documentation
```

---
## Workflows
There is two workflows files. The first one, wich is trigger on dev push, realize two tasks:
1. Process the automatics tests and merge to the staging branch if it's successfull.
2. Create a pull request between staging and main to merge into main.
The second workflow is for an automatic push of a Docker image on Docker hub. It is trigger by push on main branch but the Docker Hub connexion doesn't work...

---
## Contributors

Nathan: Master mind :)
