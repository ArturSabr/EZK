from django.db import models
from django.utils.translation import gettext_lazy as _


class City(models.Model):
    title = models.CharField(_('Название'), max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _('Город')
        verbose_name_plural = _('Города')


class ApplicationModel(models.Model):
    first_name = models.CharField(verbose_name=_('Имя'), max_length=123)
    last_name = models.CharField(verbose_name=_("Фамилия"), max_length=123)
    middle_name = models.CharField(verbose_name=_("Отчество"), max_length=123)
    age = models.DateTimeField(verbose_name=_("Дата рождения"))
    address = models.CharField(verbose_name=_("Адрес по прописке"), max_length=123)
    real_address = models.CharField(verbose_name=_("Фактический адрес"), max_length=123)
    education = models.CharField(verbose_name=_("В каком колледже, техникуме лицее вы учитесь?"), max_length=123)
    course = models.PositiveIntegerField(verbose_name=_('На каком вы курсе'))
    speciality = models.CharField(verbose_name=_('Cпециальность'), max_length=123)
    contact = models.CharField(verbose_name=_("Контакты"), max_length=123)
    contact_dad = models.CharField(verbose_name=_("Контакты отца"), max_length=123)
    contact_mam = models.CharField(verbose_name=_("Контакты матери"), max_length=123)
    comment = models.TextField(verbose_name=_("Коментарий"), blank=True, null=True)
    email = models.EmailField(verbose_name=_('Электронная почта'))
    city = models.ForeignKey(verbose_name=_('Город'), to=City, on_delete=models.DO_NOTHING, blank=True, null=True)
    is_active = models.BooleanField(verbose_name=_('Актив'), default=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'Заявка от {self.first_name} {self.last_name}'

    class Meta:
        ordering = ['-created_date']
        verbose_name = _('Заявка')
        verbose_name_plural = _('Заявки')


class NewsModel(models.Model):
    title = models.CharField(verbose_name=_('Заголовок'),max_length=255)
    body = models.TextField(verbose_name=_('Описание'),blank=True, null=True)
    created_date = models.DateTimeField(verbose_name=_('Дата'),auto_now_add=True)
    image = models.ImageField(verbose_name=_('Изображение'),upload_to='news/images')

    def __str__(self):
        return f'{self.title} | {self.date}'

    def get_full_name(self):
        return f'{self.title} {self.created_date}'

    class Meta:
        ordering = ['-created_date']
        verbose_name = _('Новость')
        verbose_name_plural = _('Новости')


class EventModel(models.Model):
    title = models.CharField(verbose_name=_('Заголовок'),max_length=255)
    body = models.TextField(verbose_name=_('Описание'),blank=True, null=True)
    created_date = models.DateTimeField(verbose_name=_('Дата'),auto_now_add=True)
    image = models.ImageField(verbose_name=_('Изображение'),upload_to='news/images')

    def __str__(self):
        return f'{self.title} | {self.date}'

    def get_full_name(self):
        return f'{self.title} {self.created_date}'

    class Meta:
        ordering = ['-created_date']
        verbose_name = _('Ивент')
        verbose_name_plural = _('Ивенты')


class ConcursModel(models.Model):
    title = models.CharField(verbose_name=_('Заголовок'),max_length=255)
    body = models.TextField(verbose_name=_('Описание'),blank=True, null=True)
    created_date = models.DateTimeField(verbose_name=_('Дата'),auto_now_add=True)
    image = models.ImageField(verbose_name=_('Изображение'),upload_to='news/images')

    def __str__(self):
        return f'{self.title} | {self.date}'

    def get_full_name(self):
        return f'{self.title} {self.created_date}'

    class Meta:
        ordering = ['-created_date']
        verbose_name = _('Конкурс')
        verbose_name_plural = _('Конкурсы')
