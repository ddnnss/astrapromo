from django.db import models
from pytils.translit import slugify
from ckeditor_uploader.fields import RichTextUploadingField


class showCase(models.Model):
    CONTEXT = 'CO'
    SEO = 'SE'
    TARGET = 'TA'
    SITES = 'SI'
    DISIGN = 'DI'
    CASETYPES = [
        (CONTEXT, 'Контекстная реклама'),
        (SEO, 'SEO продвижение'),
        (TARGET, 'Таргетированная релама'),
        (SITES, 'Создание сайтов'),
        (DISIGN, 'WEB дизайн'),
    ]

    caseName = models.CharField('Заголовок кейса', max_length=255, blank=False)
    caseNameSlug = models.CharField('Заголовок кейса', max_length=255, blank=True)
    siteUrl = models.CharField('Адрес сайта', max_length=255, blank=True)
    image = models.ImageField('Картинка', upload_to='showcases/', blank=False)
    showcaseInfo = models.CharField('Краткое описание', max_length=255, blank=False)
    showcaseFullInfo = RichTextUploadingField ('Полное описание ', blank=True, null=True)
    showInHomePage = models.BooleanField('Отображать на главной', default=False)
    is_active = models.BooleanField('Активный кейс?', default=False)
    caseType = models.CharField('Тип кейса', max_length=2, choices=CASETYPES, default=CONTEXT)

    def save(self, *args, **kwargs):
        self.caseNameSlug = slugify(self.caseName)
        super(showCase, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.caseName)

    def type_verbose(self):
        return dict(showCase.CASETYPES)[self.caseType]

    class Meta:
        verbose_name = "Кейс"
        verbose_name_plural = "Кейсы"

class review(models.Model):
    reviewFromCompany = models.CharField('От кого отзыв (фирма)', max_length=255, blank=True, null=True)
    reviewFromMan = models.CharField('От кого отзыв (руководитель)', max_length=255, blank=True, null=True)
    reviewFromSite = models.CharField('Сайт', max_length=255, blank=True, null=True)
    image = models.ImageField('Картинка', upload_to='showcases/', blank=False)
    text = models.TextField('Отзыв', blank=True, null=True)
    showHomePage = models.BooleanField("Показывать на главной?", default=False)

    def __str__(self):
        return '{}'.format(self.reviewFromCompany)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class ourSites(models.Model):
    image = models.ImageField('Картинка сайта', upload_to='sites/', blank=False)

    class Meta:
        verbose_name = "Сайт"
        verbose_name_plural = "Сайты"

class allServices(models.Model):
    serviceName = models.CharField('Заголовок услуги', max_length=255, blank=False)
    serviceNameSmall = models.CharField('Подзаголовок услуги', max_length=255, blank=False)

    serviceImage = models.ImageField('Картинка', upload_to='services/', blank=False)
    serviceInfo = models.CharField('Краткое описание', max_length=255, blank=False)
    servicePrice = models.CharField('Стоимость', max_length=255, blank=False, default='')
    serviceTarget = models.CharField('Код цели яндекс', max_length=255, blank=True)

    is_active = models.BooleanField('Показывать услугу?', default=False)



    def __str__(self):
        return '{}'.format(self.serviceName)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"