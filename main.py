from flask import flask, render_template
app = Flask(_name_)
@app.rout('/')
def home():
  # render_template automatically looks in the/ templates folder
  return render_template('index.html', title = "Home Page")
if __name__ == '__main__';
#Locel development server
app.run(host = '127.0.01', port = 8080, debug = True)
