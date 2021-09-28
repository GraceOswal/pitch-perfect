from flask import render_template
from app import app

@app.errorhandler(404)
def 404(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('404.html')