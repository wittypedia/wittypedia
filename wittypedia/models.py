from wittypedia import db


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(64), index=True, unique=True)
    # email = db.Column(db.String(120), index=True, unique=True)
    # password_hash = db.Column(db.String(128))
    wiki_topic = db.Column(db.String(100), index=True)
    wiki_links = db.Column(db.PickleType, index=True)

    def __repr__(self):
        return '<WikiTopic {}>'.format(self.wiki_topic)