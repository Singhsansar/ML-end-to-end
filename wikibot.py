from mylib.bot import scrape
import click

@click.command()
@click.option('--name', prompt='Wikipedia page to scrape', help='Web page to scrape.')
@click.option('--length', default= 5 , help='Number of sentences to scrape from Wikipedia.')
def scrapper(name, length):
    result = scrape(name, sentences=length)
    click.echo(click.style(f"{result}", fg="white"))

if __name__ == '__main__':
    scrapper()
