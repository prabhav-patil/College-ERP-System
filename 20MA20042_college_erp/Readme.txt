Running the Project:
Pre-reqs:
- Make sure that you have python and django installed on your computer.
If not, go to command prompt and type 'pip install django' and wait for
django to get installed.

Installation:
1. create a folder where you want to save this project in your computer.
2. open command prompt and change the directory to the project folder using the
change directory command ' cd ./(the path file to 'mysite' folder) '. Make sure that
your folder is saved in the original directory of your command prompt.
3. create the superuser for this project by 'python manage.py createsuperuser'.
this then requires you to put in username and password. You can put in 'admin'
as your username and 'admin' as password.
4. type in 'python manage.py runserver' to run the project.
5. the url will be provided in your command prompt. type the url into your
web browser to access and open the project.

About:
1. To check in student_login page, you can enter '20MA20018' as the roll number
and 'password' as password to login.
2. To check in faculty_login page, you can enter 'Glenda.Velazquez@gmail.com' as
the email and 'password' as password to login.
3. To go to admin login, go to your web browser, enter the ip address and add '/admin/'.
type in username as 'admin' and password as 'admin' to log in. Here, you can add and
manage all the data for all the tables in the database.