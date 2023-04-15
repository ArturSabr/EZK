from .models import *
from django.views.generic import ListView, DetailView, CreateView
from .forms import *
from django.urls import reverse


class Home(ListView):
    model = NewsModel
    queryset = NewsModel.objects.all().order_by('-created_date')[:3]
    context_object_name = 'news'
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ApplicationForm
        return context

class NewsListView(ListView):
    model = NewsModel
    queryset = NewsModel.objects.all()
    context_object_name = 'news'
    template_name = 'news_list.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


class NewsDetailView(DetailView):
    model = NewsModel
    context_object_name = 'news'
    template_name = 'news_detail.html'

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
    template_name = 'request.html'
    form_class = ApplicationForm

    def get_success_url(self):
        return reverse('success')
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


class ApplicationSendSuccessView(ListView):
    model = ApplicationModel
    context_object_name = 'application'
    template_name = 'success.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context




