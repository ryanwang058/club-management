1. install virtual environment
python3 -m venv venv

2. activate
source venv/bin/activate

3. install dependencies
pip install -r requirements.txt

4. start backend server
python manage.py runserver

# database setup
create database club_managerment in pgAdmin
python manage.py makemigrations 
python manage.py migrate 

python manage.py createsuperuser
- Email: 