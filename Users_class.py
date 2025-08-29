class User:
    def __init__(self, user_id: int, first_name: str, last_name: str,
                 gender: str, birth_year: int, description: str):
        self.id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.birth_year = birth_year
        self.description = description

    def show_id(self):
        """Show user ID"""
        print(f"User ID: {self.id}")
    
    def show_profile(self):
        """Display complete user profile"""
        self.show_id()
        print(f"Full name: {self.first_name} {self.last_name}")
        print(f"Gender: {self.gender}")
        print(f"Birth year: {self.birth_year}")
        print(f"Description: {self.description}")
        print("-" * 40)