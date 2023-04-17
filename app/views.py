from .models import *
from django.views.generic import ListView, DetailView, CreateView
from .forms import *
from django.urls import reverse
from django.shortcuts import render


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

    def get_success_url(self):
        return reverse('success')
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


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


