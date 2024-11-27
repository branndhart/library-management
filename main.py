from library_management.services import Library
from library_management.utils import sleep_txt
from library_management.config import LIBRARY_FILE_PATH
import time
import json


def main():
    library = Library(LIBRARY_FILE_PATH)

    while True:
        print(sleep_txt("\n1. Добавить книгу"))
        print(sleep_txt("2. Удалить книгу"))
        print(sleep_txt("3. Найти книгу"))
        print(sleep_txt("4. Показать все книги"))
        print(sleep_txt("5. Изменить статус книги"))
        print(sleep_txt("6. Выйти\n"))

        choice = input(sleep_txt("Выберите действие: "))

        if choice == "1":
            title = input(sleep_txt("Введите название книги: "))
            author = input(sleep_txt("Введите автора: "))
            year = int(input(sleep_txt("Введите год: ")))
            library.add_book(title, author, year)
            output = sleep_txt("Книга добавлена.\n")
            for i in output:
                print(i, end="", flush=True)
                time.sleep(0.04)
            time.sleep(1)
            
        elif choice == "2":
            book_id = int(input(sleep_txt("Введите ID книги для удаления: ")))
            # Подтверждение удаления
            confirm = input(sleep_txt(f"Вы уверены, что хотите удалить книгу с ID {book_id}? (y/n): ")).strip().lower()
            if confirm == "y":
                library.delete_book(book_id)
                print("Книга удалена.\n")
            else:
                print("Удаление отменено.\n")
            time.sleep(1)
            
        elif choice == "3":
            key = input("По какому полю искать (id, title, author, year): ")
            value = input("Введите значение для поиска: ")
            
            if key in {"id", "year"}:
                value = int(value)
                
            results = library.find_books(**{key: value})
            if results:
                for book in results:
                    print(json.dumps(book.to_dict(), indent=4, ensure_ascii=False))
                    print()
                time.sleep(1)
            else:
                print("Книги не найдены.\n")
                time.sleep(1)
                
        elif choice == "4":
            books = json.dumps(library.display_books(), indent=4, ensure_ascii=False)
            print(books, end="\n")
            time.sleep(1)
            
        elif choice == "5":
            book_id = int(input("Введите ID книги: "))
            new_status = input("Введите новый статус (в наличии/выдана): ")
            library.update_status(book_id, new_status)
            print(sleep_txt("Статус обновлен."))
            time.sleep(1)
            
        elif choice == "6":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
            time.sleep(1)


if __name__ == "__main__":
    main()
