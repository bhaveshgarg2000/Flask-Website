from enum import unique
from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class BackEnd(db.Model):
    Sno = db.Column(db.Integer,primary_key=True)
    Name = db.Column(db.String(55),nullable= False)
    Contact = db.Column(db.Integer,nullable= False)
    Email = db.Column(db.String(55),nullable= False)
    Message = db.Column(db.String(500),nullable= False)

    def __repr__(self)-> str:
        return f"{self.Name} - {self.Email}"





@app.route("/",methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        Name = request.form['Name']
        Contact = request.form['Contact']
        Email = request.form['Email']
        Message = request.form['Message']

        Backend = BackEnd(Name = Name ,Contact = Contact,Email =Email,Message =Message)
        db.session.add(Backend)
        db.session.commit()
        print("Name : ",request.form['Name'])
        print("Contact : ",request.form['Contact'])
        print("Email : ",request.form['Email'])
        print("Message : ",request.form['Message'])

    return render_template('index.html')
    



if __name__ == "__main__":
    app.run(debug=True, port =5000)