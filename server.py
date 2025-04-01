from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,request,jsonify,render_template

# Model and Engine are capitalized



TOYUSERS = [
    {
        "id" : 2,
        "name" : "Data analyst",
        "address" : "Bengaluru,India",
        "salary" : "10,00,000"
    
    },
    {
        "id" : 2,
        "name" : "Data scientist",
        "address" : "Delhi,India",
        "salary" : "1,00,000"
    
    },
    {
        "id" : 3,
        "name" : "Backend Engineer",
        "address" : "San Diego, California",
        "salary" : "10,00,000"
    
    },
    

]




app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"
# need this to prevent errors
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 0


# add the foreign key feature to sqlite3
@event.listens_for(Engine,"connect")
def _set_sqlite_pragma(dbapi_connection,connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

db = SQLAlchemy(app)
now = datetime.now()

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    posts = db.relationship("Blogpost")


class Blogpost(db.Model):
    __tablename__ = "blog_post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(200))
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"),nullable=False)



@app.route("/api/jobs")
def list_jobs():
    '''
    jovian is so goated 
    an api is just the back and forth over the internet of json
    '''
    return jsonify(TOYUSERS)





@app.route("/templates/index.html")
def index():
    return render_template("index.html",TOYUSERS=TOYUSERS)



# TODO 
# make a the functions below
# to receive input from the template 
# jsonify it
# add it to the database thru azure




@app.route("/user",methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = User(
        name=data["name"],
        email=data["email"],
        address=data["address"],
        phone=data["phone"],
    
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message":"User created"}),200


@app.route("/user/descending_id",methods=["GET"])
def get_all_users_descending():
    # how to read my data as a return type can this interact with 
    # vanilla python?
    pass

@app.route("/user/ascending_id",methods=["GET"])
def get_all_users_ascending():
    pass


@app.route("/user/<user_id>",methods=["GET"])
def get_one_user(user_id):
    pass


@app.route("/user/<user_id>",methods=["DELETE"])
def delete_user(user_id):
    pass


@app.route("/blog_post/<user_id>",methods=["POST"])
def create_blog_post(user_id):
    pass


@app.route("/user/<user_id>",methods=["GET"])
def get_all_blog_posts(user_id):
    pass

@app.route("/blog_post/<blog_post_id>",methods=["GET"])
def get_one_blog_post(blog_post_id):
    pass


@app.route("/blog_post/<blog_post_id>",methods=["DELETE"])
def delete_blog_post(blog_post_id):
    pass





# GOAL make linked list

if __name__ == "__main__":
    app.run(debug=True)