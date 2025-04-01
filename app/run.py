from app.init import Config


app = Config().create_app()

if __name__ == '__main__':
    app.run(debug=True)


