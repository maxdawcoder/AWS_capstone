from app import get_or_create_app

if __name__ == "__main__":
    app = get_or_create_app()
    app.run(debug=True, port=5000)
