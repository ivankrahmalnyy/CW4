from flask import Config, render_template, Flask

from project.config import config
from project.models import Genre, User, Director, Movie
from project.server import create_app, db

app = create_app(config)


@app.shell_context_processor
def shell():
    return {
        "db": db,
        "Genre": Genre,
        "User": User,
        "Director": Director,
        "Movie": Movie
    }

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.route('/')
    def index():
        return render_template('index.html')

if __name__ == '__main__':
    app.run(port=25000)


