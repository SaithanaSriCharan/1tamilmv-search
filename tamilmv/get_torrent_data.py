from bs4 import BeautifulSoup
import requests
import json

def get_torrent_data(links,title):

    """
    Get Torrent & Magnet Links from Posts

    Args:
        list: The list contains all the posts/topic urls related to search title.

    Returns:
        dict: The dist contains status code, torrent/magnet links count & result (Name, Torrent link and Magnet links).

    """

    torrent = []
    count = 0

    for post in links:

        response = requests.get(post)
        soup = BeautifulSoup(response.text, "html.parser")
        result_area = soup.find_all('strong')

        for res_area in result_area:

            for links in res_area.find_all('a', href=True):

                try:

                    if links['data-fileext'] == 'torrent':

                        if title.lower() in links.find('span').text.lower():

                            torrent.append({"name": links.find('span').text,
                                        "torrent": links['href'],
                                        "magnet":links.find_next('a')['href']})
                            count = count + 1

                finally:

                    continue
    
    if count != 0:

        return json.dumps({"status_code": "200",
                "Torrents found": str(count),
                "result": torrent
                })
    
    else:

        return json.dumps({
            "status_code": "404",
            "message": "No Torrents Found with Title"  
        })