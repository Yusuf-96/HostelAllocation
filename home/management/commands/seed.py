from django.core.management.base import BaseCommand, CommandError
from django.core import management
from accounts.models import *
from django.utils import timezone
from django.contrib import auth
from django.contrib.auth.models import User,Group,Permission
import os
from django.conf import settings
# from infromation.models import*


class Command(BaseCommand):
    help = 'Create seed'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    # def success(self, *args, **options): 


    def handle(self, *args, **options):

                User.objects.all().delete()
                Profile.objects.all().delete()
                management.call_command('flush')
                contexts=[


                    # ============================================Admin Account====================================================

                    { 'first_name':'yusufu', 'last_name':'', 'username':'admin', 'email':'admin@admin.com', 'password':'password', 
                    'is_superuser':True,'is_staff':True,'date_joined':f'{ timezone.now() }' },

                     # ============================================Generic User Account====================================================
                    { 'first_name':'hasani', 'last_name':'ali', 'username':'B41611022', 'email':'hasani@hasani.com', 'password':'password', 
                    'is_superuser':False,'is_staff':False, 'date_joined':f'{ timezone.now() }' },
                ]
                
                self.stdout.write(self.style.SUCCESS('\n'))
                self.stdout.write(self.style.SUCCESS('\t LIST OF SEEDED USERs' ))
                self.stdout.write(self.style.SUCCESS('\n'))
                
                for context in contexts:
                    try:
                        user = User.objects.create_user(**context)
                        profile=Profile.objects.create(user=user,phone='',location='')
                        self.stdout.write(self.style.SUCCESS(f'| ------>user {user.username } seeded  successfully! ' ))
                        # self.stdout.write(self.style.SUCCESS(f'| ------>profile for {profile.user } created successfully! ' ))
                    except User.DoesNotExist:
                        raise CommandError('Error creating User')

                # if user.username == 'Yusuph':
                #     Group.objects.all().delete()
                #     groupAdministrator=Group.objects.create(name='administrator')
                #     groupClient=Group.objects.create(name='client')
                #     perms=Permission.objects.all()
                #     groupAdministrator.permissions.set(perms)
                #     user.groups.add(groupAdministrator)
                
                   

                self.stdout.write(self.style.SUCCESS('\n' ))
                self.stdout.write(self.style.SUCCESS('---------------------------------------------' ))
                self.stdout.write(self.style.SUCCESS(f'Congrats! {len(contexts)}  User(s) seeded Successfully!' ))
                self.stdout.write(self.style.SUCCESS('---------------------------------------------' ))
                    