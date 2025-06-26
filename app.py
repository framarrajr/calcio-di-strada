from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'
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

<<<<<<< HEAD
# CREA DATABASE CON DATI DI ESEMPIO SE NON ESISTE
with app.app_context():
=======
@app.before_request
def create_tables():
>>>>>>> 3ea457e (Aggiunto sistema login e pannello admin)
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
<<<<<<< HEAD
=======

# HOME
>>>>>>> 3ea457e (Aggiunto sistema login e pannello admin)
@app.route("/")
def home():
    articles = Article.query.all()
    interviews = Interview.query.all()
    highlights = Highlight.query.all()
    return render_template("index.html", articles=articles, interviews=interviews, highlights=highlights)

# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if username == "admin" and password == "calcio2025":
            session['admin'] = True
            return redirect(url_for('admin'))
        else:
            return render_template("login.html", error="Credenziali errate.")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop('admin', None)
    return redirect(url_for('home'))

# ADMIN AREA
@app.route("/admin", methods=["GET", "POST"])
def admin():
    if not session.get('admin'):
        return redirect(url_for('login'))

    if request.method == "POST":
        if 'title' in request.form and 'content' in request.form:
            new_article = Article(title=request.form['title'], content=request.form['content'])
            db.session.add(new_article)
            db.session.commit()
            return redirect(url_for('admin'))

    articles = Article.query.all()
    return render_template("admin.html", articles=articles)

@app.route("/delete_article/<int:id>")
def delete_article(id):
    if not session.get('admin'):
        return redirect(url_for('login'))
    article = Article.query.get(id)
    db.session.delete(article)
    db.session.commit()
    return redirect(url_for('admin'))

if __name__ == "__main__":
<<<<<<< HEAD
    import os
=======
>>>>>>> 3ea457e (Aggiunto sistema login e pannello admin)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
