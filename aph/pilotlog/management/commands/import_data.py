from datetime import datetime

from django.core.management.base import BaseCommand
import json
from pathlib import Path

from ...models import Aircraft, User


class Command(BaseCommand):
    help = 'Import data from json File'

    def handle(self, *args, **options):
        file_path = Path('C:/Users/pasca/PycharmProjects/ApexHive/aph/pilotlog/Data/import - pilotlog_mcc.json')
        with open(file_path, 'r') as f:
            data = json.load(f)

        for item in data:
            user_id = item.get('user_id')
            # Get the user if exists, otherwise create it
            user, created = User.objects.get_or_create(user_id=user_id)

            if created:
                print(f"New user with user_id {user_id} created.")

            timestamp = item.pop('_modified')
            modified_datetime = datetime.fromtimestamp(timestamp)
            item['_modified'] = modified_datetime
            item['user'] = user

            try:
                obj = Aircraft(**item)
                obj.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully imported {obj.__dict__}'))
            except Exception as e:
                print(f"Failed to import aircraft: {e}")
