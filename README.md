# ACM-Website-Revamp
This is a Django application.

Steps to setup Django application on cPanel:

Step one:-  
=> Make a django project and upload it on cPanel in file manager.  
=> In seetings.py file in allowedHost add the url of hosting.  
=> In the virtual environment generate a requirements.txt file using the command "pip freez > requirements.txt".  
**Note that requirements.txt file should be there in the root directory not in any sub-directory.**

Step two:-  
=> In cpanel go to setup a python app.  
=> Choose the version of python you want.  
=> In appplication root write the path to your project directory in file manager.  
=> Application startup file shall generally be manage.py file.  
=> For the application entry point write the path from application root to th wsgi file.  
=> Click on create.  
=> A pop will be generated at the bottom asking to add files.  
=> Add requirements.txt file.  
=> Run pip install with requirements.txt.

Step three:-  
=> Now many files will be generated in the root directory.  
**passenger_wsgi.py file may contain some error and wrong syntax you'll have to modify it.**  
=> Now go to the app and change the Application startup file to passenger_wsgi.py and run pip install with requirements.txt again.  
=> Go to your hosting url, it should work now.


