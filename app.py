from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return f"""
    <h1>🚀 DevOps Demo App</h1>
    <p>Работает на Python {os.getenv('PYTHON_VERSION', '3.x')}</p>
    <p>Время деплоя: {os.getenv('DEPLOY_TIME', 'unknown')}</p>
    <p>Хост: {os.getenv('HOSTNAME', 'local')}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
