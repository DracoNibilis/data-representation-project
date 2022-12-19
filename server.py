from flask import Flask
app = Flask(__name__, static_url_path='', static_folder='pages')

@app.route('/')
def index():
    return "OOO"

if __name__ == "__main__":
    app.run(debug=True)