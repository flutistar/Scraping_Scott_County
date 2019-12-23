#Search restaurants list with Postcodes

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
class scrapeParcels():
    def Parcels():
        parcelList = []
        urls = []
        baseUrl = "https://beacon.schneidercorp.com/Application.aspx?AppID=1024&PageType=Search"
        currentPath = os.path.dirname(os.path.realpath(__file__)) + '/chromedriver.exe'
        driver = webdriver.Chrome(executable_path= currentPath)
        driver.get(baseUrl)
        if driver.find_element_by_xpath("//div[@class = 'modal-dialog']"):
            agreeButton = driver.find_element_by_xpath("//div[@class = 'modal-dialog']/div[@class = 'modal-content']/div[@class = 'modal-focus-target']/div[@class = 'modal-footer']/a[@class = 'btn btn-primary button-1']")
            agreeButton.click()
        searchButton = driver.find_element_by_xpath("//a[@id = 'ctlBodyPane_ctl00_ctl01_btnSearch']")
        searchButton.click()
        parcelList = driver.find_elements_by_xpath("//table[@id ='ctlBodyPane_ctl00_ctl01_gvwParcelResults']/tbody/tr/td[2]/a")
        for items in parcelList:
            urls.append( items.get_attribute('href') )
        driver.quit()
        return urls
        