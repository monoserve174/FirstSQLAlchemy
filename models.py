# Load Package
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base


# 資料庫連接
pwd = input('請輸入資料庫密碼:')
db_config = {
    'drivername': 'mariadb+mariadbconnector',
    'username': 'kevin',
    'password': pwd,
    'host': '138.2.46.105',
    'port': '3306',
    'database': 'mypydb',
}
db_url = URL(**db_config)
engine = create_engine(url=db_url)


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


def createTables():
    try:
        print("資料表建立中...")
        engine.connect()
        Base.metadata.drop_all(engine)  # 清空所有表
        Base.metadata.create_all(engine)  # 建立所有表
        print("建立資料表完成")
    except Exception as e:
        print(e)
        print("連線失敗")