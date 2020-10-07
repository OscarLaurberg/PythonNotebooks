import requests
from urllib.parse import urlparse
import multiprocessing
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
from operator import itemgetter

class MyIterator():
  def __init__(self, url_list):
    self.url_list = url_list

  def __iter__(self):
    self.index = 0;
    return self

  def __next__(self):
    if self.index < len(self.filenames):
      nf = self.filesnames[self.index]
      self.index += 1
      return res
    raise StopIteration

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
    with ThreadPoolExecutor(10) as ex:
      res = tqdm(ex.map(self.download, self.url_list, self.filenames), total=len(self.url_list))
      return list(res)


  def urllist_generator(self):
    for url in self.url_list:
      yield url

  def average_number_of_vowels(self, file):
    file_path = f'../downloads/{file}.txt'
    with open(file_path, 'r') as file_object:
      data = file_object.read()
      words =  len(data.split())
      amountOfVowels = sum(v.lower() in 'aeiou' for v in data)
      return (file, amountOfVowels / words)

  def hardest_read(self, workers=multiprocessing.cpu_count()):
    with ProcessPoolExecutor(workers) as ex:   
        res = list(ex.map(self.average_number_of_vowels, self.filenames))
    highestAmount = max(res, key=itemgetter(1))[1]
    fileName = max(res, key=itemgetter(1))[0]
    return(f'Hardest read is filename: {fileName}, with and avg. of {highestAmount} vowels per word')
