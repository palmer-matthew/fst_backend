from django.test import TestCase
from django.test import Client
from core.models import TestModel
from core.models import Contact
from core.models import PhoneNumber
from core.models import Event
from core.models import NewsFeed
import datetime
# Create your tests here.

class ContactViewTest(TestCase):
    
    def setUp(self):
        self.client = Client()

    def test_get(self):
        tm1 = Contact(name='Dr Kelly Harris', description='Head, department of Life Sciences', email='kelly.harris@uwimona.edu.jm',contact_type='FACULTY/STAFF', department='LIFE')
        tm1.save()
        tm1_expected = {
            'id': tm1.id,
            'name' :tm1.name,
            'website': tm1.website,
            'email':tm1.email,
            'fax':tm1.fax,
            'description': tm1.description,
            'department': tm1.department,
            'contact_type': tm1.contact_type,            
            'phone_contact_set': []  
        }

        tm2 = Contact(name='Police', department='OTHER', contact_type='EMERGENCY')
        tm2.save()
        tm2_phone = PhoneNumber(phone='119',platforms='TEXT/CALL', contact=tm2)
        tm2_phone.save()
        tm2_expected = {
            'id': tm2.id,
            'name' :tm2.name,
            'website': tm2.website,
            'email':tm2.email,
            'fax':tm2.fax,
            'description': tm2.description,
            'department': tm2.department,
            'contact_type': tm2.contact_type,            
            'phone_contact_set': [{'id': 1, 'contact': 2, 'phone': '119', 'platforms': 'TEXT/CALL'}]           
        }

        tm3 = Contact(name='Department of Computing Main Office', website='https://uwi/compsci.html',fax='(876) 390-4838', department='COMP', email='computing@uwimona.edu.jm', contact_type='OFFICE' )
        tm3.save()
        tm3_phone1 = PhoneNumber(phone='(876) 983-4782', platforms='TEXT/CALL', contact=tm3)
        tm3_phone1.save()
        tm3_phone2 = PhoneNumber(phone='(876) 489-5892', platforms='TEXT/CALL', contact=tm3)
        tm3_phone2.save() 
        tm3_expected = {
            'id': tm3.id,
            'name' :tm3.name,
            'website': tm3.website,   
            'email':tm3.email,
            'fax':tm3.fax,                     
            'description': tm3.description,     
            'department': tm3.department,       
            'contact_type': tm3.contact_type,            
            'phone_contact_set': [
                {'id': 2, 'contact': 3, 'phone': '(876) 983-4782', 'platforms': 'TEXT/CALL'}, 
                {'id': 3, 'contact': 3, 'phone': '(876) 489-5892', 'platforms': 'TEXT/CALL'}]
        }

        tm4 = Contact(name='MITS', department='OTHER', contact_type='OTHER')
        tm4.save()
        tm4_phone = PhoneNumber(phone='(876) 278-2892', platforms='WHATSAPP', contact=tm4)
        tm4_phone.save()
        tm4_expected = {
            'id': tm4.id,
            'name' :tm4.name,
            'website': tm4.website,   
            'email':tm4.email,
            'fax':tm4.fax,                     
            'description': tm4.description,     
            'department': tm4.department,       
            'contact_type': tm4.contact_type,            
            'phone_contact_set': [{'id': 4, 'contact': 4, 'phone': '(876) 278-2892', 'platforms': 'WHATSAPP'}]
        }

        #check for all objects being returned
        response  = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(len(data),4)        

        expected_response = [
            tm3_expected,
            tm1_expected,    
            tm4_expected,
            tm2_expected
        ]

        self.assertEqual(data,expected_response)

        #test department filter
        #test1
        response  = self.client.get('/contact/?department=LIFE')
        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(len(data),1)

        expected_response = [tm1_expected]

        self.assertEqual(data,expected_response)

        #test2
        response  = self.client.get('/contact/?department=COMP')
        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(len(data),1)

        expected_response = [tm3_expected]

        self.assertEqual(data,expected_response)

        #test3
        response  = self.client.get('/contact/?department=OTHER')
        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(len(data),0)

        expected_response = []

        self.assertEqual(data,expected_response)

        #test contact type filter
        #test1
        response  = self.client.get('/contact/?type=OTHER')
        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(len(data),1)

        expected_response = [tm4_expected]

        self.assertEqual(data,expected_response)

        #test2
        response  = self.client.get('/contact/?type=EMERGENCY')
        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(len(data),1)

        expected_response = [tm2_expected]

        self.assertEqual(data,expected_response)


        #test search filter
        #test1
        response  = self.client.get('/contact/?search=pol')
        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(len(data),1)

        expected_response = [tm2_expected]

        self.assertEqual(data,expected_response)

        #test2
        response  = self.client.get('/contact/?search=head%20of%20life')
        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(len(data),1)

        expected_response = [tm1_expected]

        self.assertEqual(data,expected_response)

        #test3
        response  = self.client.get('/contact/?search=office&department=COMP')
        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(len(data),1)

        expected_response = [tm3_expected]

        self.assertEqual(data,expected_response)

        #test 4
        response  = self.client.get('/contact/?search=green&department=COMP')
        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(len(data),0)

        expected_response = []

        self.assertEqual(data,expected_response)

        #test 5
        response  = self.client.get('/contact/?search=4782')
        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(len(data),1)

        expected_response = [tm3_expected]

        self.assertEqual(data,expected_response)

        #test 6
        response  = self.client.get('/contact/?search=office&type=EMERGENCY')
        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(len(data),0)

        expected_response = []

        self.assertEqual(data,expected_response)



class  TestModelViewTest(TestCase):

    def setUp(self):
        self.client = Client()
    
    def test_get(self):
        # Create test models
        test_model1 = TestModel(first_name='John', last_name='Abbot')
        test_model1.save()
        test_model2 = TestModel(first_name='Jake', last_name='Randall')
        test_model2.save()
        
        #making a get request to test model endpoint
        response  = self.client.get('/testview/')

        #check status code
        self.assertEqual(response.status_code, 200)

        # get json data
        data = response.json()

        #check number of models returned
        self.assertEqual(len(data), 2)

        #check if api returns data stored
        expected_response = [{
                                'id': test_model1.id, 
                                'first_name': 'John', 
                                'last_name': 'Abbot'
                            }, 
                            {
                              'id': test_model2.id,
                              'first_name': 'Jake',
                              'last_name': 'Randall' 
                            }]
        self.assertEqual(data, expected_response)

class EventViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_get(self):

        event1 = Event(name = 'General Orientation for New Undergraduate Students', start_date_time = '2020-08-28T09:00:00Z', end_date_time = '2020-08-28T15:00:00Z', location = 'Online', poster_image = 'assets/general_orientation_poster.JPG')
        event1.save()
        event2 = Event(name = 'FST Virtual Orientation', start_date_time = '2020-08-31T09:00:00Z', end_date_time = '2020-09-04T17:00:00Z', location = 'Online', poster_image = 'assets/fst_orientation_poster.JPG')
        event2.save()

        response = self.client.get('/events/')

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(len(data), 2)

        expected_response = [{
                                'id': event1.id,
                                'name': 'General Orientation for New Undergraduate Students',
                                'start_date_time': '2020-08-28T09:00:00Z',
                                'end_date_time': '2020-08-28T15:00:00Z',
                                'location': 'Online',
                                'poster_image': 'assets/general_orientation_poster.JPG'
                            },
                            {
                                'id': event2.id,
                                'name': 'FST Virtual Orientation',
                                'start_date_time': '2020-08-31T09:00:00Z',
                                'end_date_time': '2020-09-04T17:00:00Z',
                                'location': 'Online',
                                'poster_image': 'assets/fst_orientation_poster.JPG'
                            }]

        self.assertEqual(data, expected_response)
        
class  NewsFeedViewTest(TestCase):

    def setUp(self):
        self.client = Client()
    
    def test_get(self):
        # Create test models
        news_story1 = NewsFeed(title = 'News Story 1', date = datetime.date(2020, 4, 17), story = 'This is my first news story.')
        news_story1.save()
        news_story2 = NewsFeed(title = 'News Story 2', date = datetime.date(2020, 5, 21), story = 'This is my second news story.')
        news_story2.save()
        
        #making a get request to test model endpoint
        response  = self.client.get('/newsfeed/')

        #check status code
        self.assertEqual(response.status_code, 200)

        # get json data
        data = response.json()

        #check number of models returned
        self.assertEqual(len(data), 2)

        #check if api returns data stored
        expected_response = [{
                                'id': news_story1.id,
                                'title': 'News Story 1', 
                                'date': '2020-04-17', 
                                'story': 'This is my first news story.'
                            }, 
                            {
                                'id': news_story2.id,
                                'title': 'News Story 2',
                                'date': '2020-05-21',
                                'story': 'This is my second news story.' 
                            }]
        self.assertEqual(data, expected_response)
