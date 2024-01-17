import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Erstelle ein SQLite-Datenbank-Engine (Ändere den Datenbank-URL für deine Datenbank)
engine = create_engine('sqlite:///example.db', echo=False)

# Erstelle eine "Base" Klasse als Basis für ORM-Modelle
# Definiere ein ORM-Modell für die Tabelle 'users'
Base = sqlalchemy.orm.declarative_base()

class Spielstand(Base):
    __tablename__ = "spielstand"
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    spieler_x = Column(Integer)
    spieler_0 = Column(Integer)


# Erstelle die Tabelle im Datenbank-Schema
Base.metadata.create_all(engine)

# Erstelle eine Session-Fabrik
Session = sessionmaker(bind=engine)
session = Session()


aktueller_spielstand = session.query(Spielstand).filter(Spielstand.id == 1).first()

if not aktueller_spielstand:
    spielstand_erstellen = Spielstand(id = 1, spieler_x=0, spieler_0=0)
    session.add(spielstand_erstellen)
    session.commit()

aktueller_spielstand = session.query(Spielstand).filter(Spielstand.id == 1).first()


print(f"Spielstand aktuell\n Spieler X: {aktueller_spielstand.spieler_x} Spieler 0: {aktueller_spielstand.spieler_0}")

aktueller_spielstand.spieler_0 = 50
aktueller_spielstand.spieler_x = 100
session.commit()

