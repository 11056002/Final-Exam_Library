from django.apps import AppConfig
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_books/', methods=['GET', 'POST'])
def search_books():
    if request.method == 'POST':
        keyword = request.form['keyword']
        # 在這裡可以使用 keyword 進行一些處理...
        return render_template('results.html', keyword=keyword)
    return render_template('search_books.html')

if __name__ == '__main__':
    app.run(debug=True)

class MysiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mysite'
    


