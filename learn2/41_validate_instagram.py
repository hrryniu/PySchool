import re
url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?instagram\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username:",matches.group(1))

    #wartosci w nawiasie i zakończone znakiem zapytania są opcjonalne, nie muszą być wpisane żeby imput był valid
    # znak zapytania zaraz po "s" mówi że s jest opcjonalne. więc https i http wejdą.