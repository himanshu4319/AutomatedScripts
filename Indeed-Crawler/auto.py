import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import json
from database import *

job = input("Enter Job Domain: ")
jobLoc = input("Enter Job Location: ")

# Set up undetected Chrome options
chrome_options = Options()
chrome_options.headless = True
# chrome_options.add_argument("--headless=new")  # Run in headless mode
# chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
chrome_options.add_argument("--window-size=1920,1080")  # Set window size (optional)
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model (required for some environments)
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

# Set up undetected Chrome driver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to Indeed website
driver.get("https://www.indeed.com")
print(driver.title)

# Wait for the page to load completely
time.sleep(5)

# Locate the job input field
wait = WebDriverWait(driver, 10)  # Increase wait time to 20 seconds
try:
    locateJobInputField = wait.until(EC.visibility_of_element_located((By.ID, "text-input-what")))
    locateJobInputField.clear()
    locateJobInputField.send_keys(job)
except Exception as e:
    print(f"Failed to locate job input field: {e}")
    driver.quit()
    exit()

# Locate the job location field
try:
    locateJobLocationInputField = driver.find_element(By.ID, "text-input-where")
    locateJobLocationInputField.clear()
    locateJobLocationInputField.send_keys(jobLoc)
except Exception as e:
    print(f"Failed to locate job location input field: {e}")
    driver.quit()
    exit()

# Locate and click the Submit button
try:
    locatingSubmitButton = driver.find_element(By.XPATH, "//div//button[text()='Find jobs']")
    locatingSubmitButton.click()
except Exception as e:
    print(f"Failed to locate and click submit button: {e}")
    driver.quit()
    exit()

# Method for removing extra spaces
def removeExtraSpaces(lst):
    return [item.strip() for item in lst]

# Accessing Page Information
dictionary = {}
def methodFetchingInformation(driver, directory):
    for i in directory:
        informationList = {}
        time.sleep(0.5)
        driver.get(i)
        
        # Fetching JobTitle
        jobTitle = driver.find_element(By.XPATH, "//div//h1//span").text
        
        # Fetching CompanyName
        companyName = ''
        try:
            companyName = driver.find_element(By.XPATH, "//div[@data-company-name='true']//span//a").text
        except:
            companyName = driver.find_element(By.XPATH, "//div[@data-company-name='true']//span").text

        # Fetching JobLocation
        jobLocation = driver.find_element(By.XPATH, "//div[@id='jobLocationText']/div/span").text
        
        # Fetching Salary
        jobSalary = ''
        try:
            jobSalary = driver.find_element(By.XPATH, "//div[@id='salaryInfoAndJobType']//span").text
        except:
            pass

        # Fetching Job Type
        jobType = []
        jobType_selectors = [
            "//div[@data-testid='Permanent-tile']//div//div",
            "//div[@data-testid='Full-time-tile']//div//div",
            "//div[@data-testid='Fresher-tile']//div//div",
            "//div[@data-testid='Internship-tile']//div//div",
            "//div[@data-testid='Part-time-tile']//div//div",
            "//div[@data-testid='Freelance-tile']//div//div",
            "//div[@data-testid='Temporary-tile']//div//div"
        ]
        for selector in jobType_selectors:
            try:
                jobType.append(driver.find_element(By.XPATH, selector).text)
            except:
                pass

        # Fetching Shift Type
        jobShift = []
        jobShift_selectors = [
            "//div[@data-testid='Day shift-tile']//div//div",
            "//div[@data-testid='Fixed shift-tile']//div//div",
            "//div[@data-testid='Weekend availability-tile']//div//div",
            "//div[@data-testid='Monday to Friday-tile']//div//div",
            "//div[@data-testid='Night Shift-tile']//div//div",
            "//div[@data-testid='Evening Shift-tile']//div//div",
            "//div[@data-testid='US shift-tile']//div//div",
            "//div[@data-testid='Overnight Shift-tile']//div//div",
            "//div[@data-testid='Rotational Shift-tile']//div//div"
        ]
        for selector in jobShift_selectors:
            try:
                jobShift.append(driver.find_element(By.XPATH, selector).text)
            except:
                pass

        # Fetching Benefits or Perks
        jobBenefits = []
        try:
            jobBenefits = [item.text for item in driver.find_elements(By.XPATH, "//div[@id='benefits']/div[1]/div/span/ul/li")]
        except:
            pass

        # Fetching Job Description
        jobDescription = driver.find_element(By.XPATH, "//div[@id='jobDescriptionText']").text

        data = [
            i, jobTitle, jobTitle, companyName, ", ".join(jobType), ", ".join(jobShift),
            jobSalary, jobLocation, ", ".join(jobBenefits), "", jobDescription, "", "", "indeed", ""
        ]
        print(data)
        insertion(tuple(data))
        dictionary[i] = {
            "job_title": jobTitle,
            "company_name": companyName,
            "job_location": jobLocation,
            "job_salary": jobSalary,
            "job_type": ", ".join(jobType),
            "job_shift": ", ".join(jobShift),
            "job_benefits": ", ".join(jobBenefits),
            "job_description": jobDescription
        }

# Accessing hyperlinks from the jobs
def methodLocateHyperLinks(driver):
    locatedHyperLinks = []
    locateElements = driver.find_elements(By.XPATH, "//div//a[@role='button']")
    for i in locateElements:
        locatedHyperLinks.append(i.get_attribute("href"))
        time.sleep(0.5)
    return methodFetchingInformation(driver, locatedHyperLinks)

# Accessing Page Hyperlinks
locatedPageLinks = []
count = 0
def methodPageHyperLinks(driver):
    url = driver.current_url
    methodLocateHyperLinks(driver)
    driver.get(url)
    time.sleep(1)
    try:
        locateElement = driver.find_element(By.XPATH, "//div//li/a[@aria-label='Next Page']")
        locatedPageLinks.append(locateElement.get_attribute("href"))
        driver.get(locateElement.get_attribute("href"))
        methodPageHyperLinks(driver)
    except:
        return locatedPageLinks

methodPageHyperLinks(driver)

# def dumpJSON(dictionary):
#     with open("filename.json", "w", encoding="utf-8") as file:
#         json.dump(dictionary, file, indent=4)

# dumpJSON(dictionary)
driver.quit()
