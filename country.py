from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import *
import json

DatabaseTable = declarative_base()


class Country(DatabaseTable):
    __tablename__ = u'countries'

    # column definitions
    country_id = Column(INTEGER(), server_default=text(''), primary_key=True, nullable=False)
    country_name = Column(VARCHAR, nullable=False)
    country_code = Column(VARCHAR, nullable=False)
    creation_date = Column(TIMESTAMP())
    update_date = Column(TIMESTAMP())
    created_by = Column(VARCHAR)
    updated_by = Column(VARCHAR)
    soft_deleted = Column(BOOLEAN())
    deleted_by = Column(VARCHAR)

    def to_json(self):
        obj = {
            'country_id': self.country_id,
            'country_name': self.country_name,
            'country_code': self.country_code,
            'creation_date': self.creation_date.strftime('%a, %d %b %Y %H:%M:%S +0000') if self.creation_date else None,
            'update_date': self.update_date.strftime('%a, %d %b %Y %H:%M:%S +0000') if self.update_date else None,
            'created_by': self.created_by,
            'updated_by': self.updated_by,
            'soft_deleted': self.soft_deleted,
            'deleted_by': self.deleted_by,
        }
        return json.dumps(obj)
