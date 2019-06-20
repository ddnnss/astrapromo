from django.http import JsonResponse
from django.shortcuts import render, render_to_response
from .models import showCase, review, allServices


def robots(request):
    return render(request, 'staticPages/robots.txt')

def sitemap(request):
    return render(request, 'staticPages/sitemap.xml', content_type = "application/xhtml+xml")



def index(request):
    pixel_code = '<script>fbq("track", "ViewContent");</script>'
    active_home ='item-active'
    title = 'Продвижение сайтов в ТОП-10 – заказать поисковое продвижение в Челябинске | DIGITAL-АГЕНТСТВО ASTRA PROMO'
    description = 'Основное направление нашей компании – это комплекс услуг по продвижению сайтов в Челябинске.'
    keywords = 'продвижение сайта в топ 10, заказать поисковое продвижение в Челябинске, продвижение сайтов в Челябинске, раскрутка сайтов в Челябинске'
    showCases = showCase.objects.filter(is_active=True, showInHomePage=True)
    reviews = review.objects.filter(showHomePage=True)
    return render(request, 'staticPages/index.html', locals())

def about(request):
    pixel_code = '<script>fbq("track", "ViewContent");</script>'
    active_about ='item-active'
    title = 'О КОМПАНИИ | DIGITAL-АГЕНТСТВО ASTRA PROMO'
    description = 'Основное направление нашей компании – это комплекс услуг по продвижению сайтов в Челябинске.'
    keywords = 'продвижение сайта в топ 10, заказать поисковое продвижение в Челябинске, продвижение сайтов в Челябинске, раскрутка сайтов в Челябинске'
    return render(request, 'staticPages/about.html', locals())

def seo(request):
    pixel_code = '<script>fbq("track", "ViewContent");</script>'
    active_uslug='item-active'
    active_seo ='drop-item-active'
    title = 'Комплексное продвижение сайтов от 14 900 рублей в месяц | DIGITAL-АГЕНТСТВО ASTRA PROMO'
    description = 'Основное направление нашей компании – это комплекс услуг по продвижению сайтов в Челябинске.'
    keywords = 'продвижение сайта в топ 10, заказать поисковое продвижение в Челябинске, продвижение сайтов в Челябинске, раскрутка сайтов в Челябинске'
    showCases = showCase.objects.filter(is_active=True, caseType='SE')
    return render(request, 'staticPages/seo.html', locals())

def sites(request):
    pixel_code = '<script>fbq("track", "ViewContent");</script>'
    active_uslug='item-active'
    active_sites ='drop-item-active'
    title = 'СОЗДАНИЕ САЙТОВ | DIGITAL-АГЕНТСТВО ASTRA PROMO'
    description = 'Основное направление нашей компании – это комплекс услуг по продвижению сайтов в Челябинске.'
    keywords = 'продвижение сайта в топ 10, заказать поисковое продвижение в Челябинске, продвижение сайтов в Челябинске, раскрутка сайтов в Челябинске'
    showCases = showCase.objects.filter(is_active=True, caseType='SI')
    return render(request, 'staticPages/sites.html', locals())

def contacts(request):
    pixel_code = '<script>fbq("track", "Contact");</script>'
    active_contacts ='item-active'
    title = 'КОНТАКТЫ | DIGITAL-АГЕНТСТВО ASTRA PROMO'
    description = 'Основное направление нашей компании – это комплекс услуг по продвижению сайтов в Челябинске.'
    keywords = 'продвижение сайта в топ 10, заказать поисковое продвижение в Челябинске, продвижение сайтов в Челябинске, раскрутка сайтов в Челябинске'
    return render(request, 'staticPages/contacts.html', locals())

def showcase(request):
    pixel_code = '<script>fbq("track", "ViewContent");</script>'
    active_showcase ='item-active'
    title = 'НАШИ КЕЙСЫ | DIGITAL-АГЕНТСТВО ASTRA PROMO'
    description = 'Основное направление нашей компании – это комплекс услуг по продвижению сайтов в Челябинске.'
    keywords = 'продвижение сайта в топ 10, заказать поисковое продвижение в Челябинске, продвижение сайтов в Челябинске, раскрутка сайтов в Челябинске'
    showCases = showCase.objects.filter(is_active=True)
    return render(request, 'staticPages/showcase.html', locals())

def context(request):
    pixel_code = '<script>fbq("track", "ViewContent");</script>'
    active_uslug = 'item-active'
    active_context = 'drop-item-active'
    title = 'КОНТЕКСТНАЯ РЕКЛАМА | DIGITAL-АГЕНТСТВО ASTRA PROMO'
    description = 'Основное направление нашей компании – это комплекс услуг по продвижению сайтов в Челябинске.'
    keywords = 'продвижение сайта в топ 10, заказать поисковое продвижение в Челябинске, продвижение сайтов в Челябинске, раскрутка сайтов в Челябинске'
    showCases = showCase.objects.filter(is_active=True, caseType='CO')
    return render(request, 'staticPages/context1.html', locals())

def target(request):
    pixel_code = '<script>fbq("track", "ViewContent");</script>'
    active_uslug = 'item-active'
    active_target = 'drop-item-active'
    title = 'ТАРГЕТИРОВАННАЯ РЕКЛАМА | DIGITAL-АГЕНТСТВО ASTRA PROMO'
    description = 'Основное направление нашей компании – это комплекс услуг по продвижению сайтов в Челябинске.'
    keywords = 'продвижение сайта в топ 10, заказать поисковое продвижение в Челябинске, продвижение сайтов в Челябинске, раскрутка сайтов в Челябинске'
    showCases = showCase.objects.filter(is_active=True, caseType='TA')

    return render(request, 'staticPages/target.html', locals())

def services(request):
    pixel_code = '<script>fbq("track", "ViewContent");</script>'
    active_uslug = 'item-active'
    active_services = 'drop-item-active'
    title = 'ПРОЧИЕ УСЛУГИ | DIGITAL-АГЕНТСТВО ASTRA PROMO'
    description = 'Основное направление нашей компании – это комплекс услуг по продвижению сайтов в Челябинске.'
    keywords = 'продвижение сайта в топ 10, заказать поисковое продвижение в Челябинске, продвижение сайтов в Челябинске, раскрутка сайтов в Челябинске'
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



def customhandler404(request, exception, template_name='404.html'):
    response = render_to_response("404.html")
    response.status_code = 404
    return response