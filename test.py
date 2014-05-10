import lastfm

API_KEY = "d31c87e698b2ed7c59ad765cd8df374e"
API_SECRET = "7dc01725c28bd38e5fbbaad57aab99dc"
TEST_URL = "http://ws.audioscrobbler.com/2.0/"
TEST_PARAMS = {"method": "tag.getsimilar", "tag": "disco"}
TEST_PARAMS_ERROR = {"method": "tag.getsimilr", "tag": "disco"}
lfm = lastfm.LastFM(api_key=API_KEY)

print lfm.search_artists("Metallica")