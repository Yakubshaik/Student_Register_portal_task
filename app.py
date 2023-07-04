import os
from flask import Flask,redirect,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

basedir = os.path.abspath(__file__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)
Migrate(app,db)

class Registration(db.Model):
    __tablename__ = 'Registration'
    id = db.Column(db.Integer,primary_key = True)
    Name = db.Column(db.String)
    Collegename  = db.Column(db.String)
    Roll_No = db.Column(db.Integer)
    def __init__(self,Name,Collegename,Roll_No):
        self.Name = Name
        self.Collegename = Collegename
        self.Roll_No = Roll_No
    def __repr__(self):
        return "Your Regisration details are :{} {} {} ".format(self.Name,self.Collegename,self.Roll_No)

@app.route('/', methods=["POST","GET"])
def home():
    global Name,Collegename,Roll_No
    Name = request.form.get('Name')
    Collegename = request.form.get('Collegename')
    Roll_No = request.form.get('Roll_No')
    
    
    register = Registration(Name=Name,Collegename=Collegename,Roll_No=Roll_No)
    db.create_all()
    db.session.add(register)
    db.session.commit()
    
    return render_template('index.html')



@app.route('/display',methods = ['GET'])
def display_all():
    data = Registration.query.order_by(Registration.id).first()
    return render_template('display.html',data=data)



if __name__ == '__main__':
    app.run(debug=True)