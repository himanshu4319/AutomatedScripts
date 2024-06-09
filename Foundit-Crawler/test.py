import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from database import *
import time
import json
# from database import *

# job = input("Enter Job Domain: ")
# jobLoc = input("Enter Job Location: ")



def methodFetchingInformation(driver):
    
    fetchingURL= driver.current_url
    #fetching Job Title
    JobTitle=''
    try:
        JobTitle = driver.find_element(By.XPATH,"//div[@id='titleSection']//h1").text
    except:
        pass

    #fetching Company Name
    companyName=''
    try:
        companyName = driver.find_element(By.XPATH,"//div[@id='titleSection']//span//a").text
    except:
        try:
            companyName = driver.find_element(By.XPATH,"//div[@id='titleSection']//span").text
        except Exception as e:
            print(e)
    
    #fetching jobLocation
    jobLocation=""
    try:
        jobLocation = [item.text for item in driver.find_elements(By.XPATH,"//div[@id='jobHighlight']/div/div/div[1]/span/a")]
        jobLocation = ", ".join(jobLocation)
    except Exception as e:
        print(e)

    #fetching Experience
    jobExperience=''
    try:
        jobExperience = driver.find_element(By.XPATH,"//div[@id='jobHighlight']/div/div/div[2]/div/span").text
    except:
        pass
    
    #fetching Salary
    jobSalary =''
    try:
        jobSalary = driver.find_element(By.XPATH,'//div[@id="jobHighlight"]/div/div/div[2]/div[3]/span').text
    except:
        pass

    #fetching JobType
    jobType=''
    try:
        jobType=driver.find_element(By.XPATH,'//*[@id="jobInfo"]/div[1]/div/div/div/a').text
    except:
        pass

    #Industry Type
    industryType=''
    try:
        industryType=driver.find_element(By.XPATH,'//*[@id="jobInfo"]/div[2]/div/div/div/a').text
    except:
        pass

    #skills
    skills=[]
    try:
        skills = [item.text for item in driver.find_elements(By.XPATH,'//*[@id="jobInfo"]/div[4]/div/div/div/div')]
        skills = ", ".join(skills)
    except:
        pass
    
    #job Description
    jobDescription=''
    try:
        jobDescription = driver.find_element(By.XPATH,'//*[@id="jobDescription"]/div').text
    except:
        pass
    
    data=(fetchingURL,JobTitle,JobTitle,companyName,jobType,"",jobSalary,jobLocation,"",industryType,"",jobExperience,jobDescription.replace("\n",""),'Found it',skills)
    if selection(data)==False:
        insertion(data)
    else:
        pass

def findCards(driver):
    cards = driver.find_elements(By.XPATH, "//div[contains(@class, 'cardContainer') or @class='cardContainer activeCard']")
    url=driver.current_window_handle
    for i in cards:
        # print(len(cards))
        i.click()
        time.sleep(.5)
        link = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//i[@class='mqfisrp-open-jd']")))
        link.click()
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(2)
        methodFetchingInformation(driver)
        time.sleep(1)
        driver.close()
        driver.switch_to.window(url)

def MethodPageIteration(driver):
    findCards(driver)
    try:
        next_page = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='arrow arrow-right']"))
        )
        next_page.click()
        time.sleep(2)
        MethodPageIteration(driver)
    except Exception as e:
        print("No more pages or an error occurred:", e)
        driver.quit()


if __name__=="__main__":
    # Set up undetected Chrome options
    chrome_options = Options()
    chrome_options.headless = True
    # chrome_options.add_argument("--headless=new")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
    chrome_options.add_argument("--window-size=1920,1080")  # Set window size (optional)
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model (required for some environments)
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

    # Set up undetected Chrome driver
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://www.foundit.in/")

    #adding Job or company or skills
    locateInputField = driver.find_element(By.XPATH,"//input[@type='text' and @placeholder='Search by job, company or skills']")
    locateInputField.send_keys("Mechanical Engineer")

    #adding Locations
    locateInputField = driver.find_element(By.XPATH,"//input[@type='text' and @placeholder='Location']")
    locateInputField.send_keys("Gurugram")

    driver.find_element(By.XPATH,"//button[@type='submit']").click()


    # time.sleep(10)


    # findCards(driver)

    MethodPageIteration(driver)