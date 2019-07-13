
import praw
import enchant
import datetime as datetime
import time
from datetime import timedelta

# reddit api login
reddit = praw.Reddit(client_id='nZXy5zMuXw1_kg',
                     client_secret='hvn-m_ot_5Zu7ztOnIx4ihUt8tY',
                     username='newpost_bot',
                     password='W8xsrgJeh73FAaK',
                     user_agent='new post bot')
                    
bool = True
keyphrase1 = '!newpostbot'
keyphrase2 = '!stopnewpostbot'

# the subreddits you want your bot to live on
subreddit = reddit.subreddit('FashionRepsBST')

def get_date(created):
    timestamp = datetime.datetime.fromtimestamp(created)
    return timestamp


# try:
#     res = subreddit.search("supreme", sort="new", limit=10)
#     print("check1")
#     for submission in res:
#         print("check2")
#         timestamp = get_date(submission.created_utc)
#         # user = submission.user
#         cur = datetime.datetime.now()
#         # current_time = cur.strftime("%H:%M:%S")
#         td = timestamp - cur if timestamp > cur else cur - timestamp               
#         td_mins = int(round(td.total_seconds() / 60))
#         print("check3")
#         if (td_mins >= 144):
#             reddit.redditor('chugg1t').message('TEST', 'This happened!')
#             print("send_alert")
# except:     
#             print('error')

for comment in subreddit.stream.comments():
    if keyphrase1 in comment.body:
        keyword = comment.body.replace(keyphrase1, '')
        keyword = keyphrase1.replace(" ", "")
        while(True)
        try:
            res = subreddit.search(keyword, sort="new", limit=10)
            for submission in res:
                timestamp = get_date(submission.created_utc)
                user = submission.user
                cur = datetime.datetime.now()
                # current_time = cur.strftime("%H:%M:%S")
                td = timestamp - cur if timestamp > cur else cur - timestamp
                td_mins = int(round(td.total_seconds() / 60))
                if (td_mins <= 145):
                    reddit.redditor('prliift').message('TEST', 'This happened!')
                    print("send_alert")
        except:     
            print('error')
    else:
        bool = False

