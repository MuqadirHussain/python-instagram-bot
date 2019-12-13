from selenium import webdriver
import os
import csv
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

def read_data(path):
    try:
        if (os.path.exists(path)):  
            tagsArray=[]  
            with open(path,'r') as csvfile:
                data=csv.reader(csvfile)
                for row in data:
                    if(len(row)>0):
                        tagsArray.append(row[0][1:])
            return tagsArray
    except FileNotFoundError:
        print ("no data") 


def write_data(file,tag,no_of_post):
    try:
        if(os.path.exists(file)) is False:
            with open(file, 'w',newline='') as csvfile:
                filewriter = csv.writer(csvfile)
                filewriter.writerow(['TAGS', 'NO OF POST'])
                # filewriter.writerow(["#"+tag, no_of_post])
                csvfile.close()
        with open(file, 'a' , newline='') as csvfile:
            
            filewriter = csv.writer(csvfile)
            filewriter.writerow(["#"+tag, no_of_post])
    except FileNotFoundError:
        pass
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir="+os.getcwd()+"\\"+"user1")
#if you have google chrome portable then use this 
#chrome_options.binary_location=r'GoogleChromePortable\\App\\Chrome-bin\\chrome.exe'
chrome_options.add_argument('--disable-infobars')
browser=webdriver.Chrome(chrome_options=chrome_options)
browser.maximize_window()

file="tags.csv"
tag_data=read_data(file)
if(len(tag_data)>0):
    for rows_tag in tag_data:
        browser.get(r"https://www.instagram.com/explore/tags/"+rows_tag)
        try:
            WebDriverWait(browser, 15).until(lambda browser:
                                                        browser.execute_script('return document.readyState'))
            postnumber=browser.find_element_by_class_name('g47SY ')
            hash_tag_count=postnumber.text
            write_data("data.csv",rows_tag,hash_tag_count)
        except :
            write_data("data.csv",rows_tag,"page not found")
        
else:
    print("no data found")
