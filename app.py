from flask import Flask
import click
app = Flask(__name__)
username = 'guest'

@click.command()
@click.option('--name', default='guest', prompt='Your name', help='The person to play.')
def greet(name):
    """Simple program that greets NAME"""
    global username
    click.echo('Hello %s! Let the game begins...'% name)
    username = name
    app.run()

@app.route('/')
def Title():
    return ("Hi %s! Let the game begins..."% username)

if __name__ == '__main__':
    greet()
