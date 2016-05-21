import tmdbsimple as tmdb
tmdb.API_KEY = 'f2cdfa5d3850dac5c3e24acaf94394d6'

def get_data():
    title = []
    image = []

    discover = tmdb.Discover()
    response = discover.movie(sort_by='popularity.desc')
    for c in discover.results:
        title.append(c['title'])
        image.append('http://image.tmdb.org/t/p/w500'+c['poster_path'])
        
    return title,image 

