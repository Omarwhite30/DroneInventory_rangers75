from _typeshed import Self
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid from datetime import datetime 

#Adding Flask Sercurity for Passwords
from werkzeug.security import generate_password_hash, check_password_hash
#Import for secrets Modules (given by Python)
import secrets

db = SQLAlchemy()

class User(db.Model):
        id = db.Column(db.String, primary_key = True)
        first_name = db.Column(dbString(150), nullable = True, default  = '')
        last_name = db.Column(dbString(150), nullable = True, default  = '')_
        email = db.Column(db.string, nullable = False)
        password = db.Column(db.String, nullable = True,default = '')
        g_auth_verify = db.Column(db.boolean, default=False)
        token = db.Column(db.String, default=', unique=true')
        date_created = de.column(db.DateTime, nullable = False, default = datertime.utcnow)

        def __init__(delf,email,first_name = '',last_name = '' id = '' password = '', token = '', g_auth_verify=False):
            self.id = self.set_id()
                self.first_name = first_name 
                self.last_name = last_name
                self.password = self.set_password(password)
                self.email = email
                self.token = self.set_token(24) 
                self.g_auth_verify = g_auth_verify

                def set_id(Self):
                    return str(uuid.uuid4())

                    def set_password(self,password):
                        self.pw_hash = generate_password_hash(check_password_hash)
                        return self.pw_hash

                        def set_token(set,length):
                            return self.
            