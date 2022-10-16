import requests as browser

import time

from selenium import webdriver

from bs4 import BeautifulSoup

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.firefox.options import Options

from json import loads

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

start = time.perf_counter()




def n():
    print()

n()
n()
n()
#======================================using search box API to get desired anime========================================





def animepahe_search():
    n()
    anime = str(input("Enter full Anime Name to look for : "))
    print()
    print(f'You searched for {anime}')
    n()
    print('Searching....')
    n()
    # url pattern requested when anime is searched    
    animepahe_search_pattern = f'https://animepahe.com/api?m=search&q={anime}'
    
    global search_response_dict
    
    search_response = browser.get(animepahe_search_pattern).text
    # converting response json data to python dictionary for operation
    search_response_dict = loads(search_response)
    # all animepahe has a session url and the url will be https://animepahe.com/anime/[then the session id]

    resultlen = len(search_response_dict['data'])
    
    print(f'{resultlen} results were found and are as follows --> ')
    
    n()
    
    
    for el in range(len(search_response_dict['data'])):
        name = search_response_dict['data'][el]['title']
        
        episodenum = search_response_dict['data'][el]['episodes']
        
        status = search_response_dict['data'][el]['status']
        
        session = search_response_dict['data'][el]['session']
        
        index = el 
        print('-------------'*12)
        print(f'Name of Anime : {name}')
        
        n()
        
        print(f'Number of episodes contained : {episodenum}')
        
        n()
        
        print(f'Current status of the anime : {status}')
        
        n()
        
        print(f'session id of the anime : {session}')
        
        n()
        
        print(f'Index of anime : {index}')
        
        print('-------------'*12)
        n()
        n()
    
    n()
    n()    
    pick_index = int(input("Out of the results pick the Index of anime u want : ")) 
    
    n()
    global animepicked
    animepicked = search_response_dict['data'][pick_index]['title']
    
    print(f'You picked {animepicked}')
    
    n()
    
    session_id = search_response_dict['data'][pick_index]['session']
    
       
    '''for el in range(len(search_response_dict['data'])):
        if 
        '''
    #anime episode page url format and url
    global episode_page_format
    
    episode_page_format = f'https://animepahe.com/anime/{session_id}'
    
    
    # now the anime_json_data url format
    anime_url_format = f'https://animepahe.com/api?m=release&id={session_id}&sort=episode_asc&page=1'
    
    print(f'Json information on episodes ,title ,\nSession of the episodes is here : {anime_url_format}')
    
    print()
    
    print(f'Anime url to view episodes is : {episode_page_format}')
    
    n()
    
    
    return anime_url_format

#=================Now writing function to head over to the episodes and stream/download pages and get pahewin url================




def episodes_stream_page():
    global streampage_episode
    # using return value of the search function to get the page
    jsonpage = animepahe_search()
    
    # using the json data from the page url to get page where the episodes to watch are
    json_dataon_anime = browser.get(jsonpage).text
    
    jsonpage_dict = loads(json_dataon_anime)
    
    pagelen = jsonpage_dict['to']
    print()
    
    print(f'Number of episode contained is : {pagelen}')
    
    n()
    
    #This is the stream page where u can watch or download the anime
    
    anime_session = (int(input("Enter episode to stream or download >> ")))-1
    
    streampage_session = jsonpage_dict['data'][anime_session]['session']
    
    streampage_episode = (jsonpage_dict['data'][anime_session]['episode'])
    
    stream_page_format = f'{episode_page_format}/{streampage_session}'
    
    print()
    
    print(f'The episode you want to download : Episode {streampage_episode}')
    
    stream_page_json = f'https://animepahe.com/api?m=links&id={streampage_session}&p=kwik'
    
    stream_page_dict = loads(browser.get(stream_page_json).text)
    
    
    for i in range(len(stream_page_dict['data'])):
        global availquality
        availquality = (list(stream_page_dict['data'][i].keys()))[0]
        audio = stream_page_dict['data'][i][availquality]['audio']
        if audio == 'jpn':
            audio = 'English Sub'
        else:
            audio = 'English Dub'
        n()
        print(f'Available Download info  : ',end='')
        print(f'quality - {availquality} and is {audio}')
        n()
        if availquality == '720':
            global pahewin_download_url
            pahewin_download_url = stream_page_dict['data'][i]['720']['kwik_pahewin']
            
    return pahewin_download_url
    


#--------------------------------------------Selenium driver initialization---------------------------
n()
n()

driverchoice = str(input("Enter your browser of choice e.g chrome/firefox : "))

if driverchoice.lower() == "chrome":
    option = webdriver.ChromeOptions()

    option.headless = True

    option.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=option)
    
elif driverchoice.lower() == "firefox":
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

else:
    option = webdriver.ChromeOptions()

    option.headless = True

    option.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=option)


#--------------------------------------------------------------------------------------------------------

    
#======================Function for pahewin soup and getting kwik url and download========================

def AnimeDownloader():
    pahe_win_url = episodes_stream_page()
    
    pahewin = browser.get(pahe_win_url).text
    
    #==================Using beautiful soub to get kwik download page id
    
    pahe_soup = BeautifulSoup(pahewin,'lxml')
    
    kwik_link= pahe_soup.find('a',class_ = 'redirect')['href']
    
    #---------------------------Using selenium to render and clickk the download button------------------------
    
    
    
    
    driver.get(kwik_link)

    #wait for elements to load

    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//form[@method = 'POST']/button[contains(@class, 'button')]")))

    element = driver.find_element(By.XPATH,"//form[@method = 'POST']/button[contains(@class, 'button')]")

    ad = driver.find_element(By.XPATH,'/html/body/div[2]/a')

    ad.click()
    
    n()
    
    down = str(input("Do you want to still download the anime [y or n] : "))
    
    if down.lower() == 'y':
        element.click()
        n()
        print(f'You are Downloading Episode {streampage_episode} of {animepicked} NOW!!!!!!!')
        n()
        print("check the Anime file in your specified downloads folder")
        
    elif down.lower() == 'yes':
        element.click()
        n()
        print(f'You are Downloading Episode {streampage_episode} of {animepicked} NOW!!!!!!!')
        n()
        print("check the Anime file in your specified downloads folder")

    else:
        n()
        print("You chose to not download just run the script again if you change your mind")
        
        driver.quit()
        
        exit()





AnimeDownloader()


finish = time.perf_counter()

n()

print(f'Finish time is {round(finish-start,2)}')

n()
