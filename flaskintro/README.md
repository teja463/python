# Flask Intro

## Local setup

- Install virtualenv package  `pip install virtualenv`
- Create a virtual environment `python -m virtualenv env`. You can use any name instead of env
- Activate the virtual environment `.\env\Scripts\activate`
- To create Database type `flask shell` to enter into flask shell mode
- Run `db.create_all()` it creates the test.db file inside instance folder
- Now `exit()` the shell
- Run `python app.py`
- For Webserver `pip install gunicorn`
- To Freeze requirements `pip freeze requirements.txt`
> Use cmd or powershell to execute the command, if you use bash then for activate env use `source ./env/Scripts/activate`


- 
## Concepts

- Flask uses ginger2 template engine
