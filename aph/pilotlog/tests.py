from django.core.management import call_command
from django.http import HttpResponse
from django.test import TestCase
import json
import os

from .export_aircraft_data_to_csv import export_aircraft_data_to_csv
from .models import Aircraft, User

file_path = os.path.join(os.path.dirname(__file__), 'Data', 'import - pilotlog_mcc.json')


class ImportDataIntegrationTest(TestCase):

    def setUp(self):
        user = User.objects.create(pk=125880, user_id=125880)

        data = [
            {
                "user_id": user.user_id,
                "table": "Aircraft",
                "guid": "00000000-0000-0000-0000-000000000367",
                "meta": {
                    "Fin": "",
                    "Sea": False,
                    "TMG": False,
                    "Efis": False,
                    "FNPT": 0,
                    "Make": "Cessna",
                    "Run2": False,
                    "Class": 5,
                    "Model": "C150",
                    "Power": 1,
                    "Seats": 0,
                    "Active": True,
                    "Kg5700": False,
                    "Rating": "",
                    "Company": "Other",
                    "Complex": False,
                    "CondLog": 69,
                    "FavList": False,
                    "Category": 1,
                    "HighPerf": False,
                    "SubModel": "",
                    "Aerobatic": False,
                    "RefSearch": "PHALI",
                    "Reference": "PH-ALI",
                    "Tailwheel": False,
                    "DefaultApp": 0,
                    "DefaultLog": 2,
                    "DefaultOps": 0,
                    "DeviceCode": 1,
                    "AircraftCode": "00000000-0000-0000-0000-000000000367",
                    "DefaultLaunch": 0,
                    "Record_Modified": 1616320991
                },
                "platform": 9,
                "_modified": 1616317613
            }
        ]
        with open(file_path, 'w') as f:
            json.dump(data, f)

    def test_import_data(self):
        # Call the management command to import data
        call_command('import_data')

        # Perform assertions after data import
        imported_objects = Aircraft.objects.all()
        self.assertEqual(imported_objects.count(), 1)
        imported_object = imported_objects.first()
        self.assertEqual(imported_object.user_id, 125880)
        self.assertEqual(imported_object.guid, '00000000-0000-0000-0000-000000000367')


class ExportAircraftDataToCSVTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(pk=125880, user_id=125880)

        Aircraft.objects.create(
            user_id=user.user_id, guid='09877777', aircraft_code='123456', make='TestMake1', model='TestModel1',
            category=1, aircraft_class=1,
            complex=True, high_perf=True, pressurized=False, taa=False
        )

    def test_export_aircraft_data_to_csv(self):
        # Call the exporter function
        response = export_aircraft_data_to_csv()

        # Check if response is an instance of HttpResponse
        self.assertIsInstance(response, HttpResponse)

        # Check if the response has CSV content type
        self.assertEqual(response['Content-Type'], 'text/csv')

        # Check if CSV file is attached
        self.assertTrue('attachment; filename="exported_aircraft_data.csv"' in response['Content-Disposition'])

        # Read the content of the real CSV file
        with open('C:/Users/pasca/PycharmProjects/ApexHive/aph/pilotlog/Data/export - logbook_template.csv', 'r') as csv_file:
            expected_content = csv_file.read().splitlines()

        csv_content = response.content.decode('utf-8').splitlines()

        # Assert CSV content line by line
        for expected_line, actual_line in zip(expected_content, csv_content):
            expected_fields = expected_line.split(',')
            actual_fields = actual_line.split(',')

            # Ensure all fields are present in the actual CSV content
            self.assertEqual(len(expected_fields), len(actual_fields))

            for expected_field, actual_field in zip(expected_fields, actual_fields):
                self.assertEqual(expected_field.strip(), actual_field.strip())
