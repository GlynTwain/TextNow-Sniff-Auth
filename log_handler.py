import requests
# from pprint import pprint

auth = ('gfhjbkn_Kioue8', '4zC9YYaxPfqAqH4qdPtv')


def get_token()->None:
    """Получение, перебор лога и сохранение токена"""
    data = _get_session_network_log()

    for item in data['entries']:
        for val in item['request']['headers']:
            if val['name'] == 'X-TN-Integrity-Session':
                token = val['value']
                print(f'Найден токен : {token}')
                break
    with open(r"token.txt", "w") as file:
        file.write(token + '\n')


def _get_build()->str:
    """Получение Идентификатора сборки"""

    r = requests.get(
        'https://api-cloud.browserstack.com/app-automate/builds.json', auth=auth)
    # print(r.json())
    builds = r.json()[-1]
    this_build = builds['automation_build']['hashed_id']
    # print(this_build)
    return this_build


def _get_session_network_log()->str:
    """Получение Идентификатора Сессии"""

    build = _get_build()
    get_session_url = f'https://api-cloud.browserstack.com/app-automate/builds/{build}/sessions.json'
    list_session = requests.get(get_session_url, auth=auth)
    # print(list_session.json())

    this_session = list_session.json()[-1]
    this_session = this_session['automation_session']['hashed_id']
    # pprint(this_session)

    network_log = requests.get(
        f'https://api.browserstack.com/app-automate/builds/{build}/sessions/{this_session}/networklogs', auth=auth)
    data = network_log.json()['log']

    return data
