from contextlib import contextmanager
from dataclasses import asdict
from typing import ContextManager

from abstracts.base_dal import BaseDAL

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, Session

from database.base import Base
from database.table_models.user_table_model import UserTableModel
from models.user import User


class SQLAlchemyDAL(BaseDAL):
    def __init__(self, connection_string: str):
        self._connection_string = connection_string
        self._engine = create_engine(connection_string)
        self._session_maker = sessionmaker(bind=self._engine)

        # Create a user table in database
        # If user table already exists, this does nothing
        Base.metadata.create_all(self._engine)

    @contextmanager
    def _session_scope(self) -> ContextManager[Session]:
        session = self._session_maker()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def query(self, query_terms_as_user_object: User):
        with self._session_scope() as session:
            query = session.query(UserTableModel)
            query = query.filter(UserTableModel.name.contains(query_terms_as_user_object.name))
            query = query.filter(UserTableModel.title.contains(query_terms_as_user_object.title))
            query = query.filter(UserTableModel.position.contains(query_terms_as_user_object.position))
            query = query.filter(UserTableModel.summary.contains(query_terms_as_user_object.summary))
            query = query.filter(UserTableModel.skills.contains(query_terms_as_user_object.skills))
            query = query.filter(UserTableModel.experience.contains(query_terms_as_user_object.experience))
            query = query.filter(UserTableModel.education.contains(query_terms_as_user_object.education))

            for result in query.all():
                my_user = self._convert_usermodel_to_user(result)
                yield my_user

    def add_user(self, user: User):
        user = self._convert_user_to_usermodel(user)

        with self._session_scope() as session:
            session.add(user)
            session.commit()
            return self._convert_usermodel_to_user(user)

    def _convert_user_to_usermodel(self, user: User):
        return UserTableModel(**(asdict(user)))

    def _convert_usermodel_to_user(self, usermodel: UserTableModel):
        user = User(name=usermodel.name,
                    title=usermodel.title,
                    position=usermodel.position,
                    summary=usermodel.summary,
                    skills=usermodel.skills,
                    experience=usermodel.experience,
                    education=usermodel.education)
        return user
