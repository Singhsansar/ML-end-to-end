import wikipedia

def scrape(name="Microsoft",length=5):
    return wikipedia.summary(name, sentences=length)
print(scrape("Python(Programming Language)",5))
