import time

import requests
from pprint import pprint

auth = ('gfhjbkn_Kioue8', '4zC9YYaxPfqAqH4qdPtv')


def get_token() -> None:
    """Получение, перебор лога и сохранение токена"""
    time.sleep(40)

    data = _get_session_network_log()

    for item in data['entries']:
        for val in item['request']['headers']:
            if val['name'] == 'X-TN-Integrity-Session':
                token = val['value']
                print(f'Найден токен : {token}')
                with open(r"token.txt", "a") as file:
                    file.write(token + '\n')
                break


def _get_build() -> str:
    """Получение Идентификатора сборки"""

    r = requests.get(
        'https://api-cloud.browserstack.com/app-automate/builds.json', auth=auth)
    # print(r.json())
    builds = r.json()[0]
    this_build = builds['automation_build']['hashed_id']
    # print(this_build)
    return this_build


def _get_session_network_log() -> str:
    """Получение Идентификатора Сессии"""

    build = _get_build()
    get_session_url = f'https://api-cloud.browserstack.com/app-automate/builds/{build}/sessions.json'
    list_session = requests.get(get_session_url, auth=auth)
    # print(list_session.json())
    this_session = list_session.json()[0]
    # this_session = 'ffb9da1acca118044d9078a0246280004ffaa056'

    status = this_session['automation_session']['status']
    print(status)
    stop_status_l = ['timeout','failed']
    if status is not stop_status_l:
        this_session = this_session['automation_session']['hashed_id']
        print(f'Таргет сессия - {this_session}')

        network_log = requests.get(
            f'https://api.browserstack.com/app-automate/builds/{build}/sessions/{this_session}/networklogs', auth=auth)
        # print(type(network_log))
        # pprint(network_log.json())
        data = network_log.json()['log']
    else:
        print(f'Сессия неудачна, либо ещё запущена, статус {status}')
        data = None

    return data
