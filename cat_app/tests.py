# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase;
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.staticfiles.testing import LiveServerTestCase
from selenium import webdriver
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

class LoginSeleniumTests(TestCase):
	databases = {"__all__"}

	@classmethod
	def setUpClass(cls):
		super(LoginSeleniumTests, cls).setUpClass()
		# cls.selenium = WebDriver()
		cls.driver = webdriver.Chrome()
		cls.driver.implicitly_wait(10)

	@classmethod
	def tearDownClass(cls):
		cls.driver.close()
		# cls.selenium.quit()
		super(LoginSeleniumTests, cls).tearDownClass()

	def test_login(self):
		print('test8')
		self.driver.get("http://127.0.0.1:8000/cat_app/login/")
		username_input = self.driver.find_element_by_name("username")
		username_input.send_keys('Jilly')
		password_input = self.driver.find_element_by_name("password")
		password_input.send_keys('testpassword')
		self.driver.find_element_by_name("login_button").click()
		body = self.driver.find_element_by_tag_name('body')
		self.assertIn("Welcome", body.text)
		self.driver.find_element_by_name("logout_nav").click()


	def test_loginfakeuser(self):
		print('test9')
		self.driver.get("http://127.0.0.1:8000/cat_app/login/")
		username_input = self.driver.find_element_by_name("username")
		username_input.send_keys('Harry')
		password_input = self.driver.find_element_by_name("password")
		password_input.send_keys('not a password')
		self.driver.find_element_by_name("login_button").click()
		body = self.driver.find_element_by_tag_name('body')
		self.assertNotIn("Welcome", body.text)

	def test_logout(self):
		print('test10')
		self.driver.get("http://127.0.0.1:8000/cat_app/login/")
		username_input = self.driver.find_element_by_name("username")
		username_input.send_keys('Jilly')
		password_input = self.driver.find_element_by_name("password")
		password_input.send_keys('testpassword')
		self.driver.find_element_by_name("login_button").click()
		self.driver.find_element_by_name("logout_nav").click()
		body = self.driver.find_element_by_tag_name('body')
		self.assertNotIn("logout_nav", body.text)

	def test_register(self):
		timeout = 10
		print('test10')
		self.driver.get("http://127.0.0.1:8000/")
		self.driver.find_element_by_name("register_nav").click()
		reg_username_input = self.driver.find_element_by_name("username")
		reg_username_input.send_keys('Mathew')
		reg_password_input1 = self.driver.find_element_by_name("password1")
		reg_password_input1.send_keys('testpassword')
		reg_password_input2 = self.driver.find_element_by_name("password2")
		reg_password_input2.send_keys('testpassword')
		self.driver.find_element_by_name("reg_submit_btn").click()

		self.driver.find_element_by_name("login_nav").click()
		username_input = self.driver.find_element_by_name("username")
		username_input.send_keys('Mathew')
		password_input = self.driver.find_element_by_name("password")
		password_input.send_keys('testpassword')
		self.driver.find_element_by_name("login_button").click()

		body = self.driver.find_element_by_tag_name('body')
		self.assertIn("Welcome", body.text)
		self.driver.find_element_by_name("logout_nav").click()




class ProfileSeleniumTests(TestCase):
	databases = {"__all__"}

	@classmethod
	def setUpClass(cls):
		super(ProfileSeleniumTests, cls).setUpClass()
		# cls.selenium = WebDriver()
		cls.driver = webdriver.Chrome()
		cls.driver.implicitly_wait(10)

	@classmethod
	def tearDownClass(cls):
		cls.driver.close()
		# cls.selenium.quit()
		super(ProfileSeleniumTests, cls).tearDownClass()


	def test_profile(self):
		print('test11')
		self.driver.get("http://127.0.0.1:8000/cat_app/login/")
		username_input = self.driver.find_element_by_name("username")
		username_input.send_keys('Jimmy')
		password_input = self.driver.find_element_by_name("password")
		password_input.send_keys('testpassword')
		self.driver.find_element_by_name("login_button").click()
		
		self.driver.find_element_by_name("profile_nav").click()
		self.driver.find_element_by_name("update_profile_link").click()
		update_picture_input = self.driver.find_element_by_name("picture")
		update_picture_input.send_keys("C:/Users/samje/Documents/WebProjects2/djangoenv/catfriends4/static/images/profile4.jpg")
		self.driver.find_element_by_name("profile_submit").click()


		image = self.driver.find_element_by_class_name('profile-center')
		self.assertIn("media/images/profile4", image.get_attribute("src"))
		self.driver.find_element_by_name("logout_nav").click()


class CatSeleniumTests(TestCase):
	databases = {"__all__"}

	@classmethod
	def setUpClass(cls):
		super(CatSeleniumTests, cls).setUpClass()
		# cls.selenium = WebDriver()
		cls.driver = webdriver.Chrome()
		cls.driver.implicitly_wait(10)

	@classmethod
	def tearDownClass(cls):
		cls.driver.close()
		# cls.selenium.quit()
		super(CatSeleniumTests, cls).tearDownClass()

	def test_add_cat(self):
		print('test12')
		self.driver.get("http://127.0.0.1:8000/")

		self.driver.find_element_by_name("login_nav").click()
		username_input = self.driver.find_element_by_name("username")
		username_input.send_keys('Mamba')
		password_input = self.driver.find_element_by_name("password")
		password_input.send_keys('testpassword')
		self.driver.find_element_by_name("login_button").click()

		self.driver.find_element_by_name("catlist_nav").click()
		self.driver.find_element_by_class_name("cat-list-button").click()
		catname_input = self.driver.find_element_by_name("cat_name")	
		catname_input.send_keys("annonymous cat")
		catpicture_input = self.driver.find_element_by_name("cat_picture")
		catpicture_input.clear()	
		catpicture_input.send_keys("C:/Users/samje/Documents/WebProjects2/djangoenv/catfriends4/static/images/tiger.jpg")
		catstory_input = self.driver.find_element_by_name("story")	
		catstory_input.send_keys("I haven't found this cat yet ):")	
		self.driver.find_element_by_name("cat_submit_btn").click()

		image = self.driver.find_element_by_class_name('center')
		self.assertIn("media/cat_images/tiger", image.get_attribute("src"))
		self.driver.find_element_by_name("logout_nav").click()



	def test_update_cat(self):
		print('test13')
		self.driver.get("http://127.0.0.1:8000/")

		self.driver.find_element_by_name("login_nav").click()
		username_input = self.driver.find_element_by_name("username")
		username_input.send_keys('Mamba')
		password_input = self.driver.find_element_by_name("password")
		password_input.send_keys('testpassword')
		self.driver.find_element_by_name("login_button").click()

		self.driver.find_element_by_name("catlist_nav").click()
		self.driver.find_element_by_xpath("/html/body/div/div[2]/ul/li[5]/table/tbody/tr[3]/td[1]/div/a").click()
		catpicture_input = self.driver.find_element_by_name("cat_picture")	
		catpicture_input.send_keys("C:/Users/samje/Documents/WebProjects2/djangoenv/catfriends4/static/images/grass-snake.jpg")
		self.driver.find_element_by_name("cat_submit_btn").click()

		image = self.driver.find_element_by_class_name('center')
		self.assertIn("media/cat_images/grass-snake", image.get_attribute("src"))
		self.driver.find_element_by_name("logout_nav").click()

	def test_remove_cat(self):
		print('test14')
		self.driver.get("http://127.0.0.1:8000/")

		self.driver.find_element_by_name("login_nav").click()
		username_input = self.driver.find_element_by_name("username")
		username_input.send_keys('Mamba')
		password_input = self.driver.find_element_by_name("password")
		password_input.send_keys('testpassword')
		self.driver.find_element_by_name("login_button").click()

		self.driver.find_element_by_name("catlist_nav").click()
		cat_amount_before = len(self.driver.find_elements_by_xpath("/html/body/div/div[2]/ul/li"))
		self.driver.find_element_by_xpath("/html/body/div/div[2]/ul/li[4]/table/tbody/tr[3]/td[2]/div/a").click()
		self.driver.find_element_by_name("cat_delete_btn").click()
		self.driver.find_element_by_name("catlist_nav").click()	
		cat_amount_after = len(self.driver.find_elements_by_xpath("/html/body/div/div[2]/ul/li"))

		self.assertNotEqual(cat_amount_after, cat_amount_before) 
		self.driver.find_element_by_name("logout_nav").click()



class CatCommentSeleniumTests(TestCase):
	databases = {"__all__"}

	@classmethod
	def setUpClass(cls):
		super(CatCommentSeleniumTests, cls).setUpClass()
		# cls.selenium = WebDriver()
		cls.driver = webdriver.Chrome()
		cls.driver.implicitly_wait(10)

	@classmethod
	def tearDownClass(cls):
		cls.driver.close()
		# cls.selenium.quit()
		super(CatCommentSeleniumTests, cls).tearDownClass()


	def test_cat_comment(self):
		print('test15')
		self.driver.get("http://127.0.0.1:8000/")

		self.driver.find_element_by_name("login_nav").click()
		username_input = self.driver.find_element_by_name("username")
		username_input.send_keys('Mamba')
		password_input = self.driver.find_element_by_name("password")
		password_input.send_keys('testpassword')
		self.driver.find_element_by_name("login_button").click()

		self.driver.find_element_by_name("catlist_nav").click()
		self.driver.find_element_by_name("cat_item_select").click()
		comment_input = self.driver.find_element_by_name("comment")
		comment_input.send_keys("Tom has turned into a Snake Wow and a very scary one at that!")
		self.driver.find_element_by_name("cat_comment_submit_btn").click()
	
		body = self.driver.find_element_by_tag_name('body')
		self.assertIn("Tom has turned into a Snake", body.text)
		self.driver.find_element_by_name("logout_nav").click()




