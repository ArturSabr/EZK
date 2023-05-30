from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *
from django.views.generic import ListView, DetailView, CreateView
from .forms import *
from django.urls import reverse
from django.shortcuts import render, redirect
import requests
from django.utils.decorators import method_decorator


class Home(ListView):
    model = NewsModel
    queryset = NewsModel.objects.all()[:3]
    context_object_name = 'news'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ApplicationForm
        context['news'] = NewsModel.objects.all()
        return context


class NewsListView(ListView):
    model = NewsModel
    queryset = NewsModel.objects.all()
    context_object_name = 'news'
    template_name = 'News.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ApplicationForm
        return context


class NewsDetailView(DetailView):
    model = NewsModel
    context_object_name = 'news'
    template_name = 'NewsDetail.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


class AdminApplicationListView(ListView):
    model = ApplicationModel
    queryset = NewsModel.objects.all()
    context_object_name = 'applications'
    template_name = 'application_list.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


class AdminApplicationDetailView(DetailView):
    model = ApplicationModel
    context_object_name = 'application'
    template_name = 'application_detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


class SendApplicationView(CreateView):
    model = ApplicationModel
    template_name = 'Offer.html'
    form_class = ApplicationForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            data = form.save(commit=False)
            try:
                data.save()
            except:
                return HttpResponse('Error')
            payload = {
                'chat_id': '-1001900947104',
                'text': f'Заявка была отправлена от - {data.get_full_name()}\nНомер - {data.contact}\nНомер(Мамы) - {data.contact_mam}\nНомер(Папы) - {data.contact_dad}'
            }
            a = requests.post(
                url='https://api.telegram.org/bot6050131482:AAEJdTpOg-9irChfpEVHij8NJjsuvVb5Hho/sendMessage',
                json=payload
            )
            print(a.json())
            return redirect(reverse('success'))
        else:
            print(form.errors)
            return super().post(request, *args, **kwargs)


class ApplicationSendSuccessView(ListView):
    model = ApplicationModel
    context_object_name = 'application'
    template_name = 'Success.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


def aboutus(request):
    return render(request, 'AboutUs.html', {'form': ApplicationForm})


def login(request):
    return render(request, 'Auth.html', {'form': ApplicationForm})


def security(request):
    return render(request, 'Security.html', {'form': ApplicationForm})


def aboutplatform(request):
    return render(request, 'AboutPlatform.html', {'form': ApplicationForm})


class ApplicationListCRMView(ListView):
    template_name = 'crm.html'
    queryset = ApplicationModel.objects.all()
    model = ApplicationModel
    context_object_name = 'Applications'


