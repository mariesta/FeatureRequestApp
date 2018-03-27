from flask import Flask, render_template, request, json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://usr:pass@localhost/sqlalchemy'
db = SQLAlchemy(app)

class Feature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    target_date = db.Column(db.Date, nullable=False)
    client = db.Column(db.Integer, nullable=False)
    product_area = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Feature %r>' % self.title

db.create_all()
db.session.commit()

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/createFeature', methods=['GET', 'POST'])
def createFeature():
    # read the posted values from the UI
    title = request.form['title']
    description = request.form['description']
    client = request.form['client']
    priority = request.form['priority']
    target = request.form['target']
    area = request.form['area']
 
    # validate the received values
    if title:
        new_feature  = Feature(
            title=title,
            description=description,
            priority=priority,
            target_date=target,
            client=client,
            product_area=area
        )
        db.session.add(new_feature)
        db.session.commit()
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})

if __name__ == "__main__":
    app.run()