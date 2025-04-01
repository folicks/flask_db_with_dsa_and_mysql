
fastapi tutorial (irrelevant for now)
- using postman (demoing your api with http packets)
- use nginx with azure
- ci/cd with github actions
- does flask not have async support interacting with the db?!?!?
- fastapi will use pydantic







#### if sqlite prevents multiple copies of the db how/when are cilents made aware of the actual state


all ds's will be separate files and the actual api is one file

ORM : allow the sql to be access in an object i.e. programming language way

```
db = SQLAlchemy(app)
# this supposedly connects the app with the db with an assignment?

```
supposedly only needed 
- engine
- event 
to add features to sql directly






- this will decide the name of output db created using the models below

```python

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"


```




"blogpost model"







```python
user_id = db.Column(db.Integer,db.ForeignKey("user.id"),nullable=False)
```

**need this constraint in order forthe 2 tables(db.Model) to connect together a user matches to each post**



#### rember	to uninstall flask-alchemy NOT the same thing as flask_


since you had to do this

```python
from server import app,db
app.app_context()
```
it created a folder (in memory?)
where the file is nested just for referecne


recognize how the tables are just pages  
```
<f_string_BUT_with_parameter_from_function_below> 

```

200 is the status code for success

POST === CREATE DATA 








