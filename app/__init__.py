from flask import Flask, render_template, send_file
from flask_restful import Api
from datetime import datetime
import json, jinja2
import pytz

app = Flask(__name__)
api = Api(app)

app.config.update({
    'website_name': 'Title on landing page',
    'website_desc': 'Subtitle below this title ^',
    'name': 'Your name/publishing name',
    'timezone': pytz.timezone('America/Chicago'), # ENTER YOUR TIMEZONE HERE
    'secret_key': 'random-key-here', # PUT A SECRET KEY TO UPLOAD WITH, MAKE IT RANDOM TO INCREASE SECURITY!
    'base_url': 'https://blog.myblog.com', # DOMAIN THE BLOG/API WILL BE RUNNING ON
    'web_title': 'My Blog' # TITLE FOR HTML IN THE TAB
})


@app.route('/', methods=['GET'])
def index():
    blog_posts = ""
    with open('app/db/posts.json', 'r+') as json_file:
        post_obj = json.load(json_file)
        for k in post_obj['posts']:
            for k1, v1 in k.items():
                blog_posts += v1['home_html'] + "<br>"
    if blog_posts == "":
        return render_template('home.html', blog_title=app.config['website_name'], website_desc=app.config['website_desc'], card_contents="<center><h1>Sorry no blog posts yet!</h1></center>", base_url=app.config['base_url'], web_title=app.config['web_title']), 200
    else:
        return render_template('home.html', blog_title=app.config['website_name'], website_desc=app.config['website_desc'], card_contents=blog_posts, base_url=app.config['base_url'], web_title=app.config['web_title']), 200

@app.route('/assets/<folder>/<file>', methods=['GET'])
def asset_handler(folder, file):
    return send_file('templates/assets/{}/{}'.format(folder, file)), 200

@app.route('/blog/<direct_url>', methods=['GET'])
def direct_link(direct_url):
    with open('app/db/posts.json', 'r+') as json_file:
        post_obj = json.load(json_file)
        found = False
        for k in post_obj['posts']:
            for k1, v1 in k.items():
                if k1 == direct_url:
                    found = True
                card_obj = v1
        if not found:
            return render_template('404.html', base_url=app.config['base_url'], web_title=app.config['web_title'])
        json_file.close()       
    return render_template('single.html', card_contents=card_obj['card_html'], base_url=app.config['base_url'], web_title=app.config['web_title'])

@app.route('/panel', methods=['GET'])
def load_panel():
    return render_template('panel.html', web_title=app.config['web_title'], base_url=app.config['base_url'])

from app.resources import Upload

api.add_resource(Upload, '/upload')