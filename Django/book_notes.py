# começar um novo projeto: 
# abrir a pasta no terminal e digitar
# django-admin startproject <nome_do_projeto>
# por exemplo:
# django-admin startproject learning_site

# navegar até a pasta learning_site
# python manage.py runserver 0.0.0.0:8000
# no navegador, testar:
# localhost:8000

# criar um app 
# python manage.py startapp courses
# ira criar a pasta 'courses'
# ir até learning_site/settings.py e incluir courses em INSTALLED_APPS

# criado um 'Model' no arquivo models.py (class Clourses)
# python manage.py makemigrations courses
# ira criar um arquivo na pasta migrations

# caso não tenha sido feito, python manage.py migrate
# python manage.py shell
# Course.objects.create(title='Object-Oriented Python', description='Learn about Python classes')
# Isso deverá criar objeto no banco de dados [?]
# ao verificar Course.objects.all() irá aparecer os objetos criados
# ao criar o seguinte, no arquivo models.py:
    # def __str__(self):
    #     return self.title
# irá retornar o título de cada curso, nesse caso

