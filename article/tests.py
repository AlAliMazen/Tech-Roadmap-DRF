from django.test import TestCase
from django.contrib.auth.models import User
from category.models import Category
from .models import Article
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
class ArticleListViewTest(APITestCase):
    def setUp(self):
        # Create a user
        self.admin_usr = User.objects.create_user(username='thomas', password='!password#')
        
        # Create a category
        self.category = Category.objects.create(owner=self.admin_usr, title='Test Category')

    def test_can_list_articles(self):
        # Create an article
        Article.objects.create(
            owner=self.admin_usr, 
            title='a title', 
            content="thomas content", 
            category=self.category
        )
        
        # Perform GET request to list articles
        response = self.client.get('/articles/')
        
        # Check that the response status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_creat_article(self):
        # Log in the user with the correct password
        self.client.login(username='thomas', password='!password#')
        
        # Perform POST request to create an article
        response = self.client.post('/articles/', {
            'title': 'a title', 
            'owner': self.admin_usr.id,  # Use the ID of the user
            'category': self.category.id,  # Use the ID of the category
            'content': 'any content'
        })
        
        # Check that an article was created
        count = Article.objects.count()
        print("Count is ", count)
        self.assertEqual(count, 1)
        
        # Check that the response status is 201 CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)