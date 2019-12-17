#Search restaurants list with Postcodes

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
class scrapRestaurants():
    def loaddriver(postcodes):
        restaurantUrls = []
        baseUrl = "https://www.just-eat.co.uk/"
        currentPath = os.path.dirname(os.path.realpath(__file__)) + '/chromedriver.exe'
        driver = webdriver.Chrome(executable_path= currentPath)
        i = 0
        cnt = 0
        for pcode in postcodes:
            # i+=1
            # if i == 3:
            #     break    
            driver.get(baseUrl)
            search_box = driver.find_element(By.XPATH, "//input[@data-test-id='address-box-input']")
            time.sleep(1)
            search_box.clear()
            search_box.send_keys(pcode)
            search_box.submit()
            openRst = driver.find_elements_by_xpath("//div[@data-test-id='openrestaurants']/section[@data-test-id='restaurant']/a")
            cnt1 = 0
            for item1 in openRst:
                restaurantUrls.append(item1.get_attribute('href'))
                cnt1 += 1
                cnt += 1
            print(cnt, 'urls Scraped', pcode, '--open--', cnt1)
            cnt2 = 0
            closeRst = driver.find_elements_by_xpath("//div[@data-test-id='closedrestaurants']/section[@data-test-id='restaurant']/a")
            for item2 in closeRst:
                restaurantUrls.append(item2.get_attribute('href'))
                cnt2 += 1
                cnt += 1
            print(cnt, 'urls Scraped', pcode, "--close--", cnt2)
            cnt3 = 0
            offRst = driver.find_elements_by_xpath("//div[@data-test-id='offlinerestaurants']/section[@data-test-id='restaurant']/a")
            for item3 in offRst:
                restaurantUrls.append('off: ' + item3.get_attribute('href'))
                cnt3 += 1
                cnt += 1
            print(cnt, 'urls Scraped', pcode, "--off--", cnt3)            
            time.sleep(1.5)
        driver.quit()
        return restaurantUrls
