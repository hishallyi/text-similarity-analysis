"""
@Author : Hishallyi
@Date   : 2024/7/22
@Code   : 文心一言 api
"""

import requests
import json

API_Key = 'ARTiXOfYDoIwrBhRo0FLRSoT'
Secret_Key = 'BvHofSd0ENnmKkRID1IYR0lgbO1VP3aT'


def main():
    url = "https://aip.baidubce.com/oauth/2.0/token?client_id=ARTiXOfYDoIwrBhRo0FLRSoT&client_secret=BvHofSd0ENnmKkRID1IYR0lgbO1VP3aT&grant_type=client_credentials"

    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


if __name__ == '__main__':
    main()
