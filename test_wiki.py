from mylib.bot import scrape
from click.testing import CliRunner
from wikibot import scrapper


def test_scrape():
    assert "Microsoft" in scrape("Microsoft",5)

def test_wikibot():
    runner = CliRunner()
    result = runner.invoke(scrapper, ['--name', 'Microsoft', '--length', '1'])
    assert result.exit_code == 0
    assert 'Microsoft' in result.output

test_wikibot()