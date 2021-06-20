from config import MYSQL_PASS, MYSQL_IP, MYSQL_PORT, MYSQL_DB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import  create_engine

Base = declarative_base()

conn_uri = "mysql+pymysql://root:%s@%s:%s/%s?charset=utf8"%(MYSQL_PASS,MYSQL_IP,MYSQL_PORT,MYSQL_DB)

engine = create_engine(
    conn_uri,
    max_overflow=2,
    pool_size=5,
    pool_timeout=30,
    pool_recycle=-1
)

Session = sessionmaker(bind=engine)
