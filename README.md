# Django-practice
 Commands: python manage.py startapp appname  #Adding a new app


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
7. Create a superuser (in the terminal)   

    python manage.py createsuperuser
