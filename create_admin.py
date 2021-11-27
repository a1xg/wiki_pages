import os
from django.contrib.auth import get_user_model
import django
django.setup()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wiki_pages.settings')
User = get_user_model()
User.objects.create_superuser('admin2', 'admin@admin.com', 'admin2')
