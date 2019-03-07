# Port Allocator - COSC1179

### Paul Alkemade, s3431583, 2019

This web application has been made using Python Django, utilising Bootstrap css for styling as well as Gmail as a mail server.

### Requirements
Python 3.4 (Must be installed prior to "Initial Setup")

VirtualEnv (Installed during "Initial Setup")

Django 2.1.7 (Installed during "Initial Setup")

### Initial Setup - Linux/Mac OSX Terminal
*Also works with Windows Cmd Prompt - Ensure python3/pip/git are added to PATH if doing this all via the cmd shell, some helpful installation steps for Python, Pip and Virtual Env can be found here - http://timmyreilly.azurewebsites.net/python-pip-virtualenv-installation-on-windows/)*

Clone the repo to your machine
`git clone https://github.com/rmit-s3431583-paul-alkemade/portallocator.git`

Navigate inside the project directory

Install VirtualEnv using pip
`pip install virtualenv`

Create the virtual environment for python 3
`virtualenv -p python3 venv`, then activate it
`source venv/bin/activate`

Now that you are in the virtualenv, install required modules using pip `pip install -r requirements.txt`

The setup is complete, you can now proceed to launch the development server

### Running The Development Server

Ensure you are in the virtualenv, `source venv/bin/activate`

Start the django dev server, `python manage.py runserver`
