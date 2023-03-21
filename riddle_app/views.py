from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import FormView, ListView, DetailView, TemplateView
from django.urls import reverse_lazy

from .models import Riddle
from .forms import NewRiddleForm, GuessRiddleForm

#### class based views

class IndexView(TemplateView):
    template_name = "index.html"


class NewRiddleForm(FormView):
    template_name = "new_riddle_form.html"
    form_class = NewRiddleForm
    success_url = reverse_lazy('index')


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class RiddleListView(ListView):
    model = Riddle
    template_name = "riddle_list.html"

    queryset = Riddle.objects.all()

class RiddleDetailView(DetailView):
    model = Riddle
    template_name = "riddle_detail.html"


#### function based views

def riddle_like(request, pk):
    riddle = Riddle.objects.get(id=pk)
    riddle.increase_likes()

    return HttpResponseRedirect(reverse_lazy('riddle-detail', args=[str(pk)]))


def guess_riddle(request,pk):
    riddle = Riddle.objects.get(id=pk)

    if request.method == 'POST':

        context = {
            'riddle': riddle,
            'has_message': True,
            'message': '',
            'pk': riddle.id
            }

        form = GuessRiddleForm(request.POST)
        if form.is_valid():
            form_cleaned= form.cleaned_data

            print(riddle.check_guess(form_cleaned['guess']))
                  
            context['message'] = riddle.check_guess(form_cleaned['guess'])

            return render(request, 'riddle_guess.html', context)
            return HttpResponseRedirect(reverse_lazy('riddle-guess', kwargs=context))
            # return redirect(reverse_lazy('riddle-guess', dwars=[str(pk)]))

    else:
        context = {
            'riddle': riddle,
            'form': GuessRiddleForm()
            }
        
        return render(request, 'riddle_guess.html', context)