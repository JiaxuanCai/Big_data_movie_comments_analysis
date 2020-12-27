from login import DouBan
import time
import random
from bs4 import BeautifulSoup
import pandas as pd


class Crawler:
    def __init__(self):
        self.comment_url = 'https://movie.douban.com/subject/26357307/comments?start=%d&limit=20&sort=new_score&status=P'
        self.comment_count = 500
        self.douban = DouBan()
        self.get_comments()

    def get_comments(self):
        comments = {'users': [], 'ratings': [], 'shorts': [], 'times': []}
        for i in range(0, 500, 20):
            time.sleep(random.random())
            url = self.comment_url % i
            response = self.douban.get_html(url)
            print('进度', i, '条', '状态是：', response.status_code)
            soup = BeautifulSoup(response.text)
            for comment in soup.select('.comment-item'):
                try:
                    user = comment.select('.comment-info a')[0].text
                    rating = comment.select('.rating')[0]['class'][0][7:8]
                    short = comment.select('.short')[0].text
                    t = comment.select('.comment-time')[0].text.strip()
                    # print(user, rating, short, t)
                except:
                    continue
                else:
                    comments['users'].append(user)
                    comments['ratings'].append(rating)
                    comments['shorts'].append(short)
                    comments['times'].append(t)
            # break
        comments_pd = pd.DataFrame(comments)
        # 保存完整短评信息
        comments_pd.to_csv('comments.csv')
        # 仅保存评论，作为后续分词的数据源
        comments_pd['shorts'].to_csv('shorts.csv', index=False)

if __name__ == '__main__':
    crawler = Crawler()