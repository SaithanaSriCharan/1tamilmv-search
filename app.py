# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
import json
from flask import Flask, render_template, request
from tamilmv import get_posts, get_torrent_data, init_request
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def index():

    return render_template('index.html')

@app.route('/search', methods = ['post'])
def search():

    title = request.form['title']
    res = init_request(title)

    if res['status_code'] == 200:

        links = get_posts(res)

        if len(links) > 0:
            data = get_torrent_data(links,title)
        else:
            data = {"status_code":"404","reason":"No Posts Found"}

    else:
        data = {"status_code": "404", "reason":res['reason']}

    data = str(data).replace("\'", "\"")
    data = json.loads(str(data))
    
    return render_template('/search.html', data=data)

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
