from .models import Console, Game
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from django.urls import reverse, reverse_lazy
from .forms import UserForm

class IndexView(generic.ListView):
    template_name = 'games/index.html'
    context_object_name = 'all_consoles'

    def get_queryset(self):
        return Console.objects.all()


class AllGames(generic.ListView):
    template_name = 'games/all_games.html'
    context_object_name = 'all_games'

    def get_queryset(self):
        return Game.objects.all()


class ConsoleGames(generic.DetailView):
    model = Console
    template_name = 'games/console_games.html'


class ConsoleCreate(CreateView):
    model = Console
    fields = ['name', 'publisher', 'image', 'description']


class ConsoleUpdate(UpdateView):
    model = Console
    fields = ['name', 'publisher', 'image', 'description']


class ConsoleDelete(DeleteView):
    model = Console
    success_url = reverse_lazy('games:index')


class GameDetail(generic.DetailView):
    model = Game
    template_name = 'games/game_detail.html'


class GameCreate(CreateView):
    model = Game
    fields = ['name', 'console', 'year', 'genre', 'image', 'description']


class GameUpdate(UpdateView):
    model = Game
    fields = ['name', 'console', 'year', 'genre', 'image', 'description']


class GameDelete(DeleteView):
    model = Game
    success_url = reverse_lazy('games:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'games/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # normalised - for dates for example
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return user object if correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('games:index')

        return render(request, self.template_name, {'form': form})

#
# def index(request):
#     all_consoles = Console.objects.all()
#     return render(request, 'games/index.html', {'all_consoles': all_consoles})
#
#
# def console_games(request, console_id):
#     console = get_object_or_404(Console, id=console_id)
#     return render(request, 'games/console_games.html', {'console': console})
#
#
# def game_detail(request, game_id):
#     game = get_object_or_404(Game, id=game_id)
#     return render(request, 'games/game_detail.html', {'game': game})
#
#
# def completed(request, game_id):
#     game = get_object_or_404(Game, id=game_id)
#     game.completed = not game.completed
#     game.save()
#     return render(request, 'games/game_detail.html', {'game': game})
#
#
