# selfie-less-act

Cloud Computing Project for 6th Sem

# Follow these instructions to set up.

### Strongly recommend to use a virtual environment and Visual Studio Code as the editor.

## If using a virtual environment
* `python3 -m venv env` # To create a virtual env.
* `cd env && source bin/activate` # To activate venv. Do this everytime you start to work.

## Clone from gitlab.

* `git clone 'your_path'`
* `cd selfie-less-act`
* Create a new branch using `git checkout -b 'branch_name'`

### * Do not work on `master` branch.

## Initialise the repository
* `pip3 install -r requirements.txt`
* `python manage.py createsuperuser`

## To run the django project
* `python3 manage.py runserver`

## Initialise the db
* When changes to the database schema are made (the models), run `python manage.py makemigrations` and then  	`python manage.py migrate` from the repo directory in order to make the corresponding changes in the schema to  your local database.
* Mostly not needed at the moment as we are using sqlite3 rn

## Pull before making any new commits
* Pull using ``git pull origin `branch_name` ``

## To commit your changes
* `git add .`
* `git commit -m "Message"`
* `git push origin 'branch_name'`