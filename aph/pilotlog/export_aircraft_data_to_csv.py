import csv
from django.http import HttpResponse
from .models import Aircraft

def export_aircraft_data_to_csv():
    # Prepare CSV response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="exported_aircraft_data.csv"'

    # Write CSV data
    with open('C:/Users/pasca/PycharmProjects/ApexHive/aph/pilotlog/Data/export - logbook_template.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        writer = csv.writer(response)

        # Write each line from the template CSV to the response
        for row in csv_reader:
            writer.writerow(row)

    return response
