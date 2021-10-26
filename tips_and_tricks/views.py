from django.shortcuts import render
from tips_and_tricks.forms import AddForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from tips_and_tricks.models import TipsAndTrick
from django.core.paginator import Paginator
from django.core import serializers
from django.http import JsonResponse
from django.template.loader import render_to_string
# Create your views here.

def index(request):
    if 'page' in request.GET:
        q=request.GET['page']
        articles=TipsAndTrick.objects.filter(title__icontains=q)
        if q == '':
            paginator=Paginator(articles, 3)
            page_number = request.GET.get('page')
            articles = paginator.get_page(page_number)
    else:
        articles=TipsAndTrick.objects.all()

    if request.is_ajax():
        html = render_to_string(
            template_name="load_article.html", context={"articles": articles}
        )
        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)

    paginator=Paginator(articles, 3)
    page_number = request.GET.get('page')
    posts_obj = paginator.get_page(page_number)
    response = {'articles': posts_obj}
    return render(request, 'main.html', response)

@login_required(login_url='/admin/login/')
def add(request):
    form = AddForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/tips-and-tricks")
    response = {'form': form}
    return render(request, 'add.html', response)


def load_more(request):
    offset=int(request.POST['offset'])
    limit=3
    posts=TipsAndTrick.objects.all()[offset:limit+offset]
    totalData=TipsAndTrick.objects.count()
    data={}
    posts_json=serializers.serialize('json',posts)
    return JsonResponse(data={
        'posts':posts_json,
        'totalResult':totalData
    })