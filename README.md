# Install Dependencies
Inside the `club-management` directory:

1.Install virtual environment

    $ python3 -m venv venv

Then go to the `src` directory:

    $ cd src

2.Activate virtual environment

    $ source venv/bin/activate

Then go back to the `club-management` directory:

    $ cd -

3.Install dependencies

    $ pip install -r requirements.txt

# Database setup

1.Create database named `club_managerment` in pgAdmin

Go to the `src` directory:

    $ cd src

2.Activate virtual environment

    $ source venv/bin/activate

3.Migrate to create tables

    $ python manage.py makemigrations
    $ python manage.py migrate 

4.Insert the sample data `DML_Django.sql` using the files in `SQL` directory with pgAdmin

# How to use the program

Go to the `src` directory:

    $ cd src

1.Activate virtual environment

    $ source venv/bin/activate

2.Run the server

    $ python manage.py runserver

3.Register or login

Register page: [http://127.0.0.1:8000/register/](http://127.0.0.1:8000/register/)

Login page: [http://127.0.0.1:8000/accounts/login](http://127.0.0.1:8000/accounts/login/)

4. Enjoy!

# Demo Link
https://youtu.be/wTKEI2SGTyE

Note that sql files in Demo Link have been moved to the `SQL` directory as specified.
