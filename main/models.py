from datetime import date
from django.db import models


class InformationBox(models.Model):
    title = models.CharField(blank=False, max_length=60)
    main_text = models.TextField(blank=False, max_length=500)
    box_img = models.ImageField(blank=False)
    side = models.CharField(blank=False, max_length=10, default='left')

    def __str__(self):
        return f'{self.title} /// {self.side}'

    @staticmethod
    def get_all_information_box():
        return InformationBox.objects.all()


class Feedback(models.Model):
    name = models.CharField(blank=False, max_length=60)
    feedback_text = models.TextField(blank=False, max_length=255)
    feedback_img = models.ImageField(blank=False)

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def get_all_feedback():
        return Feedback.objects.all()


class ContactUs(models.Model):
    name = models.CharField(blank=False, max_length=60)
    last_name = models.CharField(blank=False, max_length=60)
    email = models.EmailField(blank=False)
    text = models.TextField(blank=False)

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def get_all_feedback():
        return ContactUs.objects.all()


class DailyQuote(models.Model):
    text = models.CharField(max_length=150, blank=False)
    day = models.DateField()

    def __str__(self):
        return f'{self.day}'

    @staticmethod
    def get_all_daily_quote():
        return

    @staticmethod
    def get_today_daily_quote():
        today = date.today()
        quotes = DailyQuote.objects.all()
        quote = quotes[0]
        if DailyQuote.objects.filter(day=today):
            quote = DailyQuote.objects.get(day=today)
        return quote


class Credits(models.Model):
    name = models.CharField(blank=False, max_length=60)
    link = models.TextField(blank=False, max_length=500)
    position = models.CharField(blank=False, max_length=500)
    box_img = models.ImageField(blank=False)

    def __str__(self):
        return f'{self.name} /// {self.position}'

    @staticmethod
    def get_all_credits():
        return Credits.objects.all()
