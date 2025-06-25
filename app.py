from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calcio_di_strada.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# MODELLI DATABASE
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

class Interview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

class Highlight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

# CREA DATABASE CON DATI DI ESEMPIO SE NON ESISTE
with app.app_context():
    db.create_all()
    if not Article.query.first():
        db.session.add_all([
            Article(title="Il talento nascosto nei campetti di periferia", content="Scopriamo i giovani promettenti che stanno facendo parlare di sé nei tornei amatoriali."),
            Article(title="La rinascita del calcio di strada in Italia", content="Un ritorno alle origini: come il calcio di strada sta riconquistando il cuore dei tifosi.")
        ])
        db.session.add(
            Interview(title="Intervista con il bomber del quartiere", content="Parla il capocannoniere del torneo estivo di Milano Nord.")
        )
        db.session.add(
            Highlight(title="Top 5 gol della settimana", content="Una selezione delle migliori reti segnate nei campetti italiani.")
        )
        db.session.commit()
@app.route("/")
def home():
    articles = Article.query.all()
    interviews = Interview.query.all()
    highlights = Highlight.query.all()
    return render_template("index.html", articles=articles, interviews=interviews, highlights=highlights)

if __name__ == "__main__":
    app.run(debug=True)
