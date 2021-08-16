# olx-rest-api
A sample python-django project to assist OLX backend support. 

## Setup instructions
This doc will list set of instructions about how to configure this project.
### Virtualenv

Install `virtualenv`. Refer to [docs](https://virtualenv.pypa.io/en/latest/installation.html) 

Install `pipx`. Refer to [brew install from this link](https://pypi.org/project/pipx)

Run `virtualenv venv -p $(which python3)` to create venv with python3

For local `virtualenv` you can create a new folder `virtual-env` and install virtual env in this folder. 

To activate virtual environment. Run `source .venv/bin/activate`
### Run Project
Install all the dependencies `pip install -r requirements.txt`

Run `python api/manage.py runserver`

