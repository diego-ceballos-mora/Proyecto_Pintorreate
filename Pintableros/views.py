# Create your views here.
# Developed with class based views
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from .forms import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from Publicaciones.models import *


def ImageUser(id):
    image = Usuario.objects.get(username = id).avatar
    return image

# Boards details
class BoardView(View):
    template_name='Publicaciones/Boardpub.html'
    
    @method_decorator(login_required)
    def get(self, request, *arg, **kwargs):
        id = self.kwargs['board_id']

        list = Board.objects.get(id=id).FK_Board_Pub.all()
        b = Board.objects.get(id=id)
        return render(request,self.template_name,{'b':b, 'list':list,'image':ImageUser(request.user)})


# List of Boards
class ListBoardView(View):
    template_name='Pintableros/boards.html'

    @method_decorator(login_required)   
    def get(self, request, *args, **kwargs):
        list = Board.objects.all().order_by('-date')
        return render(request, self.template_name, {'list':list,'image':ImageUser(request.user)})


#Add Board
class AddBoardView(View):
    form_class = BoardForm
    template_name = 'Pintableros/newBoard.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        formB = self.form_class()
        return render(request, self.template_name, {'formB': formB, 'user':request.user, 'image':ImageUser(request.user)})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():    
            form.save()
            return redirect('/Pintableros')

        return render(request, self.template_name, {'formB': form})

# Edit Board
class EditBoardView(View):
    form_class = BoardForm
    template_name = 'Pintableros/editBoard.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EditBoardView, self).dispatch(*args, **kwargs)

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        id = self.kwargs['board_id']
        board = get_object_or_404(Board, pk=id)
        formB = self.form_class(instance = board)
        return render(request, self.template_name, {'board':board,'formB': formB,'image':ImageUser(request.user)})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        id = self.kwargs['board_id']
        board = get_object_or_404(Board, pk=id)
        form = self.form_class(request.POST, request.FILES, instance=board)

        if form.is_valid():
             form.save()
             return redirect('/Pintableros/'+id)

        return render(request, self.template_name, {'form': form})

# Delete Board
class DeleteBoardView(View): 

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        id = self.kwargs['board_id']
        b = get_object_or_404(Board, pk=id)
        
        b.delete()

        return redirect('/Pintableros')
