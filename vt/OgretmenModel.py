from sqlalchemy import Column, Integer, String

from vt.baglanti import vt


class Ogretmen(vt.baglanti):
    __tablename__ = 'ogretmenler'

    ogretmen_id = Column(Integer, primary_key=True)
    ogretmen_adi = Column(String)
    ogretmen_soyadi = Column(String)
