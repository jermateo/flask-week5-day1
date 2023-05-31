from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html', name='Jeremy')

@app.route('/fav5')
def test():
    fav5 = ['Chris Brown', 'Jacquees', 'Young Thug', 'OHGEESY', 'Mike Sherm']
    return render_template('fav5.html', fav5=fav5)