from flask import Flask, render_template, flash, redirect
from config import Config
from flask_migrate import Migrate
from extensions import db
from models import Participant

from forms import ParticipantForm


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/', methods=['GET', 'POST'])
def index():  # put application's code here
    form = ParticipantForm()
    if form.validate_on_submit():
        print('Данные занесены в БД')
        participant = Participant()
        participant.name = form.name
        participant.surname = form.surname
        db.session.add(participant)
        db.session.commit()
        print(Participant.query.all())
        return redirect('/')
    return render_template('index.html', title='Колесо Фортуны', form=form)


if __name__ == '__main__':
    app.run()
