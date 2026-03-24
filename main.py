from app import application

if __name__ == '__main__':
   #from waitress import serve
   #serve(app, host = "0.0.0.0", port = 3000)
   application().run(port=3000)