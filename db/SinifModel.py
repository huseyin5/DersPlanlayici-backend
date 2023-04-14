from sqlalchemy import Column, Integer, String

from .db import db


class Sinif(db.Model):
    __tablename__ = "siniflar"

    sinif_id = Column(Integer, primary_key=True)
    sinif_adi = Column(String)
