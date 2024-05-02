from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

bs_capabilities = [
    {
        'browser': 'Chrome',
        'browser_version': 'latest',
        'os': 'Windows',
        'os_version': '10',
        'name': 'Test for Samsung Galaxy S10 on Flipkart - Chrome'
    },
    {
        'browser': 'Firefox',
        'browser_version': 'latest',
        'os': 'Windows',
        'os_version': '10',
        'name': 'Test for Samsung Galaxy S10 on Flipkart - Firefox'
    },
    {
        'browser': 'IE',
        'browser_version': '11.0',
        'os': 'Windows',
        'os_version': '10',
        'name': 'Test for Samsung Galaxy S10 on Flipkart - Internet Explorer'
    },
    {
        'browser': 'Edge',
        'browser_version': 'latest',
        'os': 'Windows',
        'os_version': '10',
        'name': 'Test for Samsung Galaxy S10 on Flipkart - Microsoft Edge'
    }
]

for caps in bs_capabilities:
    desired_caps = {
        'browser': caps['browser'],
        'browser_version': caps['browser_version'],
        'os': caps['os'],
        'os_version': caps['os_version'],
        'name': caps['name']
    }

    if caps['browser'] == 'Chrome':
        driver = webdriver.Chrome(options=webdriver.ChromeOptions())
    elif caps['browser'] == 'Firefox':
        driver = webdriver.Firefox(options=webdriver.FirefoxOptions())
    elif caps['browser'] == 'IE':
        driver = webdriver.Ie(capabilities=webdriver.DesiredCapabilities.INTERNETEXPLORER)
    elif caps['browser'] == 'Edge':
        driver = webdriver.Edge(options=webdriver.EdgeOptions())

    driver.get("https://www.flipkart.com")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Samsung Galaxy S10" + Keys.RETURN)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Mobiles']"))).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Brand']"))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Samsung']"))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Flipkart Assured']"))).click()

    sort_dropdown = driver.find_element(By.XPATH, "//div[text()='Price']")
    ActionChains(driver).move_to_element(sort_dropdown).perform()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Price -- High to Low']"))).click()

    products = driver.find_elements(By.XPATH, "//div[@class='_4rR01T']")
    prices = driver.find_elements(By.XPATH, "//div[@class='_30jeq3 _1_WHN1']")
    links = driver.find_elements(By.XPATH, "//a[@class='IRpwTa']")

    results = []
    for i in range(len(products)):
        product_name = products[i].text
        display_price = prices[i].text
        product_link = links[i].get_attribute('href')
        results.append({'Product Name': product_name, 'Display Price': display_price, 'Link to Product Details Page': product_link})

    print(f"Results for {caps['name']}:")
    for result in results:
        print(result)

    driver.quit()
