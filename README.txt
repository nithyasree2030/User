
Conversation opened. 1 read message.

Skip to content
Using Gmail with screen readers
Meet
New meeting
Join a meeting
Hangouts
2 of 7,007
readme
Inbox
Nithya sree <nithyasree30800@gmail.com>

AttachmentsTue, Apr 19, 10:09 PM (11 hours ago)

to me

Attachments area




Create a virtual environment --> virtualenv venv
Activate the virtual environment --> source bi368707n/activate
Install django --> pip install django
Install psycopg2 --> pip install psycopg2-binary
Start a project --> django-admin startproject user
Create app for the project --> python manage.py startapp team
In settings, add the app name 'team' in INSTALLED_APPS

Install DRF --> pip install django-restframework
In settings, add 'django-restframwork' in the INSTALLED_APPS

Create the customer user model with email and password as the authentication fields
Create model for team, team members, task

Do Migration:
python manage.py makemirations
python manage.py migrate


Create a super user:
python manage.py createsuperuser
Enter the credentails--> Email: xxx.gmail.com
password - ********
Confirm password - ********

Add the model class in the admin.py as admin.site.register(ModelName)

Serializers.py:
Create a ModelSerializers for all the modlel class

views.py:
Do the authentication and authorization for the user using JWT token
Install JWT --> pip install djangorestframework-simplejwt
In settings.py, add the JWT token as default


Using ListCreateView, make User, Team, Team members, Task creation/get all along with pagination
Add the PageNumberPagination in the settings.py in RESTFRAMEWORK

Using token authentication assign a task for the team members only if the team member is available.
Update the task status by team member

README.txt
Displaying README.txt.