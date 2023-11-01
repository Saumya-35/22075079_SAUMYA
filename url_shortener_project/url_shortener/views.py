from django.shortcuts import render, redirect
from .models import URLMapping
from .utils import generate_short_code
from django.http import Http404


def shorten_url(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        
        existing_mapping = URLMapping.objects.filter(long_url=long_url).first()
        
        if existing_mapping:
            return render(request, 'url_shortener/shorten_url.html', {'short_url': f'http://localhost:8000/{existing_mapping.short_code}'})
        
        short_code = generate_short_code(long_url)
        url_mapping = URLMapping(long_url=long_url, short_code=short_code)
        url_mapping.save()
        
        return render(request, 'url_shortener/shorten_url.html', {'short_url': f'http://localhost:8000/{short_code}'})
    
    return render(request, 'url_shortener/shorten_url.html')


def redirect_to_original(request, short_code):
    try:
        url_mapping = URLMapping.objects.get(short_code=short_code)
        return redirect(url_mapping.long_url)
    except URLMapping.DoesNotExist:
        raise Http404("Short URL does not exist")
    
def url_list(request):
    url_mappings = URLMapping.objects.all()
    return render(request, 'url_shortener/url_list.html', {'url_mappings': url_mappings})
