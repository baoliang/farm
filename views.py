from flaskext.mako import render_template
from app import app
@app.route('/')
def index():
    '''
    @todo:index page:
    '''
    return render_template('index.html')
