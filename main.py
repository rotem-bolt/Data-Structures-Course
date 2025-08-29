from AVLTree_class import AVLTree, load_users_into_tree, _Node
from Messages import Message
from MessageHashTable import MessageHashTable
from FriendsHashTable import FriendsHashTable

def load_messages():
    """Load all messages into hash table based on the table"""
    messages_hash = MessageHashTable()

    # לכל משתמש: {message_id: (טקסט, האם הודעה קיבלה לייק לפי הטבלה בצהוב)}
    initial_messages = {
        7: {
            1: {"message_text": 'היה חשמונאי', "is_liked": True},
            11: {"message_text": 'מי לה׳-אלי', "is_liked": False},
            18: {"message_text": 'נכה ביוונים', "is_liked": True},
            23: {"message_text": 'נארוב לפילים', "is_liked": False},
        },
        8: {
            2: {"message_text": 'צא ולמד', "is_liked": False},
        },
        9: {
            3: {"message_text": 'הגע בנפשך עד היכן', "is_liked": False},
            12: {"message_text": 'התבוא אלי?', "is_liked": False},
            19: {"message_text": 'שומר נפשו', "is_liked": False},
            24: {"message_text": 'תודה', "is_liked": False},
            26: {"message_text": 'בבקשה', "is_liked": False},
        },
        10: {
            4: {"message_text": 'חינם בלבד', "is_liked": True},
        },
        11: {
            5: {"message_text": 'רוקדים עם כוכבים', "is_liked": False},
            13: {"message_text": 'רוקד עם כוכבה', "is_liked": False},
            20: {"message_text": 'לא רוקדים', "is_liked": False},
        },
        12: {
            6: {"message_text": 'בשבת בלבד אליך ים', "is_liked": False},
            14: {"message_text": 'לבריכה', "is_liked": False},
        },
        13: {
            7: {"message_text": 'אני זמין החל מיום שני', "is_liked": False},
            15: {"message_text": 'נמצא בקוטב הצפוני', "is_liked": True},
        },
        14: {
            8: {"message_text": 'דובים מסביב, איזה פחד', "is_liked": True},
        },
        15: {
            9: {"message_text": 'ולאד המשפד (הערפד)', "is_liked": False},
            16: {"message_text": 'בטירת בראן', "is_liked": False},
            21: {"message_text": 'אגדה אורבנית', "is_liked": True},
        },
        16: {
            10: {"message_text": 'הודעההודעההודעה', "is_liked": False},
            17: {"message_text": 'לאלאלאלאלא', "is_liked": False},
            22: {"message_text": 'כןכןכןכ', "is_liked": False},
            25: {"message_text": 'בהחלט', "is_liked": True},
            27: {"message_text": 'אולי????', "is_liked": False},
        }
    }


    # טעינה לטבלה
    for user_id, msgs in initial_messages.items():
        for msg_id, data in msgs.items():
            messages_hash.add_message(user_id, Message(msg_id, data["message_text"], data["is_liked"]))

    return messages_hash

def load_friends() -> FriendsHashTable:
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

    ht = FriendsHashTable()
    for user_id, friends in friends_data.items():
        for f in friends:
            ht.add_friend(user_id, f)
    return ht

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # --- הנתונים ---
    users_data = [
        (1, "אא", "אא", "זכר", 2000, "אאאאאאאאאאאאאאאאאאאאאאאאא"),
        (2, "אא", "בב", "זכר", 2001, "אאאבבבאאאאבבבבאאאאאבבבבבבא"),
        (3, "אב", "גג", "זכר", 2002, "גגגגגגגגגגגגגגגגגגגגגגגגגגגגגגגגגגגגג"),
        (4, "אג", "דד", "זכר", 2003, "דדדדדדדדדדדדדדדדדדדדדדדדדדדדדד"),
        (5, "בא", "הה", "זכר", 2004, "ההההההההההההההה"),
        (6, "בב", "וו", "זכר", 2005, "הזהזהזהזהזהההזהזהזהזזזזזזזז"),
        (7, "בב", "זז", "זכר", 2006, "חיחיחיחיחיחיחיחיחחחחחללללללללל"),
        (8, "בג", "חח", "זכר", 2007, "בגבגבגבגבגבגבגבגבגבגבגבגבגבגבגבג"),
        (9, "גג", "טט", "נקבה", 2000, "גטגטטגטגטגטטטטטטגגגגגגגגג"),
        (10, "גד", "יי", "נקבה", 2001, "גדייגדייגדייגדייגדייגדייגדיייגדיי"),
        (11, "דד", "ככ", "נקבה", 2002, "בבדדבבדדבבדדבבג'יגיבורההההה"),
        (12, "יי", "לל", "נקבה", 2003, "ללליללהיאללההלאהללללללללללל"),
        (13, "ככ", "ממ", "נקבה", 2004, "כבודויקרמלא הארץ"),
        (14, "כא", "ננ", "נקבה", 2005, "יושביחושך וצלמוותאומרים בטקס כפרות בערביוםכיפור"),
        (15, "כב", "אא", "נקבה", 2006, "שנהטובהומאושרתשנתשלום ללאמלחמה"),
        (16, "כג", "בב", "נקבה", 2007, "בובקאטקאטקאטקתי"),
        (17, "לל", "גג", "זכר", 2000, "לוגלוגלוגלוגלוגלוגלוגלוגלוגלוגלוגלוג"),
        (18, "למ", "סס", "זכר", 2001, "איןלחסוםשורבדישו"),
        (19, "ממ", "עע", "זכר", 2002, "פשוטנבלהבשוקואלתצטרךלנדבה"),
        (20, "מנ", "פפ", "זכר", 2003, "פיקוחנפשדוחהשבתוחג"),
        (21, "ננ", "צצ", "זכר", 2004, "לךאלהנמלהעצלראהדרכיהוחכם"),
        (22, "נס", "קק", "נקבה", 2005, "השפןהקטןשכחלסגורהדלתבצטנןהמסכןוקיבלנזלת"),
        (23, "סס", "רר", "נקבה", 2006, "ביוסגרירללאחמהבימשתוממתהנשמה"),
        (24, "סע", "שש", "נקבה", 2007, "אםמיזהמהאומהזהמי"),
        (25, "עע", "תת", "נקבה", 2000, "מיאיזהואאיזהיאאיזשיאיזהר"),
    ]

    tree = AVLTree()
    load_users_into_tree(tree, users_data)

    # --- מידע כללי ---
    print(f"Total users in tree: {len(tree)}\n")

    # --- הדפסה ממוינת לפי ת\"ז (Inorder) ---
    print("=== All users (sorted by ID) ===")
    for user in tree.inorder():
        user.show_profile()
    ht = load_messages()

    # הצגת כל ההודעות של משתמש 7
    print("📌 הודעות של משתמש 7:")
    for m in ht.get_messages(7).values():
        m.show_message()
    # שליפת הודעה מסוימת
    print("\n📌 הודעה 3 של משתמש 7:")
    msg = ht.get_message(7, 3)
    if msg:
        msg.show_message()

    # הצגת כל המשתמשים וההודעות
    print("\n📌 כל ההודעות במערכת:")
    ht.show_all()

    friends_ht = load_friends()

    print("📌 כל החברים של משתמש 1:")
    print(friends_ht.get_friends(1))

    print("\n📌 כל מאגר החברים:")
    friends_ht.show_all()
