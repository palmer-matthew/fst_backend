from django.test import TestCase
from django.test import Client
from core.models import TestModel
from core.models import Event
# Create your tests here.



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

        event1 = Event(name = 'FST Pre-Orientation', start_date_time = '2020-08-05T09:00:00Z', end_date_time = '2020-08-05T14:00:00Z', location = 'Faculty of Science and Technology')
        event1.save()
        event2 = Event(name = 'Fresher\'s Orientation', start_date_time = '2020-08-28T09:00:00Z', end_date_time = '2020-08-28T14:00:00Z', location = 'UWI, Mona')
        event2.save()

        response = self.client.get('/events/')

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(len(data), 2)

        expected_response = [{
                                'id': event1.id,
                                'name': 'FST Pre-Orientation',
                                'start_date_time': '2020-08-05T09:00:00Z',
                                'end_date_time': '2020-08-05T14:00:00Z',
                                'location': 'Faculty of Science and Technology'
                            },
                            {
                                'id': event2.id,
                                'name': 'Fresher\'s Orientation',
                                'start_date_time': '2020-08-28T09:00:00Z',
                                'end_date_time': '2020-08-28T14:00:00Z',
                                'location': 'UWI, Mona' 
                            }]

        self.assertEqual(data, expected_response)