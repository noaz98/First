import os
import requests

urls = input("Please write a URL or URLs you want to check\n").split(',')


def input_url(urls):
  for url in urls:
    url = url.strip()
    if "https:" not in url:
      if ".com" not in url:
        print(f"{url} is not a valid URLs")
        return answer()
      url = "https://" + url
    try:
      rs = requests.get(url)
      rs_code = rs.status_code
      if rs_code == requests.codes.ok:
        print(f"{url} is up!")
      else:
        print(f"{url} is Down!")
    except:
      print(f"{url} is Down!")
  return answer()


def answer():
  a = input("Do you want start over? y/n ")
  if a == 'y':
    def clear(): return os.system('cls')
    clear()
    urls = input("Please write a URL or URLs you want to check\n").split(',')
    return input_url(urls)
  elif a == 'n':
    print("bye!")
  else:
    print("Thats not a valid answer")
    return answer()


input_url(urls)
