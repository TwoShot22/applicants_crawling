from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time

class Applicant:
    def __init__(self):
        self.info = ""
        self.part = ""
        self.q1 = ""
        self.q2 = ""
        self.q3 = ""
        self.q4 = ""
        self.date = ""

driver = webdriver.Chrome("./chromedriver")
driver.get("http://www.likelion-mju.com/admin/login/?next=/admin/")

# id
id_box = driver.find_element_by_css_selector('input#id_username')
id_box.send_keys("#")

# password
pass_box = driver.find_element_by_css_selector('input#id_password')
pass_box.send_keys("#")

driver.find_element_by_css_selector('div.submit-row input').click()

time.sleep(2)

driver.get("http://www.likelion-mju.com/apply/list/submit")
soup = BeautifulSoup(driver.page_source, 'html.parser')

applicants = soup.select("ul.list-group li")
print(len(applicants))
print(applicants)

all = []
# tmp = driver.find_elements_by_css_selector('li.list-group-item a')
for i in range(0, len(applicants)):
    driver.find_elements_by_css_selector('li.list-group-item a')[i].click()
    # driver.find_element_by_css_selector("ul.list-group a:nth-of-type("+str(i)+")").click()
    time.sleep(2)
    html = BeautifulSoup(driver.page_source, 'html.parser')
    ap = Applicant()
    info = html.select('div.user-info')
    for i in info:
        ap.info = ap.info + i.text + "\n"
    ap.part = html.select_one('input#field[checked]').attrs['value']
    ap.q1 = html.select_one('textarea#answer1').text
    ap.q2 = html.select_one('textarea#answer2').text
    ap.q3 = html.select_one('textarea#answer3').text
    ap.q4 = html.select_one('textarea#answer4').text
    ap.date = html.select_one('input#date[checked]').attrs['value']
    all.append(ap)
    driver.get("http://www.likelion-mju.com/apply/list/submit")

print(all)
print(ap.date)
print(ap)
driver.close()