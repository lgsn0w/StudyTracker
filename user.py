import bcrypt

class user:
    def __init__(self,username, password):
        self.username = username
        self.password = password

    def check_password(self, password):
        return bcrypt.checkpw(password.encode(), self.password)

def find_user(conn,username):
    c = conn.cursor()
    c.execute("SELECT username, password FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    if user is not None:
        return user
    else:
        return None



def close_conn(conn):
    conn.close()