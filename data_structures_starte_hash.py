from types import user_type, message_type, friends_type, likes_type


users_data_structure: list[user_type] = {
    1: {
    "first_name": 'אא',
    "last_name": 'אא',
    "is_male": True,
    "birth_year": 2000,
    "description": 'אאאאאאאאאאאאאאאאאאאאאאאאא',
    },
    2: {
    "first_name": 'אא',
    "last_name": 'בב',
    "is_male": True,
    "birth_year": 2001,
    "description": 'אאאבבבאאאאבבבבאאאאאבבבבבבא',
    },
    3: {
    "first_name": 'אב',
    "last_name": 'גג',
    "is_male": True,
    "birth_year": 2002,
    "description": 'גגגגגגגגגגגגגגגגגגגגגגגגגגגגגגגגגגגגג',
    },
    4: {
    "first_name": 'אג',
    "last_name": 'דד',
    "is_male": True,
    "birth_year": 2003,
    "description": 'דדדדדדדדדדדדדדדדדדדדדדדדדדדדדד',
    },
    5: {
    "first_name": 'בא',
    "last_name": 'הה',
    "is_male": True,
    "birth_year": 2004,
    "description": 'ההההההההההההההה',
    },
    6: {
    "first_name": 'בב',
    "last_name": 'וו',
    "is_male": True,
    "birth_year": 2005,
    "description": 'הזהזהזהזהזהההזהזהזהזזזזזזזז',
    },
    7: {
    "first_name": 'בג',
    "last_name": 'חח',
    "is_male": True,
    "birth_year": 2006,
    "description": 'חחחחחחחחחחחחחחחחחחחחחחחחחחחחחחחחחחחחחח',       
    },
    8: {
    "first_name": 'בג',
    "last_name": 'חח',
    "is_male": True,
    "birth_year": 2007,
    "description": 'חחחחחחחחחחחחחחחחחחחחחחחחחחחחחחחחחחחחחח', 
    }
}

messages_data_structure: list[message_type] = {
    7: [
            {
                "message_id": 1,
                "message_text": 'היה חשמונאי',
                "is_liked": True,
            },
            {
                "message_id": 11,
                "message_text": 'מי לה׳-אלי',
                "is_liked": False,
            },
            {
                "message_id": 18,
                "message_text": 'נכה ביוונים',
                "is_liked": True,
            },
            {
                "message_id": 23,
                "message_text": 'נארוב לפילים',
                "is_liked": False,
            }
        ],
    8: [
            {
                "message_id": 2,
                "message_text":'צא ולמד',
                "is_liked": False,
            }
        ],
    9: [
            {
                "message_id": 3,
                "message_text": 'הגע בנפשך עד היכן',
                "is_liked": False,
            },
            {
                "message_id": 12,
                "message_text": 'התבוא אלי?',
                "is_liked": False,
            },
            {
                "message_id": 19,
                "message_text": 'שומר נפשו',
                "is_liked": True,
            },
            {
                "message_id": 24,
                "message_text": 'תודה',
                "is_liked": False,
            },
            {
                "message_id": 26,
                "message_text": 'בבקשה',
                "is_liked": False,
            }
        ],
}

friends_data_structure: list[friends_type] =  {
    1: [2,4,6,8,10,21,23,25],
    2: [1,3,4,7,9,11,13,15],
    3: [1,2,4,25,24],
    4: [25,22,13,11,9,8,6],
    5: [6,9,17,18,19,24],
    6: [4,5,7,11,12,15,17,20],
    7: [25],
    8: [1,7],
    9: [22,25,17,16,19,9,5],
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
    25: [24]
}

likes_data_structure: likes_type = [1,4,8,15,18,21,25]