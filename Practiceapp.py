from flask import Flask
app = Flask(__name__)
@app.route('/')
def HelloWorld():
    return 'Hello world'
if __name__ == "__main__":
    app.run(debug=True)

#Think of some simple code from which you could create a route. 
# Then try to create a new route implementing that logic.

app = Flask(__name__)
@app.route('/')
def test():
    return 'Test Test'
if __name__ == "__main__":
    app.run(debug=True)