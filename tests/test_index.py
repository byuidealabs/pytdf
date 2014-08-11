"""
Tests the index view, making sure that angular is wired together properly
and ready run tdf.
"""
from pyramid import testing


class TestView(object):
    """
    Tests the IndexView class to ensure that it is sending the proper data
    to the view itself.
    """

    def setup(self):
        self.config = testing.setUp()

    def teardown(self):
        testing.tearDown()

    def test_view(self):
        from tdf.app.views.index_view import IndexView

        request = testing.DummyRequest()
        inst = IndexView(request)
        response = inst.index()
        assert 'Hello World' == response['body']


class TestFunctional(object):
    """
    Performs a functional test on the index view to ensure that the right
    content is seen on the page.
    """

    def setup(self):
        from tdf import main
        mysqlurl = 'mysql+pymysql://tdf:markowitz@localhost:3306/test-tdf'
        settings = {  # TODO have a better way of doing this, don't use mysql
            'auth.secret': 'secret',
            'sqlalchemy.url': mysqlurl
        }
        app = main({}, **settings)
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=200)
        assert b'Hello World' in res.body


class TestDependencyLoading(object):
    """
    Ensures that the page can load all of the proper dependencies.
    """

    def setup(self):
        self.config = testing.setUp()
        self.config.add_static_view('public', 'tdf:public')

    def teardown(self):
        testing.tearDown()

    def test_dependencies(self):
        """
        Tests the plugin dependencies (angular.js, jquery, twitter bootstrap,
        etc)
        """
        from tdf.app.views.index_view import IndexView

        request = testing.DummyRequest()
        inst = IndexView(request)
        dependencies = {k: v for k, v in inst.dependencies}

        assert 'angular' in dependencies
        assert 'angular.min.js' in dependencies['angular']['js']

        assert 'bootstrap' in dependencies
        assert 'dist/js/bootstrap.min.js' in dependencies['bootstrap']['js']
        assert 'dist/css/bootstrap.min.css' in dependencies['bootstrap']['css']

        assert 'jquery' in dependencies
        assert 'dist/jquery.min.js' in dependencies['jquery']['js']

    def test_stylesheets(self):
        """
        Tests the tdf stylesheets in public/css/.
        """
        from tdf.app.views.index_view import IndexView

        request = testing.DummyRequest()
        inst = IndexView(request)
        stylesheets = inst.stylesheets

        assert 'common.css' in stylesheets

    def test_js(self):
        """
        Tests the tdf javascript in public/js/.
        """
        from tdf.app.views.index_view import IndexView

        request = testing.DummyRequest()
        inst = IndexView(request)
        scripts = inst.scripts

        assert 'app.js' in scripts
        assert 'init.js' in scripts
        assert 'controllers/header.js' in scripts
