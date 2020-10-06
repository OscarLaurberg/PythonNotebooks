import requests
from urllib.parse import urlparse
import multiprocessing
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

class MyIterator():
  def __init__(self, url_list):
    self.url_list = url_list

  def __iter__(self):
    return self

  def download(self, url, filename):
    r = requests.get(url)

    if(r.status_code == 404):
      raise NotFoundException

    file_path = f'../downloads/{filename}.txt'

    with open(file_path, 'w') as file_object:
      file_object.write(r.text)
    return file_path
  
  def multi_download(self):
    # Grabbing last part of our url
    self.filenames = [url.split('/')[-2] for url in self.url_list]
    with ThreadPoolExecutor() as ex:
      res = tqdm(ex.map(self.download, self.url_list, self.filenames), total=len(self.url_lsit))
      return list(res)
    