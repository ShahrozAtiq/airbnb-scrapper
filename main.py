# import the necessary libraries
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# open a new Chrome browser window
driver = webdriver.Chrome("chromedriver.exe")

# navigate to the Airbnb website
driver.get("https://www.airbnb.com")

# find the search box element and enter the keyword to search
search_box = driver.find_element_by_xpath("//input[@aria-label='Search']")
search_box.send_keys("keyword")  # replace "keyword" with your desired keyword
search_box.send_keys(Keys.RETURN)

# wait for the page to load completely
driver.implicitly_wait(10)

# find all the search results and extract the necessary information
search_results = driver.find_elements_by_xpath("//div[@itemprop='itemListElement']")
result_list = []

for result in search_results:
    title = result.find_element_by_xpath(".//div[@class='_bzh5lkq']")
    location = result.find_element_by_xpath(".//div[@class='_167qordg']")
    price = result.find_element_by_xpath(".//span[@class='_krjbj']")
    rating = result.find_element_by_xpath(".//span[@class='_10fy1f8']")
    
    result_list.append([title.text, location.text, price.text, rating.text])

# close the browser window
driver.quit()

# write the scraped data to a CSV file
with open('airbnb_results.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Title', 'Location', 'Price', 'Rating'])
    writer.writerows(result_list)
