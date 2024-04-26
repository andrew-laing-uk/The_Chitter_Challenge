from lib.peep import Peep

class PeepRepository:

    def __init__(self, connection):
        self._connection = connection

    # Retrieve all peeps
    def all(self):
        rows = self._connection.execute('SELECT * from peeps')
        peeps = []
        for row in rows:
            taglist = row["tags"].replace(' ','').split(',')
            item = Peep(row["id"], row["content"], str(row["time_of_post"]), taglist, row["maker_id"])
            peeps.append(item)
        return peeps
    
    def find(self, peep_id):
        rows = self._connection.execute(
            'SELECT * from peeps WHERE id = %s', [peep_id])
        row = rows[0]
        taglist = row["tags"].replace(' ','').split(',')
        return Peep(row["id"], row["content"], str(row["time_of_post"]), taglist, row["maker_id"])
    