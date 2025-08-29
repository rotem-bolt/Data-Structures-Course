user_type = {
    "first_name": str,
    "last_name": str,
    "user_id": int,
    "is_male": bool,
    "birth_year": int,
    "description": str,
}

message_type = {
    "user_id": int,
    "messages": [
        {
            "message_id": int,
            "message_text": str,
            "is_liked": bool,
        }
    ]
}

friends_type = {
    int: list[int]
}

likes_type = list[int]