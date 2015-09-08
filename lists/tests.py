from django.core.urlresolvers import resolve
from django.test import TestCase

from django.http import HttpRequest
from lists.views import home_page

class HomePageTest(TestCase):
	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		self.assertTrue(response.content.startswith(b'<html>'))
		self.assertIn(b'<title>To-Do lists</title><h1>Jika saya Gina Andriyani</h1>', response.content)
		self.assertTrue(response.content.endswith(b'</html>'))
		
#from django.test import TestCase

# Create your tests here.
#class SmokeTest(TestCase):

#	def test_bad_maths(self):
#		self.assertEqual(1+1, 3)
