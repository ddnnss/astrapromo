from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models



class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    first_name = None
    last_name = None
    email = models.EmailField('Эл. почта', unique=True)
    is_vip = models.BooleanField('Вип?', default=False)
    clientFio = models.CharField('ФИО', max_length=255, blank=True, null=True)
    clientCompany = models.CharField('Фирма', max_length=50, blank=True, null=True)
    clientSite = models.CharField('Адрес сайта', max_length=50, blank=True, null=True)
    country = models.CharField('Страна', max_length=50, blank=True, null=True)
    city = models.CharField('Город', max_length=50, blank=True, null=True)
    post_code = models.CharField('Индекс', max_length=50, blank=True, null=True)
    phone = models.CharField('Телефон', max_length=50, blank=True, null=True)
    address = models.TextField('Адрес', blank=True, null=True)
    comment = models.TextField('Комментарий', blank=True, null=True)
    is_allow_email = models.BooleanField('Согласен на рассылку', default=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

class callBack(models.Model):
    clientName = models.CharField('Имя', max_length=255, blank=True, null=True)
    clientPhone = models.CharField('Телефон', max_length=255, blank=True, null=True)
    clientEmail = models.CharField('Email', max_length=255, blank=True, null=True)
    clientSite = models.CharField('Адрес сайта', max_length=255, blank=True, null=True)
    comment = models.TextField('Комментарий по клиенту', blank=True, null=True)
    is_done = models.BooleanField('Заявка отработана ?', default=False)
    is_client = models.BooleanField('Возможна дальнейшая работа ?', default=False)
    created_at = models.DateTimeField('Создана', auto_now_add=True)
    updated_at = models.DateTimeField('Изменена', auto_now=True)

    def __str__(self):
        return '{} - Заявка на обратный звонок. Отработана :{}'.format(self.created_at, self.is_done)

    class Meta:
        verbose_name = "Заявка на обратный звонок"
        verbose_name_plural = "Заявки на обратный звонок"

class quizForm(models.Model):
    step0 = models.CharField('Сколько заявок?', max_length=30, blank=True, null=True)
    step1 = models.CharField('Какой бюджет?', max_length=30, blank=True, null=True)
    step2 = models.CharField('Название сайта/Группы', max_length=255, blank=True, null=True)
    step3 = models.CharField('Какие услуги интересны?', max_length=50, blank=True, null=True)
    step4 = models.CharField('Сфера деятельности', max_length=255, blank=True, null=True)
    is_done = models.BooleanField('Заявка отработана ?', default=False)
    created_at = models.DateTimeField('Создана', auto_now_add=True)

    def __str__(self):
        return '{} - Квиз форма. Отработана :{}'.format(self.created_at, self.is_done)

    class Meta:
        verbose_name = "Квиз форма"
        verbose_name_plural = "Квиз формы"