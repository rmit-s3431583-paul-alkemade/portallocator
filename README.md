# Port Allocator - COSC1179

### Paul Alkemade, s3431583, 2019

This web application has been made using Python Django, utilising Bootstrap css for styling as well as Gmail as a mail server.

## Setting Up

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

Now that you are inside the virtualenv, install required modules using pip `pip install -r requirements.txt`

The setup is complete, you can now proceed to launch the development server

### Running The Development Server

Ensure you are in the virtualenv, `source venv/bin/activate`

Start the django dev server, `python manage.py runserver`

If all is well you should see something like 
```
System check identified no issues (0 silenced).
March 07, 2019 - 14:19:33
Django version 2.1.7, using settings 'portallocator.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Navigate to http://127.0.0.1:8000/ and give it a try

## User Guide

### Student User
Open http://127.0.0.1:8000/ via a browser, enter a student number, and two ports between 61000 and 61999. 
Once you click submit the app will check its internal database to ensure the ports have not yet been allocated, in which case it will send an email to fengling.han@rmit.edu.au for further processing. 

The app also features basic form validation to ensure port selection is valid/student number formatting is correct.

### Admin Portal
There is an additional administration portal, accessible at http://127.0.0.1:8000/admin, which is used to manage
port allocations. Once you have logged into the portal, click *port allocations* to review all current port allocation
requests submitted with allocated student numbers. These requests can also be removed from the database via the admin portal.

## Miscellaneous Details
### Email
Email is sent from the gmail account portallocator@gmail.com to itself, in order to change the destination address, simply change line 51 in portmanager/views.py from `['portallocator@gmail.com'],` to `['destination@email.com'],`

### Credentials
Please contact s3431583@student.rmit.edu.au for credentials to this account and the admin portal.

### Specification and not referencing Google Sheets
This application has been made according to the specifications detailed in the discussion post *Call for programmers to claim 3-5 marks bonus*, port allocations are therefore managed via an internal database. This application is intended to meet the spec for both Task 1 and Task 2

However, as per a question posted later, the application can be extended to allow cross reference checking of the google sheet - A sample quickstart.py file is available in the parent directory, as a reference in how to query the sheet using the Google Sheets API. *Please note this is just an example and requires a generated credentials.json using a private Google account*. 

This feature has not been implemented as Google Sheets will be disabled in the near future on the RMIT domain.
