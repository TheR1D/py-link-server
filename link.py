from config import database
from model import Link, LinkSchema
from flask import redirect, abort

def open_link(link_id):
    link = Link.query.filter(Link.id == link_id).one_or_none()
    if link:
        link.view_count += 1
        database.session.commit()
        return redirect(link.original_url, code=301)
    abort(404, f"Link with id {link_id} not found.")

def create_link(link):
    schema = LinkSchema()
    new_link = schema.load(link, session=database.session)
    database.session.add(new_link)
    database.session.commit()
    data = schema.dump(new_link)
    return data, 201

