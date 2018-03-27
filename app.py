from flask import Flask, render_template, request, json, redirect, url_for
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
    client = db.Column(db.String(5), nullable=False)
    product_area = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Feature %r>' % self.title

db.create_all()
db.session.commit()

@app.route("/")
def main():
    features = Feature.query.order_by('-id').all()
    print(features)
    for feature in features:
        print(feature.title)
    return render_template('index.html', features=features)

@app.route('/createFeature', methods=['GET', 'POST'])
def createFeature():
    if request.method == 'POST':
        # read the posted values from the UI
        title = request.form['title']
        description = request.form['description']
        client = request.form['client']
        priority = int(request.form['priority'])
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

            # Feature for a specific client cannot have the same priority so re-order features' priorities if a new one
            # with the same priority is added
            priority_to_update = priority
            features_to_update_count = Feature.query.filter_by(client=client, priority=priority_to_update).count()
            while features_to_update_count > 1:
                feature_to_update = Feature.query.filter_by(client=client, priority=priority_to_update).order_by('id').first()
                feature_to_update.priority = feature_to_update.priority + 1
                priority_to_update = priority_to_update + 1
                features_to_update_count = Feature.query.filter_by(client=client, priority=priority_to_update).count()

            db.session.commit()
            return json.dumps({'html':'<span>All good</span>'})
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})
    elif request.method == 'GET':
        return render_template('createFeature.html')

if __name__ == "__main__":
    app.run()