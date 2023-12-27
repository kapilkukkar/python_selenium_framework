
from configparser import ConfigParser


def read_data(category, key):
    config = ConfigParser()
    config.read('C:\\Users\\kumar\\PycharmProjects\\Selenium_python_project\\configuration\\config.ini')
    return config.get(category, key)

