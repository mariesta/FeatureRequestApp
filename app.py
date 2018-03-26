from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://usr:pass@localhost/sqlalchemy'
db = SQLAlchemy(app)
db.create_all()
db.session.commit()


@app.route("/")
def main():
	return render_template('index.html')

if __name__ == "__main__":
	app.run()