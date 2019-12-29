import requests
from bs4 import BeautifulSoup
import re

def get_page(url):
    page = requests.get(url)
    with open('content.txt','w') as file:
        file.write(str(page.content))
    soup = BeautifulSoup(page.content, 'html.parser')
    # ultag = soup.find('ul', {'class': 'bui-pagination__list'})
    # print(ultag)
    # page_list=[]
    # lis = ultag.find_all('li')
    # for li in lis:
    #     link = li.find('a')
    #     if link is not None and 'searchresults' in link['href']:
    #         detail_link = link['href']
    #         page_list.append(detail_link)
    # print(len(page_list))
    #main_div=soup.find("a", {"class": " sr_item_photo_link sr_hotel_preview_track "})
    for div in soup.find_all("a", {"class": "sr_item_photo_link sr_hotel_preview_track"}):
        print(div['href'])
        print("***********************************")
    # lis = soup.find_all('li')
    # for li in lis:
    #     if 'Quicksand' in str(li):
    #         link=li.find('a')
    #         print(li.text)
    #         #print(li)
    #         detail_link=link['href'] if link is not None else None
    #         print(detail_link)
    #         detailpage = requests.get(detail_link)
    #         print(detailpage.status_code)
    #         dsoup = BeautifulSoup(detailpage.content, 'html.parser')
    #         address = dsoup.find_all('span', {'class' : 'fl padR10 lh1-2'})
    #         print(address)
    #         print("*******************")


get_page('https://www.booking.com/searchresults.html?aid=356980&label=gog235jc-1DCAUobEIJbGFsLXF1aWxhSDNYA2hsiAEBmAExuAEXyAEM2AED6AEB-AECiAIBqAIDuALX_JfwBcACAQ&sid=48aeb9f5e06e3d609966e6b33c51850a&tmpl=searchresults&ac_click_type=b&ac_position=0&class_interval=1&dest_id=-2106102&dest_type=city&from_sf=1&group_adults=2&group_children=0&iata=DEL&label_click=undef&no_rooms=1&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&src=landmark&src_elem=sb&srpvid=82a55e9d84da0017&ss=New%20Delhi%2C%20Delhi%20NCR%2C%20India&ss_raw=delhi&ssb=empty&ssne=Red%20Fort&ssne_untouched=Red%20Fort&top_ufis=1&rows=25')
#headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
# rest=requests.get('https://www.goibibo.com/hotels/the-vegas-hotel-in-delhi-2452480955417304410/')
# print(rest.status_code)