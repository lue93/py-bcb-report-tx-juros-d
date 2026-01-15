
def write(data):
    with open("content.json", "w", encoding="utf-8") as f:
        f.write(data)

def read():
    data = ""
    try:
        with open("content.json", "r", encoding="utf-8") as f:
            data = f.read()
    except FileNotFoundError:
        raise FileNotFoundError("File content.json not found")
    finally:
        return data