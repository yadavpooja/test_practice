import  unittest
from selenium import webdriver

class login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test01(self):
        #to check google have gmail option
        self.driver.get("https://www.google.co.in/")
        gmail = self.driver.find_element_by_class_name("gb_P")
        gmail_text = gmail.text
        self.assertEqual("Gmail",gmail_text)

    def test02(self):
        self.driver.get("https://www.google.co.in/")
        self.driver.find_element_by_class_name("gb_P").click()
        page = self.driver.find_element_by_class_name("hidden-small")
        page_text =page.text
        self.assertEqual("Sign in to continue to Gmail",page_text)

    def test03(self):
        #to check page username field
        self.driver.get("https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/?tab%3Dwm&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier")
        email = self.driver.find_element_by_id("Email")
        email_text =email.get_attribute("placeholder")
        self.assertEqual("Enter your email",email_text)

    def test04(self):
        #to check option for password
        self.driver.get("https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/?tab%3Dwm&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier")
        passwd = self.driver.find_element_by_id("next")
        passwd_text = passwd.get_attribute("value")
        self.assertEqual("Next",passwd_text)

    

        




    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
