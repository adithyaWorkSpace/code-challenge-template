# Instructions to build Weather Data API
### Scope:
This Django-based Weather API delivers weather data to users. It includes guidelines for setting up a virtual environment, installing necessary dependencies, applying migrations, and importing data. Furthermore, it provides details on how to access and utilize the API.

### Prerequisites:
``` shell
Python Version: 3.12.4
Postgres Version:15.x
AWS Account(if deploying to AWS)
```

### Requirments:
After cloning the github repository, create a virtual environment by executing the following command.
``` shell
python3 -m venv <env_name>
```

### Activate the virtual environment by executing the following command.
``` shell
source <env_name>/bin/activate
```

### Install the dependencies by executing the following command.
``` shell
pip3 install -r requirements.txt
```

### Database Setup:

```shell
brew install postgresql
sudo -u postgres psql
CREATE DATABASE mydatabase;
CREATE USER dbuser WITH PASSWORD dbpassword ;
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO dbuser;
```

Update settings.py with your database credentials.
``` shell
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'your_db_host',
        'PORT': '5432'
    }
}
```

### Run weather_data.py
Execute the below command in terminal to insert weather data into database (weather_data table).
``` shell
python django_project/weather_data.py
```

### Run weather_stats.py
Execute the below command in terminal to calculate weather statistics and insert result in weather_stats table in database.
``` shell
python django_project/weather_stats.py
```

### Migrate:
Execute below command to migrate all the migrations to the database.
``` shell
python django_project/manage.py makemigrations
python django_project/manage.py migrate
```

### Runserver:
Execute the below command to start Django developement server.
``` shell
python django_project/manage.py runserver
```

### API Endpoints:
Once the application is running, navigate to below url in your browser to access and try out the endpoints.
```shell
http://127.0.0.1:8000/api/weather
http://127.0.0.1:8000/api/weather/stats
http://127.0.0.1:8000/api/schema/swagger-ui/
```
Both endpoints apply a filter based on the filename (station ID) and date fields. Additionally, a "page" field is used to handle pagination. The page size is set to 100, but it can be adjusted in the settings.py file.


### Testing:
To run tests, execute the below command.
```shell
python manage.py test app.tests.WeatherDataAndStatsTests
```

## Project Structure:
``` shell
Django_project/
│
├── django_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│
├── manage.py
├── weather_data.py
├── weather_statistics.py
├── db_connection.py
└── queries.sql
```
### Deployment in AWS:
- Create AWS account.
- Create an EC2 instance.
- Establish a CI/CD pipeline for the continuous deployment either by using jenkins.
- Setup a virtual environment in EC2 instance and install project dependencies from requirements.txt.
- Create a new PostgreSQL RDS instance.
- Run Django migrations on the EC2 instance to set up the database schema.
- Configure a web server like Apache on the EC2 instance.
- Test your deployment to ensure your Django application is accessible via the domain name.
- AWS CloudWatch for monitoring the EC2 instance and application logs.

### Screenshots:
![image](https://github.com/user-attachments/assets/f734480b-b422-4373-b21b-3ed600468230)
