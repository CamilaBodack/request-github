"""
Modulo que contém funcionalidades que podem ser uteis em todo o sistea
"""

import requests


def get_username(username: str) -> dict:
    return requests.get(f"https://api.github.com/users/{username}").json()
