import configparser
import os


config = configparser.ConfigParser()

config_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "config",
    "config.ini"
)

config.read(config_path)


def get_application_url():
    return config["application"]["url"]


def get_browser():
    return config["application"]["browser"]