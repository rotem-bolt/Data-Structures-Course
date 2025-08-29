class Message:
    def __init__(self, message_id: int, message_text: str, is_liked: bool):
        self.id = message_id
        self.message_text = message_text
        self.is_liked = is_liked

    def show_message(self):
        """Show message"""
        print(f"Message ID: {self.id}\nMessage text: {self.message_text}\nIs liked: {self.is_liked}")

    def get_message_text(self):
        return self.message_text

    def get_is_liked(self):
        return self.is_liked

    def get_id(self):
        return self.id

    def __repr__(self):
        return f"Message({self.id}, '{self.message_text}', {self.is_liked})"