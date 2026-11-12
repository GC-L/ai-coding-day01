from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

device_list = [
    {'name': 'R1', 'type': 'router', 'version': 'IOS XE 17.14', 'location': 'Beijing-IDC-A'},
    {'name': 'R2', 'type': 'router', 'version': 'IOS XE 17.14', 'location': 'Shanghai-IDC-B'},
    {'name': 'SW1', 'type': 'switch', 'version': 'IOS 15.2', 'location': 'Beijing-IDC-A'},
    {'name': 'SW2', 'type': 'switch', 'version': 'IOS 15.2', 'location': 'Shanghai-IDC-B'},
    {'name': 'FW1', 'type': 'firewall', 'version': 'ASA 9.16', 'location': 'Beijing-IDC-A'},
    {'name': 'FW2', 'type': 'firewall', 'version': 'FTD 7.2', 'location': 'Shenzhen-IDC-C'},
]

# 1. 连接数据库：SQLite 数据库就是当前目录下的一个文件
engine = create_engine("sqlite:///device_inventory.db")
Session = sessionmaker(bind=engine)
Base = declarative_base()


# 2. 定义表结构：一个类 = 一张表，一个类属性 = 一个字段
class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), index=True, nullable=False)
    type = Column(String(32), nullable=False)
    version = Column(String(64), nullable=False)
    location = Column(String(64), nullable=False)
    create_time = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return (f"Device(设备名称: {self.name} | 类型: {self.type} | 版本: {self.version} "
                f"| 位置: {self.location} | 入库时间: {self.create_time})")


# 3. 初始化：建表；只有表是空的时候才插入初始数据
def init_db():
    Base.metadata.create_all(engine)
    with Session() as session:
        if session.query(Device).count() == 0:
            for d in device_list:
                session.add(Device(**d))
            session.commit()
            print("数据库初始化成功，已写入 {} 条设备记录".format(len(device_list)))


def show(devices):
    if not devices:
        print("没有找到匹配的设备")
    for device in devices:
        print(device)


# 4. 菜单查询
def main():
    init_db()
    while True:
        print("\n请选择查询方式：")
        print("输入 1：查询所有设备")
        print("输入 2：根据设备名称查询")
        print("输入 3：根据设备类型查询")
        print("输入 4：根据机房位置查询")
        print("输入 0：退出")
        choice = input("请输入查询选项：").strip()

        with Session() as session:
            if choice == "1":
                show(session.query(Device).all())
            elif choice == "2":
                name = input("请输入设备名称：").strip()
                show(session.query(Device).filter_by(name=name).all())
            elif choice == "3":
                dev_type = input("请输入设备类型（router/switch/firewall）：").strip()
                show(session.query(Device).filter_by(type=dev_type).all())
            elif choice == "4":
                keyword = input("请输入机房位置关键词：").strip()
                show(session.query(Device).filter(Device.location.like(f"%{keyword}%")).all())
            elif choice == "0":
                print("已退出")
                break
            else:
                print("输入有误，请输入 0-4")


if __name__ == "__main__":
    main()