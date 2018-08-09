import json, config


def get_instructions():
    with open(config.env['FILE_HELP'], "r", encoding="utf-8") as file:
        msg = file.read()


def get_coins():
    with open(config.env['FILE_COINS'], "r", encoding="utf-8") as file:
        return json.load(file)


def update(data):
    with open(config.env['FILE_COINS'], "w", encoding="utf-8") as file:
        json.dump(data, file)