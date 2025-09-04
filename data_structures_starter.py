from AVLTree import AVLTree
from User import User
from Message import Message
from FriendsHashTable import FriendsHashTable
from MessageHashTable import MessageHashTable

users_data = [
        (1, "Alon", "Avraham", "male", 2000, "alonavraham@gmail.com"),
        (2, "Bar", "Bib", "male", 2001, "barbib@gmail.com"),
        (3, "Cici", "Cohen", "female", 2002, "cicic@gmail.com"),
        (4, "David", "Danon", "male", 2003, "daviddanon@gmail.com"),
        (5, "Eran", "Boim", "male", 2005, "eranboim@gmail.com"),
        (6, "Faran", "Keren", "female", 2006, "farankeren@gmail.com"),
        (7, "Gabi", "Gonen", "male", 2002, "gabigonen@gmail.com"),
        (8, "Hen", "Hacohen", "male", 2007, "henhacohen@gmail.com"),
        (9, "Ilan", "Nachum", "male", 2000, "ilannachum@gmail.com"),
        (10, "Jakob", "Levi", "male", 2005, "jakoblevi@gmail.com"),
        (11, "Kobi", "Levi", "male", 2006, "kobillevi@gmail.com"),
        (12, "Lilach", "Levi", "male", 2007, "liorlevi@gmail.com"),
        (13, "Lib", "Levi", "male", 2000, "liblevi@gmail.com"),
        (14, "Lior", "Shalom", "male", 2001, "gilsalom@gmail.com"),
        (15, "Meni", "Ben Hamo", "female", 2002, "menibenhamo@gmail.com"),
        (16, "Noa", "Levi", "female", 2003, "noalevi@gmail.com"),
        (17, "Oren", "Or", "male", 2004, "orenor@gmail.com"),
        (18, "Or", "Levi", "male", 2001, "orlevi@gmail.com"),
        (19, "Pini", "Levi", "male", 2002, "pinilevi@gmail.com"),
        (20, "Pnina", "Levi", "male", 2003, "pninlevi@gmail.com"),
        (21, "Qalanit", "Calanit", "female", 2004, "qalanitcalanit@gmail.com"),
        (22, "Rina", "Levi", "female", 2005, "rinalevi@gmail.com"),
        (23, "Roni", "Levi", "male", 2006, "ronilevi@gmail.com"),
        (24, "Rona", "Levi", "female", 2007, "ronalevi@gmail.com"),
        (25, "Sharon", "Levi", "female", 2000, "sharonlevi@gmail.com"),
]

friends_data = {
        1: [2,4,6,8,10,21,23,25],
        2: [1,3,4,7,9,11,13,15],
        3: [1,2,4,25,24],
        4: [25,22,13,11,9,8,6],
        5: [6,9,17,18,19,24],
        6: [4,5,7,11,12,15,17,20],
        7: [25],
        8: [1,7],
        9: [22,25,17,16,19,5],
        10: [],
        11: [],
        12: [13,14,25],
        13: [24,4,6,19],
        14: [18,17,16,15,6],
        15: [3,13,23],
        16: [7,17,25],
        17: [18,20],
        18: [2,5,9,11],
        19: [],
        20: [21,11,1,14],
        21: [],
        22: [20,19,17,9,7,5],
        23: [6,16,8,18,21,11],
        24: [12,14,16,18,20],
        25: [24],
}

messages_data = {
        7: {
            1: {"message_text": 'text1', "likes": [1]},
            11: {"message_text": 'text11', "likes": [11]},
            18: {"message_text": 'text18', "likes": [18,16]},
            23: {"message_text": 'text23', "likes": [23]},
        },
        8: {
            2: {"message_text": 'text2', "likes": [2]},
        },
        9: {
            3: {"message_text": 'text3', "likes": [3]},
            12: {"message_text": 'text12', "likes": [12]},
            19: {"message_text": 'text19', "likes": [19,14]},
            24: {"message_text": 'text24', "likes": [24]},
            26: {"message_text": 'text26', "likes": [22]},
        },
        10: {
            4: {"message_text": 'text4', "likes": [4]},
        },
        11: {
            5: {"message_text": 'text5', "likes": [5]},
            13: {"message_text": 'text13', "likes": [13]},
            20: {"message_text": 'text20', "likes": [20,15]},
        },
        12: {
            6: {"message_text": 'text6', "likes": [6]},
            14: {"message_text": 'text14', "likes": [14]},
        },
        13: {
            7: {"message_text": 'text7', "likes": [7]},
            15: {"message_text": 'text15', "likes": [15]},
        },
        14: {
            8: {"message_text": 'text8', "likes": [8]},
        },
        15: {
            9: {"message_text": 'text9', "likes": [9]},
            16: {"message_text": 'text16', "likes": [16,10]},
            21: {"message_text": 'text21', "likes": [21,12]},
        },
        16: {
            10: {"message_text": 'text10', "likes": [10]},
            17: {"message_text": 'text17', "likes": [17,11]},
            22: {"message_text": 'text22', "likes": [22]},
            25: {"message_text": 'text25', "likes": [25,13]},
            27: {"message_text": 'text27', "likes": [22]},
        }
}

def load_users(tree: AVLTree, users_data: list[tuple]) -> None:
    """
    Load user data from list of tuples into AVL tree
    Each tuple should be: (user_id, first_name, last_name, gender, birth_year, email)
    """
    for user_tuple in users_data:
        if len(user_tuple) == 6:
            user_id, first_name, last_name, gender, birth_year, email = user_tuple
            user = User(user_id, first_name, last_name, gender, birth_year, email)
            tree.insert(user_id, user)
        else:
            print(f"Warning: Invalid user data tuple: {user_tuple}")

def load_messages(messages_hash: MessageHashTable, messages_data: dict, msg_counter: int):
    for user_id, msgs in messages_data.items():
        for msg_id, data in msgs.items():
            messages_hash.add_message(user_id, Message(msg_id, data["message_text"], data["likes"]))
            msg_counter += 1

    return messages_hash, msg_counter

def load_friends(friends_hash: FriendsHashTable, friends_data: dict):
    for user_id, friends in friends_data.items():
        for f in friends:
            friends_hash.add_friend(user_id, f)
    return friends_hash
