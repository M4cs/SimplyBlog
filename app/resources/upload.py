from flask_restful import Resource, reqparse
from flask import redirect
from app import app
from datetime import datetime
from uuid import uuid4
import json, jinja2

blog_post_body = """\
          <div class="card">
            <div class="card-content">
              <div class="media">
                <div class="media-content">
                  <p class="title is-4">{title}</p>
                  <p class="subtitle is-6">{upload_date} by {name}</p>
                </div>
              </div>
              <div class="content">
                <hr>
                  {content}
              </div>
            </div>
          </div>"""
          
home_post_body = """\
          <div class="card">
            <div class="card-content">
              <div class="media">
                <div class="media-content">
                  <p class="title is-4"><a href="https://blog.maxbridgland.com/blog/{direct_url}">{title}</a></p>
                  <p class="subtitle is-6">{upload_date} by {name}</p>
                </div>
              </div>
              <div class="content">
                <hr>
                  {content}
              </div>
            </div>
          </div>"""

def upload_parser():
      parser = reqparse.RequestParser()
      parser.add_argument('t', help='Title of Blog Post', required=True, type=str)
      parser.add_argument('c', help='Content of Blog Post', required=True, type=str)
      parser.add_argument('s', type=str)
      return parser
          
class Upload(Resource):
    def post(self):
      parser = upload_parser()
      args = parser.parse_args()
      if not args.get('s'):
        return { 'error': 'Authorization failure.' }, 503
      title = args['t']
      content = args['c']
      upload_date = str(datetime.now(tz=app.config['timezone']).strftime('Published on %m/%d/%y at %H:%M EST'))
      uuid_split = str(uuid4()).split('-')
      direct_url = str(title.replace(' ', '+') + '_' + uuid_split[1])
      with open('app/db/posts.json', 'r+') as json_file:
        posts_obj = json.load(json_file)
        posts_obj['posts'].append({
          direct_url: {
            'title': title,
            'content': content,
            'upload_date': upload_date,
            'card_html': blog_post_body.format(title=title, upload_date=upload_date, content=content, name=app.config['name']),
            'home_html': home_post_body.format(title=title, upload_date=upload_date, content=content, name=app.config['name'], direct_url=direct_url)
          }
        })
        json_file.truncate()
        json_file.seek(0)
        json.dump(posts_obj, json_file, indent=4)
        json_file.close()
    
      return redirect('{}/blog/{}'.format(app.config['base_url'], direct_url))