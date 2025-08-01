from selenium import webdriver

# Next 2 lines are needed to specify the path to your geckodriver
geckodriver_path = "/snap/bin/geckodriver"
driver_service = webdriver.FirefoxService(executable_path=geckodriver_path)

browser = webdriver.Firefox(service=driver_service)
# browser = webdriver.Firefox() # Originial Example
browser.get("http://localhost:8000")

assert "Congratulations!" in browser.title
print("OK")
