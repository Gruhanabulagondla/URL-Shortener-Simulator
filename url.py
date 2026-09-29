import random
import string

url_database = {}


def generate_code():
    characters = string.ascii_letters + string.digits

    while True:
        code = ''.join(random.choice(characters) for _ in range(6))

        if code not in url_database:
            return code


def shorten_url(url):
    code = generate_code()
    url_database[code] = url
    return code


def retrieve_url(code):
    return url_database.get(code)


def main():
    print("========== URL SHORTENER ==========")

    while True:
        print("\n1. Shorten URL")
        print("2. Retrieve Original URL")
        print("3. View All URLs")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            url = input("\nEnter long URL: ")

            code = shorten_url(url)

            print("Short Code:", code)
            print("Short URL: short.ly/" + code)

        elif choice == "2":
            code = input("\nEnter short code: ")

            url = retrieve_url(code)

            if url:
                print("Original URL:", url)
            else:
                print("URL not found.")

        elif choice == "3":
            print("\n---------- STORED URLS ----------")

            if not url_database:
                print("No URLs stored.")
            else:
                for code, url in url_database.items():
                    print("short.ly/" + code, "->", url)

        elif choice == "4":
            print("\nThank you!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()