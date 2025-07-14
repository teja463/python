# Flask Intro

## Local setup

- Install virtualenv package  `pip install virtualenv`
- Create a virtual environment `python -m virtualenv env`. You can use any name instead of env
- Activate the virtual environment `.\env\Scripts\activate`
- To create Database type `flask shell` to enter into flask shell mode
- Run `db.create_all()` to create the sqlite database. It can be found in instance folder
- Now `exit()` the shell
- Run `python app.py`
- 
## Concepts

- Flask uses ginger2 template engine 
- 