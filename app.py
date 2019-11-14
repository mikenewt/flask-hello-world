from flask import Flask 

# create app object
app = Flask(__name__)

# error handling
app.config["DEBUG"] = True

# use decorator pattern to link view function to url
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string
def hello_world():
    return "Hello, world?!?!?!?!"

# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query

@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael" :
        return "Hello, {}".format(name), 200
    else:
        return "Not Found", 404

# start the dev server using run()
if __name__ == "__main__":
    app.run()