from sqlalchemy import Column, Integer, String

from .db import db


class Ogretmen(db.Model):
    __tablename__ = "ogretmenler"

    ogretmen_id = Column(Integer, primary_key=True)
    ogretmen_adi = Column(String)
    ogretmen_soyadi = Column(String)
