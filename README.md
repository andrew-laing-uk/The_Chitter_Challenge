# The Chitter Challenge Solution

## Setup

```shell
# Clone the repository to your local machine
; git clone git@github.com:andrew-laing-uk/The_Chitter_Challenge.git he_Chitter_Challenge he_Chitter_Challenge

# Or, if you don't have SSH keys set up
; git clone https://github.com/andrew-laing-uk/The_Chitter_Challenge.git he_Chitter_Challenge

# Enter the directory
; cd The_Chitter_Challenge

# Set up the virtual environment
; python -m venv html-application-starter-venv

# Activate the virtual environment
; source html-application-starter-venv/bin/activate 

# Install dependencies
(html-application-starter-venv); pip install -r requirements.txt
# Read below if you see an error with `python_full_version`

# Create a test and development database
(html-application-starter-venv); createdb The_Chitter_Challenge
(html-application-starter-venv); createdb The_Chitter_Challenge_test

# Open lib/database_connection.py and change the database name to YOUR_PROJECT_NAME
(html-application-starter-venv); open lib/database_connection.py

# Seed the development database
(html-application-starter-venv); python seed_dev_database.py

# Run the tests (with extra logging)
(html-application-starter-venv); pytest -sv

# Run the app
(html-application-starter-venv); python app.py
# Now visit http://localhost:5001/emoji in your browser
```
