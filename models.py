#encoding: utf-8
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    'mysql://root:wwwsunboy@127.0.0.1:3306/farm_dev?charset=utf8', 
    encoding = "utf-8",
    echo =True
)
Base = declarative_base(bind=engine)

class Info(Base):
    __tablename__ = 'info_struct'

    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True)
    def __repr__(self):
        return self.name

