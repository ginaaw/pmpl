from selenium import webdriver
import unittest

class NewVIsitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

#	def tearDown(self):
#		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		self.browser.get('http://localhost:8000')		
		self.assertIn('To-Do', self.browser.title)
		header_text=self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Nama saya Gina Andriyani', header_text)
		self.fail('Finish the test!')

if __name__=='__main__':
	unittest.main(warnings='ignore')

#browser = webdriver.Firefox()
#browser.get('http://localhost:8000')

#assert 'To-Do' in browser.title

#browser.quit()
