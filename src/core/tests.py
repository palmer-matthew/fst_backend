from django.test import TestCase
from django.test import Client
from core.models import TestModel
from core.models import Scholarship
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


class ScholarshipViewTest(TestCase):

    def setUp(self):
        self.client = Client()
    
    def test_get(self):
        tst_scholar_model1 = Scholarship(
            name ="Jimmy Neutron Welfare Scholarship",
            description="Available for 1st - 2nd year students for a maximum of 7 years",
            details="Must be involved in co-curricular activities, must have good hygiene, must be smart and not dunce"
        )
        tst_scholar_model1.save()
        tst_scholar_model2 = Scholarship(
            name ="Grace Kennedy Scholarship",
            description="Available for 1st - 3nd year students for a maximum of 1 years",
            details="Must be involved in co-curricular activities, must have good hygiene, must be smart and not dunce"
        )
        tst_scholar_model2.save()
        tst_scholar_model3 = Scholarship(
            name ="NCB STEM Scholarship",
            description="Available for 2nd year students going into 3rd year for a maximum of 0.5 years",
            details="Must be involved in co-curricular activities, must have good hygiene, must be smart and not dunce"
        )
        tst_scholar_model3.save()

        response = self.client.get('/scholarship/')

        self.assertEqual(response.status_code, 200)

        # get json data
        data = response.json()

        #check number of models returned
        self.assertEqual(len(data), 3)

        #check if api returns data stored
        expected_response = [{
                                'id': tst_scholar_model1.id, 
                                'name': "Jimmy Neutron Welfare Scholarship",
                                'description': "Available for 1st - 2nd year students for a maximum of 7 years",
                                'details': "Must be involved in co-curricular activities, must have good hygiene, must be smart and not dunce"

                            }, 
                            {
                              'id': tst_scholar_model2.id,
                              'name': "Grace Kennedy Scholarship",
                              'description': "Available for 1st - 3nd year students for a maximum of 1 years",
                              'details': "Must be involved in co-curricular activities, must have good hygiene, must be smart and not dunce"

                            },
                            {
                              'id': tst_scholar_model3.id,
                              'name': "NCB STEM Scholarship",
                              'description': "Available for 2nd year students going into 3rd year for a maximum of 0.5 years",
                              'details': "Must be involved in co-curricular activities, must have good hygiene, must be smart and not dunce"
 
                            }]
        self.assertEqual(data, expected_response)



