"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime
from collections import Counter
import operator

import lorem


def generate_chat_history():
    messages_amount = random.randint(10, 10)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


'''# 1. Вывести айди пользователя, который написал больше всех сообщений.
def most_talkative_person():
    users_id = []
    for message in generate_chat_history():
        users_id.append(message['sent_by'])
    id_with_most_posts_with_number = Counter(users_id).most_common(1)[0]
    id_with_most_posts = id_with_most_posts_with_number[0]
    number_of_messages_from_id = id_with_most_posts_with_number[1]
    return f'Пользователь {id_with_most_posts} написал больше всех сообщений: {number_of_messages_from_id}.'


# 2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
def most_responsed_id():
    replies = []
    user_id_with_message = {}
    id_with_number_of_messages = {}
    for message in generate_chat_history():
        user_id_with_message[str(message['id'])] = message['sent_by']
        if message['reply_for'] is not None:
            replies.append(str(message['reply_for']))
        id_with_number_of_messages[user_id_with_message.get(str(message['id']))] = 0

    for message in user_id_with_message:
        if message in replies:
            id_with_number_of_messages[user_id_with_message.get(message)] += 1
    id_with_most_responses = max(list(id_with_number_of_messages.items()), key=lambda i : i[1])[0]
    return f'Пользователь с id {id_with_most_responses} получил больше всего ответов.'''


# 3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
def most_seen_users():
    user_with_watched_users = {}
    for message in generate_chat_history():
        if message['sent_by'] not in user_with_watched_users:
            user_with_watched_users[message['sent_by']] = message['seen_by']
        else:
            user_with_watched_users[message['sent_by']] += message['seen_by']
    for users in user_with_watched_users:
        user_with_watched_users[users] = len(list(set(user_with_watched_users[users])))
    top_seen_users = list(dict(sorted(user_with_watched_users.items(), key=operator.itemgetter(1), reverse=True)).keys())[:3]
    top_seen_users = ', '.join(map(str, top_seen_users))
    return f'Пользователи, сообщения которых видело больше всего уникальных пользователей: {top_seen_users}'


if __name__ == "__main__":
    #print(most_talkative_person())  # 1
    #print(most_responsed_id())  # 2
    print(most_seen_users())  # 3