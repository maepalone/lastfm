"""Provides a LastFMHelper class that gives some higher level functionality
than the basic request functions in lastfm.py."""

import lastfm

class LastFMHelper(lastfm.LastFM):
    """Subclass of lastfm.LastFM that provides higher level functionality."""
    def __init__(self, api_key=None, api_secret=None):
        lastfm.LastFM.__init__(self, api_key=api_key, api_secret=api_secret)

    def similar_artist_attrs(self, name=None, mbid=None, attrs=None, **kwargs):
        """Returns a list of lists containing the fields specified in attrs for
        each artist returned by a similar_artist() request."""
        if not attrs:
            raise ValueError("Must specify attributes to get.")
        raw_response = self.similar_artist(name=name, mbid=mbid, **kwargs)
        data = [[artist[attr] for attr in attrs] 
            for artist in raw_response["similarartists"]["artist"]]
        return data

    def first_search_id(self, artist):
        """Returns the MusicBrainz ID of the first artist search result."""
        raw_response = self.search_artists(artist)
        mbid = raw_response["results"]["artistmatches"]["artist"][0]["mbid"]
        return mbid