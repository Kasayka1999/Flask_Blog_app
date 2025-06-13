from os import WCONTINUED

from flask import Flask, render_template, request, redirect, url_for
import json



app = Flask(__name__)

data_path = "data/blog_posts.json"



def load_data(path):

    with open(path, "r") as json_data:
        content = json_data.read()
        data = json.loads(content)
        return data

def save_data(new_data):

    with open(data_path, "w") as filedata:
        json.dump(new_data, filedata, indent=4 )

def add_post(author, title, content):
    existing_posts = load_data(data_path)

    user_ids = {post["id"] for post in existing_posts}
    free_id = 0
    while free_id in user_ids:
        free_id += 1


    new_posts = { "id" : free_id,
                 "author": author,
                 "title": title,
                 "content": content
    }
    existing_posts.append(new_posts)
    save_data(existing_posts)

def delete_post(post_id):
    existing_posts = load_data(data_path)

    for post_index, post in enumerate(existing_posts):
        if post_id == post["id"]:
            existing_posts.pop(post_index)

    save_data(existing_posts)

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
        add_post(author, title, content)
        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    # Find the blog post with the given id and remove it from the list
    if request.method == 'POST':
        delete_post(post_id)
        return redirect(url_for('index'))
    # Redirect back to the home page
    return render_template('index.html', post_id=post_id)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5001, debug=True)