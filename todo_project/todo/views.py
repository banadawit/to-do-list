from django.shortcuts import render, redirect
from .models import Task, Category
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm

@login_required
def task_list(request):
    category_filter = request.GET.get('category', None)
    tasks = Task.objects.filter(user=request.user)
    if category_filter:
        tasks = tasks.filter(category__name=category_filter)
    categories = Category.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks, 'categories': categories})

class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'completed', 'category']  # Added category
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'completed', 'category']  # Added category
    template_name = 'todo/task_form.html'
    success_url = reverse_lazy('task_list')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'todo/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('login') 
    else:
        form = UserCreationForm()

    return render(request, 'todo/signup.html', {'form': form})
