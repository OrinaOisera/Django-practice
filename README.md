# Django-practice
 Commands:
dgit jango-admin startproject project name   #start start project
 

python manage.py startapp appname  #Adding a new app


manage.py  ---> is commandline utility to perform admin tasks 

wsgi.py    --->Web Server  Gateway Interface (describes communication btwn webserver & another application)

asgi.py   --->Asynchronous Gateway Interface 

__init.py ---> holds the packages and how they will be looked up 



Models ---> Are python classes that make our data consistent 
       
       ----> Classes are Mapped to database tables
       ----> Fields  are Mapped to database columns
       -----> Objects are mapped to database rows

Migrations 
Python scripts that change the data base to keep db structure in sync with code


#Models & Migrations workflow
- Make sure your    app is in INSTALLED_APPS in settings.py 
1. Create/change your models in models.py 
2. Generate migration script (check it!) 
     
    python manage.py makemigrations
3. Optional: Show migrations
    
     python manage.py showmigrations
4. Optional: Show SQL for specific migration
  
   python manage.py sqlmigrate appname migrationname
5. Step 3: Run migrations
    
    python manage.py migrate
6. Register Model with Admin site on Admin.py 
    
    from .models import example_Model
    admin.site.register(example_Model)
Remember : Create a superuser (in the terminal)   

    python manage.py createsuperuser
7. Run app 
      python manage.py runserver   (runs on default port 8000) 
      python manage.py runserver 8080  (runss on port 8080)

#Model View  Template  pattern
Template  -- Components that display data to the user.

          -- Generates text files and html files

          -- contains special place holders for variables thus creating dynamic html files.

View     --the func calls the correct template

          --uses the func render: pass request and name of template file

          --Third argument: dict with data passed to the template

           --Templates should be in folder /templates inside app

Model    -- Represents the data that live in the application (Models classes mapped to data BASE TABLES)




#Retrieving Model DATA

meeting = Meeting.objects.all()    [Gets all objects]

meeting = Meeting.objects.count()   [Get object count]

meeting = Meeting.objects.get(pk=4)  [Get specific object]


---------------------------------------------------------------------------

manage.py 



Use re_apth to return an element for inclusion in your url pattern.


#Class-Based Geneic views 

Display static html content : Template view   
Display list of items : List View
