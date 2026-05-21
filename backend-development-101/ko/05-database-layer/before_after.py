"""Generated from book-content article."""

def create_user(name):
    cur = db.execute("INSERT INTO users(name) VALUES(?)", (name,))
    return cur.lastrowid
