import argparse
import logging
from rtrfm2spot.rtrfm_tools import scrape_rtrfm_show
from rtrfm2spot.spotify_tools import (
    authenticate_spotify,
    search_spotify,
    create_spotify_playlist,
)

SHOWTITLES = {
    "allcity": "All City",
    "basscheck": "Bass Check",
    "behindthemirror": "Behind the Mirror",
    "blackandblue": "Black and Blue",
    "criticalmass": "Critical Mass",
    "difficultlistening": "Difficult Listening",
    "drivetime": "Drivetime",
    "fullfrequency": "Full Frequency",
    "giantsteps": "Giant Steps",
    "globalrhythm": "Global Rhythm Pot",
    "goldenapples": "Golden Apples of the Sun",
    "homegrown": "Homegrown",
    "peer2peer": "peer2peer",
    "rhythmtrippin": "Rhythm Trippin'",
    "rockrattleandroll": "Rock Rattle and Roll",
    "saturdayjazz": "Saturday Jazz",
    "sundaymorning": "Sunday Morning Coming Down",
    "uplate": "Up Late",
}  # TODO Mostly predicted by copilot, double check

parser = argparse.ArgumentParser(
    description="Create a Spotify playlist from an RTRFM show tracklist"
)
parser.add_argument("show_url", type=str, help="URL of the show to process")


def process_show(show_url: str) -> None:
    """Scrape track list from a show-episode on RTRFM"""
    logger = logging.getLogger("rtrfm_log")
    if "show-episode" not in show_url:
        raise ValueError(
            "Must specify a specific show with date in url (press previous)"
        )

    artist_track_list = scrape_rtrfm_show(show_url)
    num_tracks = len(artist_track_list)
    logger.info(f"Read {num_tracks} tracks from {show_url} tracklist")

    try:
        import rtrfm2spot.spotify_tokens as tokens
    except ImportError:
        raise ImportError("Please add your tokens rtrfm2spot/spotify_tokens.py")

    spot = authenticate_spotify(tokens)

    tracks = []
    for artist_track in artist_track_list:
        tracks.append(search_spotify(spot, artist_track))

    # spotify track ids are 22 chars long
    missing = [id for id in tracks if len(id) != 22]
    track_ids = [id for id in tracks if len(id) == 22]

    logger.info(f"I think I Found {len(track_ids)} / {num_tracks} tracks on Spotify")

    playlist_id = create_spotify_playlist(
        SHOWTITLES, spot, show_url, found=track_ids, total=num_tracks, missing=missing
    )

    spot.playlist_add_items(playlist_id, track_ids)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("rtrfm_log")
    args = parser.parse_args()
    process_show(show_url=args.show_url)
