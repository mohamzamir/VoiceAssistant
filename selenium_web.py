from selenium import webdriver


class info():
    def __init__(self):
        self.driver = webdriver.Safari(executable_path='/usr/bin/safaridriver')

    def get_info(self, query):

        self.query = query
        self.driver.get(url="https://www.wikipedia.org")

        search = self.driver.find_element_by_xpath('//*[@id="search-form"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button/i')
        enter.click()


