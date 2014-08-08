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
