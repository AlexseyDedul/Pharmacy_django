# Pharmacy_django

git clone https://github.com/AlexseyDedul/Pharmacy_django.git

cd pharmacy

sudo apt install python3.8-venv

python3 -m venv venv

. venv/bin/activate

pip3 install -r req.txt

#install postgres and create user with db
sudo apt-get install postgresql
sudo postgres psql
CREATE USER name WITH PASSWORD 'pass';
create database pharmacy;

python manage.py migrate

./manage.py createsuperuser

python manage.py runserver