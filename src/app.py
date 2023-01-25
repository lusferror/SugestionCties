from flask import Flask
from routes import api
from flask_migrate import Migrate
from models import db

app = Flask(__name__)
app.register_blueprint(api)
app.config["SQLALCHEMY_DATABASE_URI"]="mysql+mysqlconnector://root:password@localhost:3306/s2g"
Migrate(app,db)
db.init_app(app)

if __name__=='__main__':
    app.run(port = 3000, debug= True)