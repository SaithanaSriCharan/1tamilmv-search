from bs4 import BeautifulSoup
import requests

def init_request(search_title):

    """
    Initial Request for Title in 1Tamilmv

    Args:
        Title (str): Movie name.

    Returns:
        dict: The result containing web page info.

    Raises:
        httpx.RequestError: If an error occurs during the API request.
    """

    response = requests.get("https://www.1tamilmv.tf/index.php?/search/&q="+search_title+"&type=forums_topic&quick=1&search_and_or=and&search_in=titles&sortby=relevancy")

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, "html.parser")
        result_count = soup.select('.ipsType_sectionTitle')[0].text

        # No Posts Found for Title
        if int(result_count.split()[1]) == 0:

            response = {"status_code": "404","reason":"No Posts Found"}

            return response
        
        else:
            #Have some Posts
            return {"status_code":response.status_code,"reason":response.reason,"text":response.text,"url":response.url,"title":search_title}
    else:
        # Httpx Error
        return {"status_code":response.status_code,"reason":response.reason,"text":response.text}