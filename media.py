#!env/bin/python

import webbrowser

class Movie():
    def __init__(self, _title, _storyline, _poster, _youtube):
        self.title = _title
        self.storyline  = _storyline
        self.poster_image_url = _poster
        self.trailer_youtube_url = _youtube

    def ShowTrailer():
        webbrowser.open(self.trailer_youtube_url)

if __name__ == '__main__':
    print 'works'
