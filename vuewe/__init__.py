# import os
# import imp
# import os 
# import sys
# from django_app.wsgi import application
# sys.path(0, os.path.path.dirname(__file__))


# sys.path.insert(0, os.path.dirname(__file__))

# wsgi = imp.load_source('wsgi', 'passenger_wsgi.py')
# application = wsgi.application
import pymysql
pymysql.version_info = (1, 4, 2, "final", 0)
pymysql.install_as_MySQLdb()