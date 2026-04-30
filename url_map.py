from shortener import generate_short_code

url_db = {}

def shorten_url(original_url):
    
    code = generate_short_code()
    
    url_db[code] = original_url
    
    return code

def get_original_url(code):
    
    return url_db.get(code, "Not found")


if __name__ == "__main__":
    
    short = shorten_url("https://example.com")
    print("Short code:", short)
    
    print("Original URL:", get_original_url(short))