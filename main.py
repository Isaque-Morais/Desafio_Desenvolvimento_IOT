from flask import Flask
app = notafiscal(__name__)

@app.route('/')
def teste_flask():
    return "teste!"
