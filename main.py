import webapp2, jinja2, os, re
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)



app = webapp2.WSGIApplication([
    ('/', MainPageHandler)
], debug=True)
