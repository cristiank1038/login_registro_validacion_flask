from flask import Flask

app = Flask(__name__)

#Generar la secret_key  (se usa para guardar los datos que guardemos en sesion)
app.secret_key = "Esta es mi llave super secreta"