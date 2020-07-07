import json
import time
import demoji

from selenium.webdriver import Chrome

with open('./credentials.json') as f:
    params = json.load(f)
    
with open("./posts.json") as f:
    posts = json.load(f)
    
url = params["target_url"]

browser = Chrome()

def submit_post(text):
    browser.get(url)
    print(browser.title)
    
    time.sleep(5)
    
    input_field = browser.find_element_by_tag_name("textarea")
    
    text = demoji.replace(text)
    
    input_field.send_keys(text)
    
    time.sleep(2)
    
    button = browser.find_element_by_css_selector("div[class='freebirdFormviewerViewNavigationButtons'] > div[role='button']")
    
    button.click()
    
    time.sleep(1)
    
    
posts = posts["posts"]

for post in posts:
    submit_post(post["selftext"])
    print("Done with {}".format(post["title"]))
