# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase;
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.staticfiles.testing import LiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from .models import UserProfileInfo, Cat_Topic, Cat_Topic_Comment
from selenium.webdriver.support.wait import WebDriverWait

class CatFriendsTests(TestCase):

    def test_get_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_catlist_page(self):
        response = self.client.get('/cat_app/cat_list/')
        self.assertEqual(response.status_code, 200)

    def test_get_loginpage(self):
        response = self.client.get('/cat_app/login/')
        self.assertEqual(response.status_code, 200)

    def test_get_register_page(self):
        response = self.client.get('/cat_app/register/')
        self.assertEqual(response.status_code, 200)

class CatFriendsSeleniumTests(LiveServerTestCase):
	# fixtures = ['user-data.json']

	@classmethod
	def setUpClass(cls):
		super(CatFriendsSeleniumTests, cls).setUpClass()
		cls.selenium = WebDriver()
		cls.selenium.implicitly_wait(2000)

	@classmethod
	def tearDownClass(cls):
		cls.selenium.quit()
		super(CatFriendsSeleniumTests, cls).tearDownClass()

	def test_login(self):
		self.selenium.get("http://127.0.0.1:8000/cat_app/login/")
		username_input = self.selenium.find_element_by_name("username")
		username_input.send_keys('Jilly')
		password_input = self.selenium.find_element_by_name("password")
		password_input.send_keys('testpassword')
		self.selenium.find_element_by_name("login_button").click()
		# index_text = self.selenium.find_element_by_name("index_text")
		body = self.selenium.find_element_by_tag_name('body')
		self.assertIn("Welcome", body.text)


	def test_login_fakeuser(self):
		self.selenium.get("http://127.0.0.1:8000/cat_app/login/")
		username_input = self.selenium.find_element_by_name("username")
		username_input.send_keys('Harry')
		password_input = self.selenium.find_element_by_name("password")
		password_input.send_keys('not a password')
		self.selenium.find_element_by_name("login_button").click()
		# index_text = self.selenium.find_element_by_name("index_text")
		body = self.selenium.find_element_by_tag_name('body')
		self.assertNotIn("Welcome", body.text)

