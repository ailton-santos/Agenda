# Agenda

  
</ul>

<h2>project_agenda</h2>

Create development environment, create the project folder and inside it create the virtual environment:
``` 
mkdir projeto_agenda
cd projeto_agenda/
python3  -m venv env
source env/bin/activate
```

(to close virtual env type deactivate)

 install Django:
```
pip3 install django
```
Start Django
```
django-admin startproject agenda 
cd agenda
```
The project is called "agenda" and inside it we will launch the apps
```
cd agenda

django-admin startapp agenda
django-admin startapp agendador
django-admin startapp accounts

```
<h2>Run project after git-clone:</h2>
To start this project, after placing it, enter the project page:

```
cd projeto_agenda/agenda
```
Instalar e configurar o pacote crispy_forms para uso de templates:
```
pip install django-crispy-forms
```
Include the app in the project's settings.py in the following fields:
```
INSTALED_APPS = [
    ...
    'crispy_forms', 
]

CRISPY_TEMPLATE_PACK = 'uni_form'
```
Now upload the project with manage:
```
python3 manage.py makemigrations 
python3 manage.py migrate
python3 manage.py runserver
```
