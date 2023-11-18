import csv
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from tables.models import TeachersAddInfo

class Command(BaseCommand):
    help = 'Create users and user profiles from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        with open(csv_file, 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                try:
                    password = 'test'
                    name = row['name']
                    surname = row['surname']
                    username = row['email']
                    degree = row['degree']
                    position = row['position']
                    school = row['school']
                    orcid = row["ORCID"]
                    Scopus_ID = row["Scopus ID"]
                    Web_of_Science_ResearcherID = row["Web of Science ResearcherID"]
                    scientific_interests = row["scientific interests"]

                    user = User.objects.create_user(
                            username=username, 
                            password=password
                        )

                    user_profile = TeachersAddInfo(
                            user=user,
                            avatar='static/profile/avatars/User-Profile-PNG-Clipart-1781504426.jpeg',
                            name=name,
                            surname=surname,
                            degree=degree,
                            position=position,
                            school=school,
                            orcid=orcid,
                            Scopus_ID=Scopus_ID,
                            Web_of_Science_ResearcherID=Web_of_Science_ResearcherID,
                            scientific_interests=scientific_interests
                        )
                        
                    user_profile.save()
                    self.stdout.write(self.style.SUCCESS(f'Successfully created user {username}'))
                except:
                    pass
