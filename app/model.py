from sqlalchemy import Column, Integer, String, DateTime, select, func

from database import BASE, Database
from object import Question as QuestionObject


class Question(BASE):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True, nullable=False)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    request_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)

    @staticmethod
    async def get_last_request_id(*, database: Database) -> int:
        async with database.make_session() as session:
            stmt = (select(func.max(Question.request_id)))
            last_request_id = await session.scalar(stmt)
        return 0 if last_request_id is None else last_request_id

    @staticmethod
    async def get_by_request_id(*, request_id: int, database: Database) -> list["Question"]:
        async with database.make_session() as session:
            stmt = (select(Question).
                    where(Question.request_id == request_id))
            questions = await session.scalars(stmt)
        return questions.fetchall()

    @staticmethod
    async def check_existing(*, id: int, database: Database) -> bool:
        async with database.make_session() as session:
            stmt = (select(Question).
                    where(Question.id == id))
            last_request_id = await session.scalar(stmt)
        return last_request_id is not None

    @staticmethod
    async def create(*, question_object: QuestionObject, request_id: int, database: Database) -> None:
        async with database.make_session() as session:
            question_object.created_at= question_object.created_at.replace(tzinfo=None)
            session.add(Question(**question_object.dict(), request_id=request_id))
            await session.commit()
