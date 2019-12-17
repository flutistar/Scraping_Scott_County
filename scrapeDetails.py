#Search restaurants list with Postcodes

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import xlsxwriter 

class scrapeDetails():
    def Details(Urls):
        currentPath = os.path.dirname(os.path.realpath(__file__)) + '/chromedriver.exe'
        driver = webdriver.Chrome(executable_path= currentPath)
        workbook = xlsxwriter.Workbook('Parcels.xlsx') 
        worksheet = workbook.add_worksheet("Details")
        row_count = 0
        #Set Sheet Colum Width
        worksheet.set_column('A:A', 10)
        worksheet.set_column('B:B', 32)
        worksheet.set_column('C:C', 110)
        worksheet.set_column('D:D', 30)
        worksheet.set_column('E:E', 35)
        worksheet.set_column('F:F', 60)
        worksheet.set_column('G:G', 25)
        worksheet.set_column('H:H', 12)
        worksheet.set_column('I:I', 12)
        worksheet.set_column('J:J', 12)
        worksheet.set_column('K:K', 12)
        worksheet.set_column('L:L', 12)
        worksheet.set_column('M:M', 12)
        #Set Sheet Colum Header
        worksheet.write(row_count, 0, 'ALT KEY')
        worksheet.write(row_count, 1, "SITE ADDRESS")
        worksheet.write(row_count, 2, "LEGAL DESCRIPTION")
        worksheet.write(row_count, 3, 'LAND USE')
        worksheet.write(row_count, 4, "OWNER")
        worksheet.write(row_count, 5, "OWNER ADDRESS")
        worksheet.write(row_count, 6, 'OCCUPANCY TYPE')
        worksheet.write(row_count, 7, "YEAR BUILT")
        worksheet.write(row_count, 8, "SALE DATE")
        worksheet.write(row_count, 9, 'SALE PRICE')
        worksheet.write(row_count, 10, "LAND VALUE")
        worksheet.write(row_count, 11, "BLDG VALUE")
        worksheet.write(row_count, 12, "JUST VALUE")
        i = 0
        for url in Urls:
            if i>3:
                break
            i += 1
            row_count +=1
            driver.get(url)
            print(url)
            # Check Agreement Button
            if len(driver.find_elements_by_xpath("//div[@class = 'modal-dialog']")):
                agreeButton = driver.find_element_by_xpath("//div[@class = 'modal-dialog']/div[@class = 'modal-content']/div[@class = 'modal-focus-target']/div[@class = 'modal-footer']/a[@class = 'btn btn-primary button-1']")
                agreeButton.click()
            # Summary - Auditor's Office
            if len(driver.find_elements_by_xpath("//section[@id = 'ctlBodyPane_ctl00_mSection']")):
                if len(driver.find_elements_by_xpath("//span[@id = 'ctlBodyPane_ctl00_ctl01_lblAlternateID']")):
                    altKey = driver.find_element_by_xpath("//span[@id = 'ctlBodyPane_ctl00_ctl01_lblAlternateID']").text
                    worksheet.write(row_count, 0, altKey)
                    print('altKey--  ', altKey)
                if len(driver.find_elements_by_xpath("//span[@id = 'ctlBodyPane_ctl00_ctl01_lblPropertyAddress']")):
                    propertyAddress = driver.find_element_by_xpath("//span[@id = 'ctlBodyPane_ctl00_ctl01_lblPropertyAddress']").text
                    worksheet.write(row_count, 1, propertyAddress)
                    print('property--  ', propertyAddress)
                if len(driver.find_elements_by_xpath("//span[@id = 'ctlBodyPane_ctl00_ctl01_lblLegalDescription']")):
                    briefDescription = driver.find_element_by_xpath("//span[@id = 'ctlBodyPane_ctl00_ctl01_lblLegalDescription']").text
                    worksheet.write(row_count, 2, briefDescription)
                    print('Description--  ', briefDescription)
                if len(driver.find_elements_by_xpath("//span[@id = 'ctlBodyPane_ctl00_ctl01_lblClass']")):
                    classItem = driver.find_element_by_xpath("//span[@id = 'ctlBodyPane_ctl00_ctl01_lblClass']").text
                    worksheet.write(row_count, 3, classItem)
                    print('class--  ', classItem)
                print('--------------------')
            # Owners - Auditor's Office
            if len(driver.find_elements_by_xpath("//section[@id = 'ctlBodyPane_ctl02_mSection']")):
                if len(driver.find_elements_by_xpath("//a[@id = 'ctlBodyPane_ctl02_ctl01_lstDeed_ctl01_lblDeedName_lnkSearch']")):
                    ownerName = driver.find_element_by_xpath("//a[@id = 'ctlBodyPane_ctl02_ctl01_lstDeed_ctl01_lblDeedName_lnkSearch']").text
                    worksheet.write(row_count, 4, ownerName)
                    print('ownername--  ', ownerName)
                if len(driver.find_elements_by_xpath("//a[@id = 'ctlBodyPane_ctl02_ctl01_lstDeed_ctl01_lnkAddress1']")):
                    ownerAddress1 = driver.find_element_by_xpath("//a[@id = 'ctlBodyPane_ctl02_ctl01_lstDeed_ctl01_lnkAddress1']").text
                    print('add-1--  ', ownerAddress1)
                if len(driver.find_elements_by_xpath("//span[@id = 'ctlBodyPane_ctl02_ctl01_lstDeed_ctl01_lblAddress2']")):
                    ownerAddress2 = driver.find_element_by_xpath("//span[@id = 'ctlBodyPane_ctl02_ctl01_lstDeed_ctl01_lblAddress2']").text
                    print('add-2--  ', ownerAddress2)
                if len(driver.find_elements_by_xpath("//span[@id = 'ctlBodyPane_ctl02_ctl01_lstDeed_ctl01_lblAddress3']")):
                    ownerAddress3 = driver.find_element_by_xpath("//span[@id = 'ctlBodyPane_ctl02_ctl01_lstDeed_ctl01_lblAddress3']").text
                    print('add-3--  ',ownerAddress3)
                worksheet.write(row_count, 5, ownerAddress1 + ', ' + ownerAddress2 + ', ' + ownerAddress3)
            # Residential Dwellings - Assessor's Office
            if len(driver.find_elements_by_xpath("//section[@id = 'ctlBodyPane_ctl06_mSection']")):
                if len(driver.find_elements_by_xpath("//span[@id = 'ctlBodyPane_ctl06_ctl01_lstResidential_ctl00_lblOccupancy']")):
                    occupancy = driver.find_element_by_xpath("//span[@id = 'ctlBodyPane_ctl06_ctl01_lstResidential_ctl00_lblOccupancy']").text
                    worksheet.write(row_count, 6, occupancy)
                    print('Occupancy--  ', occupancy)
                if len(driver.find_elements_by_xpath("//span[@id = 'ctlBodyPane_ctl06_ctl01_lstResidential_ctl00_lblYearBuilt']")):
                    yearBuilt = driver.find_element_by_xpath("//span[@id = 'ctlBodyPane_ctl06_ctl01_lstResidential_ctl00_lblYearBuilt']").text
                    worksheet.write(row_count, 7, yearBuilt)
                    print('Year Built--  ', yearBuilt)
            # Sales - Assessor's Office
            if len(driver.find_elements_by_xpath("//section[@id = 'ctlBodyPane_ctl12_mSection']")):
                if len(driver.find_elements_by_xpath("//section[@id = 'ctlBodyPane_ctl12_mSection']/div/div[1]/table/tbody/tr[1]")):
                    saleDate = driver.find_element_by_xpath("//section[@id = 'ctlBodyPane_ctl12_mSection']/div/div[1]/table/tbody/tr[1]/td[1]").text
                    amount = driver.find_element_by_xpath("//section[@id = 'ctlBodyPane_ctl12_mSection']/div/div[1]/table/tbody/tr[1]/td[8]").text
                    worksheet.write(row_count, 8, saleDate)
                    worksheet.write(row_count, 9, amount)
                    print('saleDate--  ', saleDate)
                    print('Amount--  ', amount)
            # Valuation - Assessor's Office
            if len(driver.find_elements_by_xpath("//section[@id = 'ctlBodyPane_ctl14_mSection']")):
                if len(driver.find_elements_by_xpath("//section[@id = 'ctlBodyPane_ctl14_mSection']/div/table")):
                    landValue = driver.find_element_by_xpath("//section[@id = 'ctlBodyPane_ctl14_mSection']/div/table/tbody/tr[2]/td[3]").text
                    BLDGValue = driver.find_element_by_xpath("//section[@id = 'ctlBodyPane_ctl14_mSection']/div/table/tbody/tr[4]/td[3]").text
                    justValue = driver.find_element_by_xpath("//section[@id = 'ctlBodyPane_ctl14_mSection']/div/table/tbody/tr[7]/td[3]").text
                    worksheet.write(row_count, 10, landValue)
                    worksheet.write(row_count, 11, BLDGValue)
                    worksheet.write(row_count, 12, justValue)
                    print('landValue--  ', landValue)
                    print('BLDGValue--  ', BLDGValue)
                    print('justValue--  ', justValue)
                else:
                    print('no Section14')
            print("<><><><><><><><><><><><><><><><><><><><><><><><>")
        # searchButton = driver.find_element_by_xpath("//a[@id = 'ctlBodyPane_ctl00_ctl01_btnSearch']")
        # searchButton.click()
        # parcelList = driver.find_elements_by_xpath("//table[@id ='ctlBodyPane_ctl00_ctl01_gvwParcelResults']/tbody/tr/td[2]/a")
        # for items in parcelList:
        #     url = items.get_attribute('href')
        # print(len(parcelList) 'parcels scraped')
        workbook.close()
        driver.quit()
        # for pcode in postcodes:
        #     # i+=1
        #     # if i == 3:
        #     #     break    
        #     driver.get(baseUrl)
        #     search_box = driver.find_element(By.XPATH, "//input[@data-test-id='address-box-input']")
        #     time.sleep(1)
        #     search_box.clear()
        #     search_box.send_keys(pcode)
        #     search_box.submit()
        #     openRst = driver.find_elements_by_xpath("//div[@data-test-id='openrestaurants']/section[@data-test-id='restaurant']/a")
        #     cnt1 = 0
        #     for item1 in openRst:
        #         restaurantUrls.append(item1.get_attribute('href'))
        #         cnt1 += 1
        #         cnt += 1
        #     print(cnt, 'urls Scraped', pcode, '--open--', cnt1)
        #     cnt2 = 0
        #     closeRst = driver.find_elements_by_xpath("//div[@data-test-id='closedrestaurants']/section[@data-test-id='restaurant']/a")
        #     for item2 in closeRst:
        #         restaurantUrls.append(item2.get_attribute('href'))
        #         cnt2 += 1
        #         cnt += 1
        #     print(cnt, 'urls Scraped', pcode, "--close--", cnt2)
        #     cnt3 = 0
        #     offRst = driver.find_elements_by_xpath("//div[@data-test-id='offlinerestaurants']/section[@data-test-id='restaurant']/a")
        #     for item3 in offRst:
        #         restaurantUrls.append('off: ' + item3.get_attribute('href'))
        #         cnt3 += 1
        #         cnt3 += 1
        #         cnt += 1
        #     print(cnt, 'urls Scraped', pcode, "--off--", cnt3)            
        #     time.sleep(0.5)
        # driver.quit()
        # return restaurantUrls
