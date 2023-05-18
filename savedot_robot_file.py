from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set Chrome options to enable automatic downloads
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    'download.default_directory': '/path/to/save/directory',
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'safebrowsing.enabled': True
})

# Create a new instance of the Chrome driver with the configured options
driver = webdriver.Chrome('path/to/chromedriver', options=chrome_options)

# Open the URL that triggers the file download
driver.get('https://example.com/download.robot')

# Wait for the download to complete (you can adjust the wait time as needed)
# Note: You may need to implement additional logic to wait for the file to finish downloading

# Close the browser
driver.quit()
