# Load Package
from sqlalchemy.orm import sessionmaker
from models import engine, createTables, User

Session = sessionmaker(engine)
session = Session()


input("資料庫模型建立資料表，請按 Enter 繼續。")
createTables()

input("新增一筆資料，請按 Enter 繼續。")
# 新增一筆資料
user = User("Kevin")
session.add(user)
try:
    session.commit()
    print("新增資料成功")
except Exception as e:
    print("新增失敗")
    print(e)

input("新增多筆資料，請按 Enter 繼續。")
# 新增多筆資料
users = []
for idx in range(5):
    users.append(User(f"User{idx+1:02}"))
session.add_all(item for item in users)
try:
    session.commit()
    print("新增資料成功")
except Exception as e:
    print("新增失敗")
    print(e)

input("讀出所有資料，請按 Enter 繼續。")
# 讀出所有使用者資料
users = session.query(User).all()
print(f"Users: {users}")

input("讀出特定使用者資料，請按 Enter 繼續。")
# 對特定使用者印出其屬性
user = users[0]
print(f"User<id: {user.id}, name: {user.name}>")

input("讀出特定使用者資料方法2，請按 Enter 繼續。")
# 利用 id 取得特定使用者
user = session.query(User).get(1)
print(user)

input("讀出特定使用者資料方法3，請按 Enter 繼續。")
# 利用特定資訊取的使用者
users = session.query(User).filter_by(id=1).all()
print(f"By id >>> {users}")
user = session.query(User).filter_by(name="Kevin").all()
print(f"By name >>> {users}")

input("根據關鍵字取出使用者資料，請按 Enter 繼續。")
# 模糊查詢
users = session.query(User).filter(User.name.like('User%')).all()
print(users)

input("修改特定使用者資料，請按 Enter 繼續。")
# 修改資料
user = session.query(User).get(2)
print(user)
user.name = "NewName"
session.add(user)
try:
    session.commit()
    print("資料修改完成")
except Exception as e:
    print("資料修改失敗")
    print(e)
    session.rollback()
print(session.query(User).get(2))

input("刪除特定使用者資料，請按 Enter 繼續。")
# 刪除一筆資料
users = session.query(User).all()
print(users)
user = session.query(User).get(2)
print(user)
session.delete(user)
try:
    session.commit()
    print("資料刪除成功")
    users = session.query(User).all()
    print(users)
except Exception as e:
    print("資料刪除失敗")
    print(e)
    session.rollback()


session.close()