# app.py
from flask import Flask, jsonify
from routes import bp
import datetime

app = Flask(__name__)
app.register_blueprint(bp)

@app.route('/api/healthz')
def health_check():
    return jsonify({
        "Status": "OK",
        "Version": "1.0.3",
        "Tempo": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "Author": "Uday",
    }), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')