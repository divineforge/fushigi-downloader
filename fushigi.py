#!/usr/bin/env python
# encoding: utf-8

import os
import argparse
import urllib.request
import time
import gzip
from urllib.parse import quote
from bs4 import BeautifulSoup
from io import StringIO

URL_BASE = "http://doraemon.mangawiki.org/"

def get_page_soup(url):
    """Download a page and return a BeautifulSoup object of the html"""
    response = urllib.request.urlopen(url)
    page_content = response.read()

    if response.info().get('Content-Encoding') == 'gzip':
        gzipFile = gzip.GzipFile(fileobj=response)
        page_content = gzipFile.read()

    soup_page = BeautifulSoup(page_content, "html.parser")

    return soup_page


def download_manga(manga, chapter, page_start, page_end, download_dir='./'):
    """Download a range of a chapters"""
    for page in range(page_start, page_end):
        url = '{0}read-manga/index.php?manga={1}&chapter={2}&page={3}'.format(URL_BASE,
                                                                              manga,
                                                                              chapter,
                                                                              page)
        print(url)
        soup = get_page_soup(url)
        img_tag=soup.find('img', {'class':"picture"})
        img_src = urllib.parse.quote(img_tag['src'])
        image_url = '{0}{1}{2}'.format(URL_BASE, 'read-manga/', img_src)
        print(image_url)

        filename = '{0}{1}.jpg'.format(download_dir, page)

        while True:
            time.sleep(2)
            print('Save ' + image_url + ' as ' + filename)
            try:

                urllib.request.urlretrieve(image_url, filename)
            except urllib.error.HTTPError as http_err:
                print ('HTTP error ', http_err.code, ": ", http_err.reason)

                if http_err.code == 404:
                    break

            except urllib.error.ContentTooShortError:
                print ('The image has been retrieve only partially.')
            except:
                print ('Unknown error')
            else:
                break

def main():
    parser = argparse.ArgumentParser(description='Fushigi Downloader')

    parser.add_argument('--manga', '-m',
                        required=True,
                        action='store',
                        help='Manga to download')

    parser.add_argument('--chapter', '-c',
                        action='store',
                        required=True,
                        help='Chapter to download')

    parser.add_argument('--start', '-s',
                        action='store',
                        default=1,
                        type=int,
                        help='Page to start download')

    parser.add_argument('--end', '-e',
                        action='store',
                        required=True,
                        type=int,
                        help='Page to end download')

    args = parser.parse_args()

    download_dir = '{0}/{1}/'.format(args.manga, args.chapter)
    if os.path.exists(download_dir) is False:
        os.makedirs(download_dir)

    download_manga(args.manga, args.chapter, args.start, args.end, download_dir)

if __name__ == "__main__":
    main()
