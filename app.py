from flask import Flask 

# create app object
app = Flask(__name__)

# use decorator pattern to link view function to url
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string
def hello_world():
    return "Hello, world!"

# start the dev server using run()
if __name__ == "__main__":
    app.run()