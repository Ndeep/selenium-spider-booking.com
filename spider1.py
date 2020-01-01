import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from bs4 import BeautifulSoup
import pandas as pd
import re
import json
def get_page(url,i,link_list=[]):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    for div in soup.find_all("a", {"class": "sr_item_photo_link sr_hotel_preview_track"}):
        #r = requests.get("https://www.booking.com/" + div['href'])
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        r=session.get("https://www.booking.com/" + div['href'])
        soup = BeautifulSoup(r.text, 'html.parser')
        s = soup.find('script', type='application/ld+json')
        dict1 = {}
        json_data = json.loads(s.text)
        if 'Zostel' in json_data['name']:
            dict1['name'] = json_data['name']
        else:
            dict1['name'] = json_data['name']
        dict1['url'] = json_data['url']
        dict1['description'] = json_data['description']
        dict1['addressCountry'] = json_data['address']['addressCountry']
        dict1['postalCode'] = json_data['address']['postalCode']
        dict1['addressRegion'] = json_data['address']['addressRegion']
        dict1['streetAddress'] = json_data['address']['streetAddress']
        dict1['addressLocality'] = json_data['address']['addressLocality']
        dict1['rating'] = json_data['aggregateRating']['ratingValue'] if json_data.get('aggregateRating',
                                                                                       None) is not None else None
        dict1['image'] = json_data['image']
        dict1['priceRange'] = json_data['priceRange'] if json_data.get('priceRange', None) is not None else None
        dict1['hasMap'] = json_data['hasMap']
        # dict1[soup.title.string.strip()] = json_data
        link_list.append(dict1)
        print(soup.title.string)
        print("***********************************")
    if i <40:
        get_page(
        'https://www.booking.com/searchresults.html?aid=356980&label=gog235jc-1DCAUobEIJbGFsLXF1aWxhSDNYA2hsiAEBmAExuAEXyAEM2AED6AEB-AECiAIBqAIDuALX_JfwBcACAQ&tmpl=searchresults&ac_click_type=b&ac_position=0&class_interval=1&dest_id=-2098033&dest_type=city&from_sf=1&group_adults=2&group_children=0&iata=JAI&label_click=undef&no_rooms=1&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&src=index&src_elem=sb&srpvid=2eef430f69340083&ss=Jaipur%2C%20Rajasthan%2C%20India&ss_raw=jaipur&ssb=empty&top_ufis=1&rows=25&offset={}'.format(
            i * 25), i + 1, link_list)
    print(link_list)
    df = pd.DataFrame(link_list)
    df.to_csv("jaipur_hotels.csv")

get_page('https://www.booking.com/searchresults.html?aid=356980&label=gog235jc-1DCAUobEIJbGFsLXF1aWxhSDNYA2hsiAEBmAExuAEXyAEM2AED6AEB-AECiAIBqAIDuALX_JfwBcACAQ&tmpl=searchresults&ac_click_type=b&ac_position=0&class_interval=1&dest_id=-2098033&dest_type=city&dtdisc=0&from_sf=1&group_adults=2&group_children=0&iata=JAI&inac=0&index_postcard=0&label_click=undef&no_rooms=1&postcard=0&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&src=index&src_elem=sb&srpvid=6d413d3f4ea200a5&ss=Jaipur%2C%20Rajasthan%2C%20India&ss_all=0&ss_raw=jaipur&ssb=empty&sshis=0&top_ufis=1&rows=25',1,[])