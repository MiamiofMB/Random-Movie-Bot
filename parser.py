import json
import requests
from random import *
headers={
    'X-API-KEY':'H5VGER9-1SD4QN7-K3VS63Y-4R3GB9T'
}
def rand_mov(ganre):
    page = randint(1,200)
    r= requests.get(f'https://api.kinopoisk.dev/v1.3/movie?page={page}&genres.name={ganre}',headers=headers)
    return r.json()
