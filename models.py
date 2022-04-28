from extensions import db


class Participant(db.Model):
    __tablename__ = 'participants'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text())
    surname = db.Column(db.Text())

    def __repr__(self):
        return f'<Участник {self.name} {self.surname}>'
