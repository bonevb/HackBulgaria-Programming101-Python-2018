from bs4 import BeautifulSoup
import requests
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
import re
# import matplotlib.pyplot as plt

Base = declarative_base()

class Page(Base):

    __tablename__ = 'page'
    id = Column(Integer, primary_key=True)
    server = Column(String)

engine = create_engine('sqlite:///page.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

request = requests.get('http://register.start.bg/')
cont = request.content
soup = BeautifulSoup(cont, "html.parser")

for link in soup.find_all('a'):
    try:
        url = link['href']
        # print(url)
        content = requests.get("http://register.start.bg/" + url)
        result = content.headers['Server']
        updated_result = result.split('/')[0]
        # updated_result = re.split(r'(;|/|\s)\s*', result)
        session.add_all([Page(server=updated_result)])
        session.commit()
        print(updated_result)
    except Exception:
        continue

h = dict()
invalid_keys = ['none', 'NULL']
servers = session.query(Page).all()
for server in servers:
    key = server.server.split('/')[0]
    if key not in invalid_keys:
        if key in h.keys():
            h[key] += 1
        else:
            h[key] = 1


# print(h)

# keys = list(h.keys())
# values = list(h.values())
#
# X = list(range(len(keys)))
#
# plt.bar(X, list(h.values()), align="center")
# plt.xticks(X, keys)
#
# plt.title(".bg servers")
# plt.xlabel("Server")
# plt.ylabel("Count")
#
# plt.savefig("histogram.png")

