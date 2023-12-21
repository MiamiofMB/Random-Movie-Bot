import json
import requests
from random import *
from secret.py import load_keys

load_keys()

headers={
    'X-API-KEY':header
}
def rand_mov(ganre):
    page = randint(1,200)
    r= requests.get(f'https://api.kinopoisk.dev/v1.3/movie?page={page}&genres.name={ganre}',headers=headers)
    return r.json()
