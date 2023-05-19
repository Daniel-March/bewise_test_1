#  Bewise test task 1

## Инструкция по сборке
1. Перейти в директорию с файлом `docker-compose.yml`
2. Собрать сервис `$ docker compose build`
3. Запустить сервис `$ docker compose up -d`

## Примеры
###Первый запрос
```
url: http://127.0.0.1:8000/get_question
method: POST
body: {"questions_num": 5}
```
Ответ:
```json
{
    "questions": []
}
```
Список вопросов пуст, так как это первый запрос.

###Второй запрос
```
url: http://127.0.0.1:8000/get_question
method: POST
body: {"questions_num": 1}
```
Ответ:
```json
{
    "questions": [
        {
            "id": 152272,
            "question": "& the Blackhearts",
            "answer": "Joan Jett",
            "created_at": "2022-12-30T20:38:48.893000"
        },
        {
            "id": 7477,
            "question": "Sniffing out clues in TV's \"The Thin Man\", this wire-haired terrier seemed to think he was a bloodhound",
            "answer": "Asta",
            "created_at": "2022-12-30T18:40:37.156000"
        },
        {
            "id": 113415,
            "question": "Slang for \"to kiss\" or \"to make out\" is this external body part",
            "answer": "neck",
            "created_at": "2022-12-30T19:45:23.629000"
        },
        {
            "id": 126472,
            "question": "The British don't celebrate this U.S. holiday honoring a 1621 event, but they do have something called St. Swithin's Day",
            "answer": "Thanksgiving",
            "created_at": "2022-12-30T20:03:17.455000"
        },
        {
            "id": 189438,
            "question": "Stromboli",
            "answer": "<i>Pinocchio</i>",
            "created_at": "2022-12-30T21:30:49.986000"
        }
    ]
}
```
Список вопросов полученных при предыдущем запросе.