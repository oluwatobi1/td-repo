import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

import os

uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"]= uri
else:
    app.config["SQLALCHEMY_DATABASE_URI"]='postgresql://tobi:1234@localhost:5432/todoapp'
# rest of connection code using the connection string `uri`


app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self) -> str:
        return f'<Todo {self.description}>'
        
db.create_all()



@app.route('/')
def index(): 
    return render_template("index.html", data = Todo.query.all())
