from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

db = create_engine("sqlite:///mydatabase.db")

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    username = Column("username", String, unique=True, nullable=False)
    email = Column("email", String, unique=True, nullable=False)
    password_hash = Column("password_hash", String, nullable=False)

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"

class Book(Base):
    __tablename__ = 'books'

    bookstatus = (("pendente", "pendente"),("lendo", "lendo"),("lido", "lido"))
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    title = Column("title", String, nullable=False)
    author = Column("author", String, nullable=False)
    category = Column("category", String, nullable=False)
    user_id = Column("user_id", Integer, ForeignKey('users.id'), nullable=False)
    status = Column("status", String, default="pendente", nullable=False)

    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}', category='{self.category}', status='{self.status}')>"