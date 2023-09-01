from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectF
from django.contrib.auth.decorators import login_required


def projects(request):
    pr = Project.objects.all()
    context = {
        'projects': pr
    }
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    return render(request, "projects/single-project.html", {'project': project_obj})


@login_required(login_url="login")
def create_project(request):
    form = ProjectF()

    if request.method == 'POST':
        form = ProjectF(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    return render(request, 'projects/form-template.html', {'form': form})
