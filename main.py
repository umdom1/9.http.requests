# first task

import requests

url = "https://akabab.github.io/superhero-api/api/all.json"
resp = requests.get(url)
res = resp.json()
name_list = ('Hulk', 'Captain America', 'Thanos')
intelligence_dict = {}
for el in res:
  if el['name'] in name_list:
    intelligence_dict[el['name']] = el['powerstats']['intelligence']  
intelligence_dict = sorted(intelligence_dict.items(), key=lambda x: x[1])  
print(f'Сымый умный: {intelligence_dict[-1][0]}, его интелект равен {intelligence_dict[-1][1]}')


# second task

class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
    def get_upload_files(self, url, disk_file_path, filename):
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        href =  data["href"]
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")



if __name__ == '__main__':
    disk_file_path = "/1.txt"
    url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
    token = 'token'
    uploader = YandexDisk(token)
    result = uploader.get_upload_files(url, disk_file_path, '1.txt')