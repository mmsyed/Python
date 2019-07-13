import requests
from bs4 import BeautifulSoup

# url = 'https://www.reddit.com/r/FashionRepsBST/search/?q=sup&restrict_sr=1&sort=new'
url = 'https://www.reddit.com/r/politics/search/?q=house&restrict_sr=1&sort=new'
headers = {"User-Agent" : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0'}

page = requests.get(url, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

# title = soup.find(id='t3_cby4gt').get_text()
# print(title.strip())
age = soup.find(data-click-id='timestamp').get_text()
# age = soup.find(id='timestamp').get_text()
# print(age)
age_split = (age.split(" "))

if ((age_split[1] == 'minutes') and (age_split[0] <= '10')):
    print('sending email')
    send_mail()

