from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

path ="mysql+mysqldb://root:Uperflux28$@localhost/form"

database =create_engine(path)

Session = sessionmaker(bind=database)
session =Session()
