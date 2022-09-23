# django-bootstrap
# DineshTechSolutions
#git info
#https://git-scm.com/download
#clone-link : https://github.com/DineshBadugu/DineshTechSolutions.git



#install env 
#pip install virtualenv
# create virtual environment
#python -m venv env-dt7

# activate virtual environment
#env-dt7\Scripts\activate

# install libs
pip install -r requirements.txt

# create django  project
Django-admin startproject "PROJECTNAME"

# create django app 
python manage.py startapp "APP NAME"

# create super user 
python manage.py createsuperuser
# migration process 
python manage.py makemigrations 

# run migrations 
python manage.py migrate 

# Run project or applications
python manage.py runserver

