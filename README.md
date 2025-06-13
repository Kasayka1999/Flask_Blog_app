
# 📰 Flask Blog App

A simple and elegant blog web application using Flask. It allows users to create, read, update, and delete blog posts, with data stored in a JSON file. It uses HTML templates for rendering pages and CSS for styling.

---

## 🚀 Features

- 🏠 View all blog posts on the homepage
- 📝 Add new posts via a form
- ✏️ Edit and update existing posts
- ❌ Delete posts
- 💾 Store post data persistently in JSON format
- 🎨 Styled with a clean and responsive CSS layout

---

## 🗂 Project Structure

```
Flask_Blog_App/
├── app.py
├── data/
│   └── blog_posts.json
├── templates/
│   ├── add.html
│   ├── index.html
│   └── update.html
├── static/
│   └── style.css
└── README.md
```

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Kasayka1999/Flask_Blog_app.git
   cd Flask_Blog_app
   ```

2. **Create and activate a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask
   ```

4. **Run the app**
   ```bash
   python app.py
   ```

5. **View in browser**
   Open `http://127.0.0.1:5000` in your browser.

---

## 💡 Usage

- **Homepage** (`/`) shows all posts
- **Add** (`/add`) lets users submit new blog entries
- **Update** (`/update/<post_id>`) lets users edit a specific post
- **Delete** (`/delete/<post_id>`) removes a blog post

---

## 📁 Data Format (`blog_posts.json`)

Each blog post is a JSON object with:
```json
{
  "id": 0,
  "author": "Author Name",
  "title": "Post Title",
  "content": "Post content goes here..."
}
```

---

## 📜 License

MIT License
