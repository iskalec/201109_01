from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_tempaltre('index.html')

@app.route('/about-me')
def about():
    return render_tempaltre('about-me.html')

if __name__ == '__main__':
    app.run()
