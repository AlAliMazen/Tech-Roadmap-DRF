from django.test import TestCase
from django.contrib.auth.models import User
from category.models import Category
from .models import Article
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.
class ArticleListViewTest(APITestCase):
    def setUp(self):
        User.objects.create_user(username='thomas', password='!password#')
         # Create a category
        Category.objects.create(owner_id=1, title='Test Category')

    def test_can_list_articles(self):
        admin_usr = User.objects.get(username='thomas')

        category = Category.objects.create(title='Test Category', owner=admin_usr)  # Create a Category
        #Article.objects.create(owner=admin_usr, title='a title',content="thomas content")
        Article.objects.create(
            owner= admin_usr, 
            title='a title', 
            content="thomas content", 
            category=category
        )
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))