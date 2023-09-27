import pytest
import requests

URL = 'https://api.pokemonbattle.me:9104'
response = requests.get(f'{URL}/trainers?trainer_id=1708')


def test_statuscode():
    assert response.status_code == 200

def test_response_name():
    assert response.json()['trainer_name'] == 'Egor'