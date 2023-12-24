import wikipedia

def scrape(name="Microsoft", sentences=5):
    result = wikipedia.summary(name, sentences=sentences)
    return result
