import json, config, urllib3


def get_instructions():
    with open(config.env['FILE_HELP'], "r", encoding="utf-8") as file:
        return file.read()


def get_coins():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    response = urllib3.PoolManager(cert_reqs='CERT_NONE', retries=False).request('GET', config.env['URL_COINS'])
    return response.data.decode('cp1251')
