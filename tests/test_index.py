# tests/test_index.py
from pyramid import testing


class TestView(object):

    def setup(self):
        self.config = testing.setUp()

    def teardown(self):
        testing.tearDown()

    def test_view(self):
        from tdf.app.views.index import IndexView

        request = testing.DummyRequest()
        inst = IndexView(request)
        response = inst.index()
        assert 'Hello World' == response['body']


class TestFunctional(object):

    def setup(self):
        from tdf import main
        app = main({})
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=200)
        assert b'Hello World' in res.body


class TestDependencyLoading(object):

    def setup(self):
        self.config = testing.setUp()
        self.config.add_static_view('public', 'tdf:public')

    def teardown(self):
        testing.tearDown()

    def test_dependencies(self):
        from tdf.app.views.index import IndexView

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
        from tdf.app.views.index import IndexView

        request = testing.DummyRequest()
        inst = IndexView(request)
        stylesheets = inst.stylesheets

        assert 'common.css' in stylesheets

    def test_js(self):
        from tdf.app.views.index import IndexView

        request = testing.DummyRequest()
        inst = IndexView(request)
        scripts = inst.scripts

        assert 'app.js' in scripts
        assert 'init.js' in scripts
        assert 'controllers/header.js' in scripts
