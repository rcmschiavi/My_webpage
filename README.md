# My portfolio webpage

This repository was created with the intention of organize my webpage coding project. Which was created just to host a simple page for my data aquisition project but ended up increasing and it became an entire webpage.

On the previous repository I commited the django's project secret_key and that is not a good practice. Now I used dotenv to create a environment file for storing the keys and hash that I'll use along the project creation.

Thus, I'll use this repository to version control the webpage creation. 

## Applications

### Pedidos

This application was developed as a test for a Django position.

You can check the app [here](https://rodolfoschiavi.pythonanywhere.com/portfolio/app/pedidos).

Database diagram: 
![data_base_diagram](docs/pedidos_models.png)

The diagram was generated using pydotplus. For [more details](https://simpleit.rocks/python/django/generate-uml-class-diagrams-from-django-models/)


## Good practices

- Update the requirements when installing new packages:
    - ``` pip freeze > requirements.txt ``` 

## Notes for configuring Local environment

- Create an Environment;
- Install requirements;
    - ``` pip install -r requirements.txt ```
- Install mysql: ``` sudo apt install mysql-server ```
- Login with root: ``` mysql -u root ```
- Create a user to acess the database trough django: ``` CREATE USER 'rodolfoSchiavi'@'localhost' IDENTIFIED BY 'easy_password'; ```
- Grant access to everything: ``` GRANT ALL PRIVILEGES ON * . * TO 'rodolfoSchiavi'@'localhost'; ```
- You know what this means: ``` FLUSH PRIVILEGES; ```
- Create database "all_data": ``` CREATE DATABASE all_data; ```
- Exit the mysql bash;
- Import the backup file to the previously created database: 
    - If you have the full version: ``` sudo mysql -u root all_data < db-backup-2021.sql ```
    - If you just have the provided at the repository: ``` sudo mysql -u root all_data < db-backup-2021-no_user_hashpass.sql ```
        - In this case the shared backup has a small change at the auth_user table, since it has my admin access password hash. If you wanna use it for some unimaginable reason, probably you are me in the future and I lost the full file. Anyway, you will need to copy the tables to your new project or do some magic to avoid conflicts. Maybe making a migration with django would solve, dunno.

**Now enjoy it by running: ``` python manage.py runserver ```**

### MySQL client viewer

If you want to check the data, install phpmyadmin. To access the database run http://localhost/phpmyadmin/, if it didn't run at first follow this [askubuntu topic](https://askubuntu.com/questions/19127/how-to-access-phpmyadmin-after-installation) to solve the common issue
