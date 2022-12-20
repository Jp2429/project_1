from flask import Flask, render_template
from controllers.books_controller import books_blueprint
from controllers.authors_controller import authors_blueprint
from controllers.authors_books_controller import ab_blueprint

app = Flask(__name__)
app.register_blueprint(books_blueprint)
app.register_blueprint(authors_blueprint)
app.register_blueprint(ab_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)