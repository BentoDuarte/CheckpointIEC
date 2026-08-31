from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Checkpoint para as aulas 1 2 e 3"

if __name__ == '__main__':
    app.run(debug=True)   