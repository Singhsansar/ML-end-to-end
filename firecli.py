import fire
from mylib.bot import scrape

# def cli_wiki(name="world"):
#     return "Hello %s !" % name

if __name__ == "__main__":
    fire.Fire(scrape)
