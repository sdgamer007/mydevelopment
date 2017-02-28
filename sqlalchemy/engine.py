from sqlalchemy import engine,create_engine

Engine = create_engine('sqlite:///D:\my.db', echo=True)