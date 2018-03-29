# edit the URI below to add your RDS password and your AWS URL

# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://(user):(password)@(db_endpoint)/(db_name)'

# Comment the line below if you want to work with a RDS account. Keep it as is for a local DB.
SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test2.db'


WTF_CSRF_ENABLED = True
SECRET_KEY = 'dsaf0897sfdg45sfdgfdsaqzdf98sdf0a'