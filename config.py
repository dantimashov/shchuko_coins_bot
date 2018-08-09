from os.path import join, dirname
import yaml


def load_env(config_file):
    path = join(dirname(__file__), config_file)
    with open(path) as file:
        return yaml.load(file)


env = load_env('config.prod.yml')