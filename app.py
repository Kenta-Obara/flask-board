from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///post.db'
db = SQLAlchemy(app)

class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(30), nullable=False)
  description = db.Column(db.String(100), nullable=False)
  date = db.Column(db.DateTime, nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

  else:
    name = request.form.get('name')
    description = request.form.get('description')
    date = datetime.datetime.now()

    new_post = Post(name=name, description=description, date=date)

    db.session.add(new_post)
    db.session.commit()
    return redirect('/')

@app.route('/create')
def create():
  return render_template('create.html')

if __name__ == '__main__':
  app.run(debug=True)


