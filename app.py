from flask import Flask, render_template
import json

app = Flask(__name__)

def load_data():
    data_path = "data/blog_posts.json"

    with open(data_path, "r") as json_data:
        content = json_data.read()
        data = json.loads(content)
        return data

@app.route('/')
def index():
    blog_posts = load_data()
    # add code here to fetch the job posts from a file
    return render_template('index.html', posts=blog_posts)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)