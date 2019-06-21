# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase;
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.staticfiles.testing import LiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from django.contrib.auth.models import User
from .models import UserProfileInfo, Cat_Topic, Cat_Topic_Comment

class RequestTests(TestCase):
	databases = {"__all__"}

	def test_get_homepage(self):
		print('test1')
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200)

	def test_get_catlistpage(self):
		print('test2')
		response = self.client.get('/cat_app/cat_list/')
		self.assertEqual(response.status_code, 200)

	def test_get_loginpage(self):
		print('test3')
		response = self.client.get('/cat_app/login/')
		self.assertEqual(response.status_code, 200)

	def test_get_registerpage(self):
		print('test4')
		response = self.client.get('/cat_app/register/')
		self.assertEqual(response.status_code, 200)



class CatTopicCommentTests(TestCase):
	databases = {"__all__"}

	@classmethod
	def setUpClass(cls):
		super(CatTopicCommentTests, cls).setUpClass()

	@classmethod
	def tearDownClass(cls):
		super(CatTopicCommentTests, cls).tearDownClass()

	def create_user_missy(self):
		return User.objects.create_user('Missy', 'testpassword')

	def create_profile_missy(self, user):
		user_profile = UserProfileInfo.objects.create(
			user=user,
			picture="images/cat1.jpg"
		)

		return user_profile

	def create_cat_lenny(self, user_profile):
		cat_topic = Cat_Topic.objects.create(
			owner=user_profile,
			cat_name="Lenny",
			cat_picture="cat_images/cat1.jpg",
			story="This cat is extreemly lazy"
		)

		return cat_topic

	def test_catcomment(self):
		print('test7')
		lengthBefore = len(Cat_Topic_Comment.objects.all())

		user = self.create_user_missy() 
		user_profile = self.create_profile_missy(user)
		cat_topic = self.create_cat_lenny(user_profile)

		Cat_Topic_Comment.objects.create(
			user=user,
			cat_topic=cat_topic,
			comment_picture_path="cat_images/cat1.jpg",
			comment="Yo I have been looking for have you. Have you been on here talking about cats all day?"
		)

		lengthAfter = len(Cat_Topic_Comment.objects.all())

		self.assertEqual(lengthBefore!=lengthAfter, True)

class CatTopicTests(TestCase):
	databases = {"__all__"}

	@classmethod
	def setUpClass(cls):
		super(CatTopicTests, cls).setUpClass()

	@classmethod
	def tearDownClass(cls):
		super(CatTopicTests, cls).tearDownClass()
	
	def create_user_micheal(self):
		return User.objects.create_user('Micheal', 'testpassword')

	def create_profile_micheal(self, user):
		user_profile = UserProfileInfo.objects.create(
			user=user,
			picture="images/cat1.jpg"
		)

		return user_profile

	def test_cat(self):
		print('test6')
		lengthBefore = len(Cat_Topic.objects.all())
		user = self.create_user_micheal()
		user_profile = self.create_profile_micheal(user)
		Cat_Topic.objects.create(
			owner=user_profile,
			cat_name="Garfield",
			cat_picture="cat_images/cat1.jpg",
			story="This cat is extreemly lazy"
		)

		lengthAfter = len(Cat_Topic.objects.all())

		self.assertEqual(lengthBefore!=lengthAfter, True)

class UserProfileTests(TestCase):
	databases = {"__all__"}

	@classmethod
	def setUpClass(cls):
		super(UserProfileTests, cls).setUpClass()

	@classmethod
	def tearDownClass(cls):
		super(UserProfileTests, cls).tearDownClass()

	def create_user_rubberduck(self):
		return User.objects.create_user('Rubberduck', 'testpassword')
	
	def test_userprofileinfo(self):
		print('test5')
		lengthBefore = len(UserProfileInfo.objects.all())
		user = self.create_user_rubberduck()
		UserProfileInfo.objects.create(
			user=user,
			picture="images/cat1.jpg"
		)

		lengthAfter = len(UserProfileInfo.objects.all())

		self.assertEqual(lengthBefore!=lengthAfter, True)

class CatFriendsSeleniumTests(LiveServerTestCase):
	databases = {"__all__"}

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
		print('test8')
		self.selenium.get("http://127.0.0.1:8000/cat_app/login/")
		username_input = self.selenium.find_element_by_name("username")
		username_input.send_keys('Jilly')
		password_input = self.selenium.find_element_by_name("password")
		password_input.send_keys('testpassword')
		self.selenium.find_element_by_name("login_button").click()
		# index_text = self.selenium.find_element_by_name("index_text")
		body = self.selenium.find_element_by_tag_name('body')
		self.assertIn("Welcome", body.text)


	def test_loginfakeuser(self):
		print('test9')
		self.selenium.get("http://127.0.0.1:8000/cat_app/login/")
		username_input = self.selenium.find_element_by_name("username")
		username_input.send_keys('Harry')
		password_input = self.selenium.find_element_by_name("password")
		password_input.send_keys('not a password')
		self.selenium.find_element_by_name("login_button").click()
		# index_text = self.selenium.find_element_by_name("index_text")
		body = self.selenium.find_element_by_tag_name('body')
		self.assertNotIn("Welcome", body.text)

