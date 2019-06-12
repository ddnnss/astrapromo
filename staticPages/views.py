from django.http import JsonResponse
from django.shortcuts import render
from .models import showCase, review, allServices
def robots(request):
    pass
    # return render(request, 'page/robots.txt')

def sitemap(request):
    pass
    # return render(request, 'page/sitemap.xml', content_type = "application/xhtml+xml")



def index(request):
    active_home ='item-active'
    title = 'Продвижение сайтов в ТОП-10 – заказать поисковое продвижение в Челябинске'
    description = 'Основное направление нашей компании – это комплекс услуг по продвижению сайтов в Челябинске.'
    keywords = 'продвижение сайта в топ 10, заказать поисковое продвижение в Челябинске, продвижение сайтов в Челябинске, раскрутка сайтов в Челябинске'
    showCases = showCase.objects.filter(is_active=True, showInHomePage=True)
    reviews = review.objects.filter(showHomePage=True)
    return render(request, 'staticPages/index.html', locals())

def about(request):
    active_about ='item-active'
    return render(request, 'staticPages/about.html', locals())

def seo(request):
    active_uslug='item-active'
    active_seo ='drop-item-active'
    showCases = showCase.objects.filter(is_active=True, showInHomePage=True)
    return render(request, 'staticPages/seo.html', locals())

def sites(request):
    active_uslug='item-active'
    active_sites ='drop-item-active'
    showCases = showCase.objects.filter(is_active=True, showInHomePage=True)
    return render(request, 'staticPages/sites.html', locals())

def contacts(request):
    active_contacts ='item-active'
    return render(request, 'staticPages/contacts.html', locals())

def showcase(request):
    active_showcase ='item-active'
    showCases = showCase.objects.filter(is_active=True)
    return render(request, 'staticPages/showcase.html', locals())

def context(request):
    active_uslug = 'item-active'
    active_context = 'drop-item-active'
    showCases = showCase.objects.filter(is_active=True, showInHomePage=True)
    return render(request, 'staticPages/context1.html', locals())

def target(request):
    active_uslug = 'item-active'
    active_target = 'drop-item-active'
    showCases = showCase.objects.filter(is_active=True, showInHomePage=True)

    return render(request, 'staticPages/target.html', locals())

def services(request):
    active_uslug = 'item-active'
    active_services = 'drop-item-active'
    services = allServices.objects.filter(is_active=True)
    return render(request, 'staticPages/other_services.html', locals())

def caseinfo(request):
    return_dict = {}
    caseId = request.POST.get('caseId')
    case = showCase.objects.get(id=caseId)
    return_dict['caseImg']=case.image.url
    return_dict['caseName'] = case.caseName
    return_dict['caseInfo'] = case.showcaseFullInfo
    return JsonResponse(return_dict)
