from pecan import expose

class BooksController(object):
    @expose()
    def index(self):
        return "Welcome to book section."

    @expose()
    def bestsellers(self):
        return "We have 5 books in the top 10."

class CatalogController(object):
    @expose()
    def index(self):
        return "Welcome to the catalog."

    books = BooksController()

class RootController(object):
    @expose()
    def index(self):
        return "Welcome to store.example.com!"

    @expose()
    def hours(self):
        return "Open 24/7 on the web."

    catalog = CatalogController()

    @expose('json')
    @expose('text_template.mako', content_type='text/plain')
    @expose('html_template.mako')
    def hello(self):
        return {'msg': 'Hello!'}

    @expose('json')
    def hello(self):
        response.status = 201
        return {'foo': 'bar'}

    @expose()
    def _default(self):
        return 'I cannot say hello in that language'

    @expose('json')
    def hello(self):
        abort(404)
