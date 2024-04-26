class Peep():
    def __init__(self, id, content, time_of_post, tags, maker_id):
        self.id = id
        self.content = content
        self.time_of_post = time_of_post
        self.tags = tags or []
        self.maker_id = maker_id

    def __repr__(self):
        return f"Peep({self.id}, {self.content}, {self.time_of_post}, {self.tags}, {self.maker_id})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
