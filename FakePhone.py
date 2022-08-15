import random
import requests
import datetime
from bs4 import BeautifulSoup as bs4
from fake_useragent import UserAgent

USER_AGENTS = [
    "Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Firefox/59",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
]

def gen_user_agent() -> str:
    #user_agent = random.choice(USER_AGENTS)
    try:
        user_agent = UserAgent().random
    except Exception:
       pass
    return user_agent


def get_header():
        headers = {
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "User-Agent": gen_user_agent(),
        }
        return headers

def get_random(list):
    return random.choice(list)

class Fake_Phone:
    
    def __init__(self) -> None:
        self.messages = dict()
        self.numbers = list()
        self.number_index = 0
        self.urls=list()
        self.set_all_engines()
        #self.current_number = self.numbers[self.number_index]

        
    def get_soup(self,webpage):
        soup = bs4(webpage,features="lxml")
        return soup

    def set_all_engines(self):
        #self.oksms()
        self.free_sms_num()
           
    def call_async_request(self,url):
        header= get_header()
        response = requests.get(url,headers=header)
        return self.get_soup(response.text)

    def get_async_results(self,func):
        [func(self.call_async_request(i)) for i in self.urls]

    def free_sms_num(self):
        self.numbers = list()
        soup =  self.call_async_request('https://receive-sms-free.cc/Free-USA-Phone-Number/1.html')
        #pages = int(soup.select('div[class="pagination-wrap"] li')[-1].a['href'].split('/')[-1].strip('.html'))
        #[self.urls.append('https://receive-sms-free.cc/Free-USA-Phone-Number/{page}.html'.format(page=i+1)) for i in range(1,pages)]
        self.numbers.extend(list(dict(number=i.span.text.replace(' ',''),receive_link=i["href"],site='freesms',country="US") for i in soup.select('li[class="wow fadeInUp"] a')))

        return self.numbers[:5] #this returns a list of dict containing number info
    
    def free_sms_child(self,number,choice=1):   
        soup = self.call_async_request(f"{number[choice]['receive_link']}")
        timestamp_now = int(datetime.datetime.now().timestamp())
        self.messages[number[choice]['number']] = list()
        for i in ["row border-bottom table-hover","row border-bottom table-hover bg-messages"]:
            elems = soup.select(f'div[class="{i}"]')
            for elem in elems:
                body_elem = elem.select('div[class="col-xs-12 col-md-8"]')
                detail_elem = elem.select(f'div[class="mobile_show message_head"]')                
                if body_elem not in [None,'',[]] and detail_elem not in [None,'',[]]:
                   body = body_elem[0].text
                   detail = detail_elem[0].text.strip(')').split('(') 
                else:continue                
                duration = detail[-1]
                sender = detail[0].strip('From')
                time = duration.split()[:-1]
                if time[-1] in ['min','mins']:
                    timestamp= (timestamp_now - (int(time[0])*60))
                elif time[-1] in ['hours', 'hour']:
                    timestamp= (timestamp_now-int(time[0])*60*60)
                elif time[-1] in ['weeks','week'] :
                    timestamp = (timestamp_now-(int(time[0])*60*60*24*7))
                elif time[-1] in ['second','seconds']:
                    timestamp =(timestamp_now-int(time[0]))
                else:
                
                    continue  
                self.messages[number[choice]['number']].append(dict(timestamp=timestamp,duration=duration,sender=sender,body=body))

        return self.messages[number[choice]['number']][:2]    
    

       





