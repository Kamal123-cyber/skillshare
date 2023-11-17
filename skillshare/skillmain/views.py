from django.views.generic import TemplateView, DetailView
from django.shortcuts import render, redirect
from skillapp.models import UserProfile

class HomePage(TemplateView):
    template_name = 'skillmain/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        results = None
        if query:
            results = UserProfile.objects.filter(skills_offered__name__icontains=query)
        context['results'] = results
        context['query'] = query
        return context

    def post(self, request, *args, **kwargs):
        query = request.POST.get('q')
        if query:
            results = UserProfile.objects.filter(skills_offered__name__icontains=query)
            return render(request, 'skillmain/search_results.html', {'results': results, 'query': query})
        else:
            return redirect('home')

class SkillUserDetailView(DetailView):
    template_name = 'skillmain/userskilldetail.html'
    model = UserProfile
    context_object_name = 'user'
