from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hghhhh')
def home():
    return jsonify({"message": "HELLO LEVEL 400 FET,QUALITY ASSURANCE!"})

if __name__ == '__main__':
    app.run()