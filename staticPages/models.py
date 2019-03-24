from django.db import models
from pytils.translit import slugify
from ckeditor_uploader.fields import RichTextUploadingField


class showCase(models.Model):
    caseName = models.CharField('Заголовок кейса', max_length=255, blank=False)
    caseNameSlug = models.CharField('Заголовок кейса', max_length=255, blank=True)
    siteUrl = models.CharField('Адрес сайта', max_length=255, blank=False)
    image = models.ImageField('Картинка', upload_to='showcases/', blank=False)
    showcaseInfo = models.CharField('Краткое описание', max_length=255, blank=False)
    showcaseFullInfo = RichTextUploadingField ('Полное описание ', blank=True, null=True)
    showInHomePage = models.BooleanField('Отображать на главной', default=False)
    is_active = models.BooleanField('Активный кейс?', default=False)

    def save(self, *args, **kwargs):
        self.caseNameSlug = slugify(self.caseName)
        super(showCase, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.caseName)

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
