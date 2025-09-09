class Message:
    def __init__(self, message_id: int, message_text: str, likes: list[int]):
        self.id = message_id
        self.message_text = message_text
        self.likes = likes

    def show_message(self):
        """Show message"""
        print(f"Message ID: {self.id}\nMessage text: {self.message_text}\nLikes: {self.likes}")

    def get_message_text(self):
        return self.message_text

    def get_likes(self):
        return self.likes

    def get_id(self):
        return self.id

    def __repr__(self):
        return f"Message({self.id}, '{self.message_text}', {self.likes})"