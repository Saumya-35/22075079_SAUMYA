
import random
import string
from .models import URLMapping

def generate_short_code(long_url):
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(6))
    while URLMapping.objects.filter(short_code=short_code).exists():
        short_code = ''.join(random.choice(characters) for _ in range(6))
    return short_code