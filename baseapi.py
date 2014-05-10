import requests
import json

DEBUG = True

class LastFM:
	"""Provides access to the LastFM API.

	api_key must be specified. api_secret must be specified to make requests
	that require authentication.
	"""
	def __init__(self, api_key=None, api_secret=None):
		if api_key:
			self.api_key = api_key
		else:
			raise ValueError("Must specify api_key.")

		self.api_secret = api_secret

	def _authenticate(self):
		raise NotImplementedError("Authentication is not yet implemented.")

	def _request(self, url, params=None):
		"""Given a url and dict of parameters, return the result of the request
		parsed from JSON to a dict."""

		r = requests.get(url, params=params)
		response_dict = r.json()
		if DEBUG:
			print "Making request to %s" % r.url
			print "Status code: %s" % r.status_code
			if "error" in response_dict:
				print "Error returned by last.fm: %s" % response_dict["message"]
		return response_dict

if __name__ == "__main__":
	API_KEY = "d31c87e698b2ed7c59ad765cd8df374e"
	API_SECRET = "7dc01725c28bd38e5fbbaad57aab99dc"
	TEST_URL = "http://ws.audioscrobbler.com/2.0/"
	TEST_PARAMS = {"method": "tag.getsimilar", "tag": "disco", "api_key": API_KEY, "format": "json"}
	TEST_PARAMS_ERROR = {"method": "tag.getsimilr", "tag": "disco", "api_key": API_KEY, "format": "json"}
	lastfm = LastFM(api_key=API_KEY)
	r = lastfm._request(TEST_URL, params=TEST_PARAMS)
	r_err = lastfm._request(TEST_URL, TEST_PARAMS_ERROR)