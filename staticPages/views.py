from django.shortcuts import render
from .models import showCase, review
def robots(request):
    pass
    # return render(request, 'page/robots.txt')

def sitemap(request):
    pass
    # return render(request, 'page/sitemap.xml', content_type = "application/xhtml+xml")



def index(request):
    title = 'Продвижение сайтов в ТОП-10 – заказать поисковое продвижение в Челябинске'
    description = 'Основное направление нашей компании – это комплекс услуг по продвижению сайтов в Челябинске.'
    keywords = 'продвижение сайта в топ 10, заказать поисковое продвижение в Челябинске, продвижение сайтов в Челябинске, раскрутка сайтов в Челябинске'
    showCases = showCase.objects.filter(is_active=True, showInHomePage=True)
    reviews = review.objects.filter(showHomePage=True)
    return render(request, 'staticPages/index.html', locals())

def about(request):
    return render(request, 'staticPages/about.html', locals())


