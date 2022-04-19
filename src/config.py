from distutils.command.config import config
from distutils.debug import DEBUG


class DevelopmentConfig(): # creamos una clase para el desarrollo
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'api-jhon'

# Cramos un diccionario para el renderizado del archivo 
config={
    'development': DevelopmentConfig
}