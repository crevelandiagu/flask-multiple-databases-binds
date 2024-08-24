from app import create_app, setup_database

app = create_app()

if __name__ == "__main__":
    setup_database(app)
    app.run(port=3000, debug=True, use_reloader=False)

