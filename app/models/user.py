from app.extentions import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return "<{} {}>".format(self.__class__.__name__, self.username)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def to_dict(self):
        d = {}
        for c in self.__table__.columns:
            d[c.name] = str(getattr(self, c.name))
        return d