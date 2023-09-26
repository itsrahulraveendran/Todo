from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import todoform
from django.views.generic import ListView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


# Create your views here.
def home(request):
    display_page = Task.objects.all()
    if request.method == 'POST':
        homename = request.POST.get('task', '')
        homepriority = request.POST.get('priority', '')
        homediscription = request.POST.get('discription')
        homedate = request.POST.get('date')
        task = Task(name=homename, priority=homepriority, discription=homediscription, date=homedate, )
        task.save()
    return render(request, 'home.html', {'Task': display_page})


# def details(request):
#     task=Task.objects.all()
#     return render(request,'details.html',{'Task':task})
def delete(request, delete_task):
    del_task = Task.objects.get(id=delete_task)
    if request.method == 'POST':
        del_task.delete(),
        return redirect('/')
    return render(request, 'delete.html')


def update(request, update_data):
    up_data = Task.objects.get(id=update_data)
    forform = todoform(request.POST or None, instance=up_data)
    if forform.is_valid():
        forform.save()
        return redirect('/')
    return render(request, 'update.html', {'form_data': forform, 'task_data': up_data})


class tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'Task'


class detailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'
class updateview(UpdateView):
    model=Task
    template_name='edit.html'
    context_object_name='task'
    fields=('name','priority','discription','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class deleteview(DeleteView):
    model=Task
    template_name='delete.html'
    success_url = reverse_lazy('cbvhome')
