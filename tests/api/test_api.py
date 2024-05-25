import requests


class TestHttpChecks:

	def test_http_ok_on_root_page(self):
		assert requests.get("http://127.0.0.1:5000/").status_code == 200