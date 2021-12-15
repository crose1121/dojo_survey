from flask import Flask

app = Flask(__name__)
app.secret_key = 'shhh this is a secret'