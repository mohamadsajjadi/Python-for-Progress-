import requests
import json

chess_link = "http://127.0.0.1:8000/chess/"
physic_link = "http://127.0.0.1:8000/physic/"
math_link = "http://127.0.0.1:8000/math/"


def process(book):
    if book["category"] == "math":
        response = requests.get(math_link).json()
        for item in response:
            if book["name"] in item["name"]:
                return "bad query"
        requests.post(math_link, book)
    elif book["category"] == "physic":
        response = requests.get(physic_link).json()
        for item in response:
            if book["name"] in item["name"]:
                return "bad query"
        requests.post(physic_link, book)
    elif book["category"] == "chess":
        response = requests.get(chess_link).json()
        for item in response:
            if book["name"] in item["name"]:
                return "bad query"
        requests.post(chess_link, book)


print(process(book={"name": "Fermat's Last Theorem", "category": "math"}))
