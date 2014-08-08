from pyramid import testing


class TestView(object):

    def setup(self):
        self.config = testing.setUp()

    def teardown(self):
        testing.tearDown()

    def test_view(self):
        from tdf.views import HomeViews

        request = testing.DummyRequest()
        inst = HomeViews(request)
        response = inst.home()
        assert response.status_code == 200


class TestFunctional(object):

    def setup(self):
        from tdf import main
        app = main({})
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=200)
        assert b'Hello World' in res.body
