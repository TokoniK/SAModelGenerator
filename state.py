from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import *
import json

DatabaseTable = declarative_base()


class State(DatabaseTable):
    __tablename__ = u'states'

    # column definitions
    state_id = Column(INTEGER())
    name = Column(VARCHAR)
    country_id = Column(INTEGER())
    country_code = Column(VARCHAR)
    country_name = Column(VARCHAR)
    state_code = Column(VARCHAR)
    type = Column(VARCHAR)
    latitude = Column(REAL())
    longitude = Column(REAL())

    def to_json(self):
        obj = {
            'state_id': self.state_id,
            'name': self.name,
            'country_id': self.country_id,
            'country_code': self.country_code,
            'country_name': self.country_name,
            'state_code': self.state_code,
            'type': self.type,
            'latitude': self.latitude,
            'longitude': self.longitude,
        }
        return json.dumps(obj)
