from flask import Flask
app = Flask(__name__)


@app.route('/')
def Title():
    return "Bollywood Hangaroo!"

if __name__ == '__main__':
    app.run()
