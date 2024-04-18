db = db.getSiblingDB('moodle-statistics');

db.users.insertMany([
    {
        "name": "Иван",
        "surname": "Иванов",
        "lastname": "Иванович",
        "email": "ivan@mail.ru",
        "position": "admin",
        "password": "bhewrtfm3klmt3"
    },
    {
        "name": "Петров",
        "surname": "Петр",
        "lastname": "Петрович",
        "email": "petr@mail.ru",
        "position": "regular",
        "password": "bhewrsdfsdfsdwlmt3"
    },
    {
        "name": "Сидоров",
        "surname": "Федор",
        "lastname": "Федорович",
        "email": "fedor@mail.ru",
        "position": "regular",
        "password": "bhsdgdfgergef3klmt3"
    }
])

db.statistics.insertMany([
    {
        "student_id": 2,
        "student": "Диана Романенко",
        "email": "diana@mail.ru",
        "course": "Курс молодого бойца",
        "session": "123",
        "actions": [
            {
                "timestamp": new Date("2024-02-02T14:00:00"),
                "page": "http://e.moevm.info/some_course",
                "element_type": "button",
                "element_name": "сохранить",
                "action_type": "conversation",
                "event_type": "mousedown"
            }
        ]
    },
    {
        "student_id": 3,        
        "student": "Беззубов Даниил",
        "email": "daniil@mail.ru",
        "course": "Курс молодого бойца",
        "session": "1234",
        "actions": [
            {
                "timestamp": new Date("2024-02-02T14:00:00"),
                "page": "http://e.moevm.info/some_course",
                "element_type": "button",
                "element_name": "сохранить",
                "action_type": "conversation",
                "event_type": "mousedown"
            },
            {
                "timestamp": new Date("2024-02-02T14:00:00"),
                "page": "http://e.moevm.info/some_course",
                "element_type": "button",
                "element_name": "следующая страница",
                "action_type": "conversation",
                "event_type": "mousedown"
            }
        ]
    }
])

