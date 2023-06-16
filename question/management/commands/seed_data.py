from django.core.management.base import BaseCommand
from django_seed import Seed
import random
from question.models import Category, Question


class Command(BaseCommand):
    def handle(self, *args, **options):
        seeder = Seed.seeder()

        seeder.add_entity(Category, 50, {'category_name': lambda x: f'Category {random.randint(0,1000)}'})

        seeder.add_entity(
            Question, 
            50, 
            {
                'category': lambda x: Category.objects.order_by('?').first(),
                'question_text': lambda x: f'Question {random.randint(1000,2000)}',
            }
        )
        seeder.execute()
