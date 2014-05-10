"""Provides a LastFMHelper class that gives some higher level functionality
than the basic request functions in lastfm.py."""

import lastfm

class LastFMHelper(lastfm.LastFM):
    def __init__(self, api_key=None, api_secret=None):
        lastfm.LastFM.__init__(self, api_key=api_key, api_secret=api_secret)

    def similar_artist_attrs(self, name=None, mbid=None, attrs=None, **kwargs):
        if not attrs:
            raise ValueError("Must specify attributes to get.")
        raw_response = self.similar_artist(name=name, mbid=mbid, **kwargs)
        data = [[artist[attr] for attr in attrs] 
            for artist in raw_response["similarartists"]["artist"]]
        return data
