from bs4 import BeautifulSoup
import requests

def get_posts(response):

    """
    Get Posts link for Title in 1Tamilmv

    Args:
        dict: The result containing web page info.

    Returns:
        list: The list contains all the posts/topic urls related to search title.

    """

    links = []
    soup = BeautifulSoup(response['text'], "html.parser")
    result_count = soup.select('.ipsType_sectionTitle')[0].text
    
    if int(result_count.split()[1]) > 25:

        result_area = soup.find('ol', attrs={"data-role":"resultsContents"})

        for link in result_area.find_all('a', href=True):

            if '/forums/topic/' in link['href']:
                links.append(link['href'])

        max = int(soup.find('input', attrs={'placeholder':'Page number'}).get('max'))

        for page in range(2,max+1):

            url = str(response['url'])+'&page='+str(page)
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            result_area = soup.find('ol', attrs={"data-role":"resultsContents"})

            for link in result_area.find_all('a', href=True):

                if '/forums/topic/' in link['href']:
                    links.append(link['href'])

    else:

        result_area = soup.find('ol', attrs={"data-role":"resultsContents"})

        for link in result_area.find_all('a', href=True):

            if '/forums/topic/' in link['href']:
                links.append(link['href'])
                
    return list(set(links))