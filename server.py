from flask_app import app

#Importando Controlador
from flask_app.controllers import users_controller

#Pasos a seguir:
#pipenv install pymysql flask-bcrypt
#pipenv shell
#python server.py -> python3, py o python

# Juana : 123456  
# Elena : 123456
# Pablo : Detodounpoc0

if __name__=="__main__":
    app.run(debug=True)