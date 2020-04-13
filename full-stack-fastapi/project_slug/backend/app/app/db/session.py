from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from app.core import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
# 在同一个线程中有scoped_session的时候，返回的是同一个session对象
# 在多线程下，即使通过scoped_session创建session，
# 每个线程下的session都是不一样的，每个线程都有一个属于自己的session对象，这个对象只在本线程下共享
# scoped_session 只有在单线程下才能发挥其作用，在多线程下显得没有什么作用
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)