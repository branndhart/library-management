from typing import List
from library_management.models import Book
import json


class Library:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.books = self.load_books()

    def load_books(self) -> List[Book]:
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Book.from_dict(book) for book in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_books(self):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(
                [book.to_dict() for book in self.books], f, ensure_ascii=False, indent=4
            )

    def add_book(self, title: str, author: str, year: int):
        new_id = max([book.id for book in self.books], default=0) + 1
        new_book = Book(book_id=new_id, title=title, author=author, year=year)
        self.books.append(new_book)
        self.save_books()

    def delete_book(self, book_id: int):
        self.books = [book for book in self.books if book.id != book_id]
        self.save_books()

    def find_books(self, **kwargs) -> List[Book]:
        results = self.books
        for key, value in kwargs.items():
            results = [book for book in results if getattr(book, key) == value]
        return results

    def display_books(self) -> List[dict]:
        return [book.to_dict() for book in self.books]

    def update_status(self, book_id: int, new_status: str):
        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                break
        self.save_books()
