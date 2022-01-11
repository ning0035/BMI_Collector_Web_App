from flask import Flask, render_template, request
from flask_sqlalchemy import _EngineDebuggingSignalEvents, SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/calculate BMI'
db = SQLAlchemy(app)

class Data(db.Model):
    __tablesname__ = "BMI"
    id = db.Column(db.Integer, primary_key = True)
    email_ = db.Column(db.String(120), unique = True)
    weight_ = db.Column(db.Float)
    height_ = db.Column(db.Float)
    BMI_ = db.Column(db.Float)

    def __init__(self, email_, weight_, height_, BMI_):
        self.email_ = email_
        self.weight_ = weight_
        self.height_ = height_
        self.BMI_ = BMI_

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods = ['POST'])
def success():
    if request.method == 'POST':
        email = request.form["email_name"]
        weight = request.form["weight_name"]
        height = request.form["height_name"]
        BMI = float(weight) / float(height) / float(height)
        BMI = round(BMI, 1)
        print (Data.email_) 
        if db.session.query(Data).filter(Data.email_ == email).count() == 0:
            data = Data(email, weight, height, BMI)
            db.session.add(data)
            db.session.commit()
            average_BMI = db.session.query(func.avg(Data.BMI_)).scalar()
            average_BMI = round(average_BMI, 1)
            count = db.session.query(Data.BMI_).count()
            send_email(email, BMI, average_BMI, count)
            return render_template("success.html")
        else:
            return render_template("index.html", 
            text = "We've got the BMI information from this email address already")

if __name__ == '__main__':
    app.debug = True
    app.run()