from sqlalchemy import Column, Integer, String

from .db import db


class Ders(db.Model):
    __tablename__ = "dersler"

    ders_id = Column(Integer, primary_key=True)
    ders_adi = Column(String)
    ders_saati = Column(String)
