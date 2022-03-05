# Load Package
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# 實例基礎模型
Base = declarative_base()


# 建立使用者模型
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<User {self.name}>"
