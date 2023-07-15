from bs4 import BeautifulSoup
import requests
import logging


def scrape_rtrfm_show(show_url: str) -> list:
    """Scrape tracklist from a RTRFM show page

    Tracks are nicely isolated in a artist-track div, but I just use
    the pre-generated 'google search this track' button.
    """
    logger = logging.getLogger("rtrfm_log")
    logger.info(f"Scraping {show_url}")
    soup = BeautifulSoup(requests.get(show_url).text, "lxml")

    artist_track_list = []
    for a in soup.find_all("a", "black button"):
        artist_track_list.append(
            (a.get_attribute_list("href")[0].split("="))[1].split("+")
        )
    return artist_track_list
