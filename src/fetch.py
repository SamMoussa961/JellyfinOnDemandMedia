import os
import requests
import datetime
from dotenv import load_dotenv

load_dotenv()

def api_response(api, api_key, how_long):
    response = requests.get(
        api,
        headers={'X-Emby-Token': api_key},
        params={
            'minDate': (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(
                minutes=how_long)).isoformat()
        }
    )
    if response.status_code != 200:
        return response.status_code, []

    data = response.json()
    items = data.get('Items')
    return response.status_code, items