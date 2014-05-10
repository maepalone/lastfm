"""Provides basic access to the last.fm API."""

#pylint: disable=R0921

import requests

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
        self.default_params = {"api_key": api_key, "format": "json"}
        self.BASE_URL = "http://ws.audioscrobbler.com/2.0/"

    def _authenticate(self):
        """Internal method to perform authentication with last.fm. Must be run
        before making requests that require authentication."""

        raise NotImplementedError("Authentication is not yet implemented.")

    def _request(self, params):
        """Given a url and dict of parameters, return the result of the request
        parsed from JSON to a dict."""
        params.update(self.default_params)
        response = requests.get(self.BASE_URL, params=params)
        response_dict = response.json()
        if DEBUG:
            print "Making request to %s" % response.url
            print "Status code: %s" % response.status_code
            if "error" in response_dict:
                print "Error returned by last.fm: %s" % response_dict["message"]
        return response_dict

    def search_artists(self, artist, **kwargs):
        """Makes a request to the artist.search API method."""
        params = {"artist": artist, "method": "artist.search"}
        params.update(kwargs)

        return self._request(params)

