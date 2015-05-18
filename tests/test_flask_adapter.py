import unittest

from webtest import TestApp

from tests.example_app.api.resources import DateTimeResource
from tests.example_app.flask_app import create_pale_flask_app


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.flask_app = create_pale_flask_app()
        self.app = TestApp(self.flask_app)


    def test_successful_get_without_params(self):
        """Tests against success cases.

        Call the /current_time and /parse_time endpoints with the correct
        parameters to verify that they return HTTP 200 codes, and behave
        as expected in the successful case.
        """

        # note that `create_pale_flask_app` applies a prefix of /api to
        # the uris specified in the Pale endpoints.
        resp = self.app.get('/api/current_time/')
        self.assertEqual(resp.status_code, 200)

        # the 'time' value was set in the endpoint handler
        self.assertIn('time', resp.json_body)

        # the returned time value should match the resource defined
        # in tests.example_app.api.resources.py
        returned_time = resp.json_body['time'].copy()

        # no other fields were specified, so we should get only the
        # default fields
        expected_fields = DateTimeResource._default_fields

        for f in expected_fields:
            self.assertIn(f, returned_time)
            val = returned_time.pop(f)
            # don't check the val for now
        # make sure there's nothing left in the dict
        self.assertTrue(len(returned_time.keys()), 0)


    def test_successful_post_with_params(self):
        resp = self.app.post('/api/parse_time/', {'month': 2})
        self.assertEqual(resp.status_code, 200)
