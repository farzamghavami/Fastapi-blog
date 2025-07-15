# 🚀 FastAPI Blog Project

A modern, clean, and extensible blog API built with [FastAPI](https://fastapi.tiangolo.com/) and [SQLAlchemy](https://www.sqlalchemy.org/).

---

## ✨ Features

- **User Registration & Login** with secure password hashing
- **JWT Authentication** for secure API access
- **Admin & Regular User Roles**
- **CRUD Operations** for blog posts
- **Only post owners or admins can edit/delete posts**
- **Threaded Comments**: Reply to posts and to other comments (nested)
- **Only authenticated users can create posts or comments**
- **Automatic API documentation** with Swagger (OpenAPI)

---

## 📁 Project Structure

```text
.
├── main.py                # FastAPI application entry point
├── database.py            # SQLAlchemy database setup
├── config.py              # Project configuration (optional)
├── requirements.txt       # Project dependencies
├── dependencies.py        # Auth & DB dependencies
├── models/
│   ├── __init__.py
│   ├── users.py           # User model
│   ├── posts.py           # Post model
│   └── comments.py        # Comment model
├── schemas/
│   ├── __init__.py
│   ├── users.py           # User schemas
│   ├── posts.py           # Post schemas
│   └── comments.py        # Comment schemas
├── routers/
│   ├── __init__.py
│   ├── users.py           # User routes
│   ├── posts.py           # Post routes
│   └── comments.py        # Comment routes
└── venv/                  # Python virtual environment
```

---

## ⚡️ Quick Start

1. **Clone the repository**
   ```bash
   git clone <REPO_URL>
   cd FastAPIProject
   ```
2. **Create a virtual environment & install dependencies**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Run the server**
   ```bash
   uvicorn main:app --reload
   ```
4. **API Documentation**
   - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🔐 Authentication & Permissions

- **JWT Token**: After login, use the returned token in the `Authorization` header as `Bearer <token>` for all protected endpoints.
- **Post Permissions**: Only the post owner or an admin can update or delete a post.
- **Commenting**: Only authenticated users can create comments or replies.
- **Admin Role**: Admin users can manage all posts.

---

## 🛠️ Dependencies

```
fastapi
uvicorn
sqlalchemy
pydantic
passlib[bcrypt]
python-jose
```

---

## 💡 Customization & Extensibility

- The project is designed for easy extension: add features like likes, categories, search, etc.
- All code is modular and follows best practices for FastAPI projects.

---

## 📜 License

This project is open-source and free to use for educational and development purposes.

---

## 👤 Developer

- **Your Name**
- [Your GitHub Profile](https://github.com/yourusername)

---

> Made with ❤️ using FastAPI & SQLAlchemy 