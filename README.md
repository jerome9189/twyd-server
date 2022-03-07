# twyd-server

## Setup:

```
# create a virtual environment
python3 -m venv .venv

# activate the virtual environment
source .venv/bin/activate

# install packages (could take a while, only need to do this once)
pip3 install -r requirements.txt

# Some django DB stuff
python3 manage.py makemigrations
python3 manage.py migrate

# create a super user for editing and inspecting the db
python3 manage.py createsuperuser

# more stuff
python3 manage.py migrate --run-syncdb

# run server
python3 manage.py runserver
```

You can visit the `/admin` location to manually edit the database, add users, etc. The current useful endpoints are:

- `GET /users/`: gets list of users (including aliases, image url, etc.)
- `GET /room/`: gets statuses of users in room
- `GET /preferences/<user_name>`: gets data sharing preferences of a particualr user
- `PUT /status/<user_name>`: updates status of a particular user `{current_tab, keyboard_activity}`
- `PUT /preferences/<user_name>`: updates data sharing preferences of a particular user `{show_current_tab, show_keyboard_activity}`
