from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy




class Config:
    
    def __init__(self):
        self.db = None
        
        
        
    def create_app(self):
        app = Flask(__name__)
        
        db = SQLAlchemy(app)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        
        app.config['s']
        
        
        return app
           


