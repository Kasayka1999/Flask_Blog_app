from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

data_path = "data/blog_posts.json"

def load_data(data_path):

    with open(data_path, "r") as json_data:
        content = json_data.read()
        data = json.loads(content)
        return data

@app.route('/')
def index():
    blog_posts = load_data(data_path)
    # add code here to fetch the job posts from a file
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        author = request.form.get('author', 'NoAuthor')
        title = request.form.get('title', 'NoTitle')
        content = request.form.get('content', 'NoContent')
        return redirect(url_for('index'))

    return render_template('add.html')

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)