import asyncio

import requests
import uvicorn
from fastapi import FastAPI
from fastapi.responses import Response
from pydantic import BaseModel

from database import Database
from model import Question as QuestionModel
from object import Question as QuestionObject

app = FastAPI()
database = Database()


class RequestData(BaseModel):
    questions_num: int


@app.post("/get_question")
async def get_question(data: RequestData):
    if data.questions_num <= 0:
        return Response(content="questions_num must be more than zero", status_code=422)
    questions: list[QuestionObject] = []
    for question in requests.get(f"https://jservice.io/api/random?count={data.questions_num}").json():
        questions.append(QuestionObject.parse_obj(question))
    last_request_id: int = await QuestionModel.get_last_request_id(database=database)
    for question in questions:
        while await QuestionModel.check_existing(id=question.id, database=database):
            question = requests.get(f"https://jservice.io/api/random?count=1").json()[0]
            question = QuestionObject.parse_obj(question)
        await QuestionModel.create(question_object=question, request_id=last_request_id + 1, database=database)
    questions = await QuestionModel.get_by_request_id(request_id=last_request_id, database=database)
    return {"questions": [QuestionObject.from_orm(question) for question in questions]}


if __name__ == "__main__":
    asyncio.run(database.connect(url="postgresql+asyncpg://postgres:password@database/postgres"))
    uvicorn.run(app, host="0.0.0.0", port=8000)
