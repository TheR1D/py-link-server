from secrets import token_urlsafe
from datetime import datetime
from urllib.parse import urlparse
from sqlalchemy.orm import validates
from config import database, marshmallow

def random_token():
    return token_urlsafe(nbytes=4)


class Link(database.Model):
    def __repr__(self):
        return ", ".join("%s: %s" % item for item in vars(self).items())

    id = database.Column(database.String, primary_key=True, default=random_token)
    original_url = database.Column(database.String(256), nullable=False)
    created_at = database.Column(database.DateTime, default=datetime.now(), nullable=False)
    view_count = database.Column(database.Integer, default=0, nullable=False)

    @validates("original_url")
    def url_validation(self, key, value):
        parsed_url = urlparse(value)
        if parsed_url.scheme not in ("http", "https") or not parsed_url.netloc:
            raise ValueError(f"URL Validation for {key} failed.")
        return value

class LinkSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Link
        sqla_session = database.session
        load_instance = True
