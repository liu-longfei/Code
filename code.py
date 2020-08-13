import requests
from fake_useragent import UserAgent
import os
from multiprocessing import Pool


def download(i):
    headers = {
        'User-Agent': UserAgent().random
    }

    url = 'https://baidu.com-l-baidu.com/20190813/14599_f58526fd/1000k/hls/6829deecf9e00%04d.ts' % i
    response = requests.get(url, headers=headers)
    os.makedirs('video', exist_ok=True)
    if response.status_code != 404:
        with open('./video/{}'.format(url[-7:]), 'wb') as f:
            f.write(response.content)


def main():
    po = Pool(10)
    for i in range(1, 2000):
        po.apply_async(download, args=(i,))
    po.close()
    po.join()
    # ∫œ≤¢√¸¡Ó copy /b *.ts movie.mp4


if __name__ == '__main__':
    main()
