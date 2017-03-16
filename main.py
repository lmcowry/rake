import webapp2, jinja2, os, re
from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

class SuperHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPageHandler(SuperHandler):
    def render_front(self, guessAt0="", guessAt1="", guessAt2="", guessAt3="", error=""):
        self.render("theModel.html", guessAt0=guessAt0, guessAt1=guessAt1, guessAt2=guessAt2, guessAt3=guessAt3, error=error)

    def get(self):
        self.render_front()

    def post(self):
        guessAt0 = self.request.get("guessAt0")
        guessAt1 = self.request.get("guessAt1")
        guessAt2 = self.request.get("guessAt2")
        guessAt3 = self.request.get("guessAt3")

        if guessAt0 and guessAt1 and guessAt2 and guessAt3:
            # need to make it add this
            self.render_front(guessAt0, guessAt1, guessAt2, guessAt3)
        else:
            error = "You didn't fucking enter something in one of these spots"
            self.render_front(guessAt0, guessAt1, guessAt2, guessAt3, error)

app = webapp2.WSGIApplication([
    ('/', MainPageHandler)
], debug=True)
