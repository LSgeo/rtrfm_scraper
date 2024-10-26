from bs4 import BeautifulSoup
import requests
import logging


def scrape_rtrfm_show(show_url: str) -> list:
    """Scrape tracklist from a RTRFM show page."""
    logger = logging.getLogger("rtrfm_log")
    logger.info(f"Scraping {show_url}")
    soup = BeautifulSoup(requests.get(show_url).text, "lxml")

    artist_track_list = []
    for div in soup.find_all("div", "flex flex-col gap-0.5"):
        # TODO Drop empty strings in list rather than use indices
        track = (div.text).split("\n")[2]
        artist = (div.text).split("\n")[4]
        if not track:
            logging.warning("No track title extracted from RTRFM")

        artist_track_list.append([artist, track])
    return artist_track_list
