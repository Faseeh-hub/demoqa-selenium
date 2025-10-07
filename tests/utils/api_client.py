# tests/utils/api_client.py
import requests

class BookStoreAPI:
    BASE = "https://demoqa.com/BookStore/v1"

    def get_all_books(self):
        r = requests.get(f"{self.BASE}/Books")
        if r.status_code == 200:
            return r.json().get("books", [])
        return []
