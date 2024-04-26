from lib.maker import Maker

class MakerRepository:

    def __init__(self, connection):
        self._connection = connection

    # Retrieve all makers
    def all(self):
        rows = self._connection.execute('SELECT * from makers')
        albums = []
        for row in rows:
            item = Maker(row["id"], row["full_name"], row["username"], row["user_email"], row["user_password"])
            albums.append(item)
        return albums

    # Find a single maker by its id
    def find(self, maker_id):
        rows = self._connection.execute(
            'SELECT * from makers WHERE id = %s', [maker_id])
        row = rows[0]
        return Maker(row["id"], row["full_name"], row["username"], row["user_email"], row["user_password"])
    
    def username_is_unique(self, username):
        rows = self._connection.execute(
            'SELECT * from makers WHERE username = %s', [username])
        return len(rows) == 0

    def email_is_unique(self, email):
        rows = self._connection.execute(
            'SELECT * from makers WHERE user_email = %s', [email])
        return len(rows) == 0