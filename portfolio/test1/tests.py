from django.test import TestCase
from portfolio.models import BaseNetwork, Category, Base, Tag, Portfolio, Index, Comment, Network, About, Contact_msg, Contact
from portfolio import models

class BaseNetworkModelTest(TestCase):
    def setUp(self):
        self.base_network = BaseNetwork.objects.create(
            icon='fab fa-facebook-f',
            link='https://www.facebook.com'
        )

    def test_base_network_str(self):
        self.assertEqual(str(self.base_network), 'fab fa-facebook-f')

    def test_base_network_icon_field(self):
        icon_field = self.base_network._meta.get_field('icon')
        self.assertEqual(icon_field.max_length, 80)



class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Test Category'
        )

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Test Category')

    def test_category_name_field(self):
        name_field = self.category._meta.get_field('name')
        self.assertEqual(name_field.max_length, 80)




class BaseModelTest(TestCase):
    def setUp(self):
        self.base = Base.objects.create(
            title='Test Base'
        )

    def test_base_str(self):
        self.assertEqual(str(self.base), 'base.html')

    def test_base_title_field(self):
        title_field = self.base._meta.get_field('title')
        self.assertEqual(title_field.max_length, 255)





    def test_base_header_network_header_field(self):
        header_network_header_field = self.base._meta.get_field('header_network_header')
        self.assertEqual(header_network_header_field.max_length, 60)

    def test_base_fields(self):
        fields = [field.name for field in self.base._meta.get_fields()]
        expected_fields = ['id', 'icon', 'title', 'copyright', 'network', 'header_network', 'header_network_header']
        self.assertCountEqual(fields, expected_fields)



class ContactMsgModelTest(TestCase):
    def setUp(self):
        self.contact_msg = Contact_msg.objects.create(
            name='John Doe',
            email='johndoe@example.com',
            option='fikr',
            message='This is a test message'
        )

    def test_contact_msg_name_field(self):
        name_field = self.contact_msg._meta.get_field('name')
        self.assertEqual(name_field.max_length, 255)








class ContactModelTest(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            contact_about='Contact information',
            location='New York',
            number='123456789',
            contact_link='https://www.example.com',
            contact_name='John Doe'
        )

    def test_contact_contact_about_field(self):
        contact_about_field = self.contact._meta.get_field('contact_about')
        self.assertEqual(contact_about_field.max_length, 800)

    def test_contact_location_field(self):
        location_field = self.contact._meta.get_field('location')
        self.assertEqual(location_field.max_length, 200)

    def test_contact_number_field(self):
        number_field = self.contact._meta.get_field('number')
        self.assertEqual(number_field.max_length, 50)


    def test_contact_contact_name_field(self):
        contact_name_field = self.contact._meta.get_field('contact_name')
        self.assertEqual(contact_name_field.max_length, 60)


    def test_contact_fields(self):
        fields = [field.name for field in self.contact._meta.get_fields()]
        expected_fields = ['id', 'img_header', 'contact_about', 'location', 'number', 'contact_link',
                           'contact_name', 'follow']
        self.assertCountEqual(fields, expected_fields)