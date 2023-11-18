from django.shortcuts import render

from .models import *


def index(request):
    information_boxs = InformationBox.get_all_information_box()
    feedback = Feedback.get_all_feedback()
    daily_quote = DailyQuote.get_today_daily_quote()
    info = {'InformationBox': information_boxs, 'Feedback': feedback, 'DailyQuote': daily_quote}
    return render(request, 'main/index.html', info)


def contact_us(request, *args, **kwargs):
    if request.method == 'POST':
        name = request.POST['name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        text = request.POST['text']
        info = ContactUs(name=name, last_name=last_name, email=email, text=text)
        info.save()
    return render(request, 'main/contact_us.html')


def credits(request):
    all_credits = Credits.get_all_credits()
    info = {'Credits': all_credits}
    return render(request, 'main/credits.html', info)
