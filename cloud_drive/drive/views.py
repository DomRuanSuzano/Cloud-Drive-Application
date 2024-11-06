from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm 
from .models import File, Folder
from .forms import FileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import FileResponse

@login_required
def serve_user_file(request, file_id):
    file = File.objects.get(id=file_id)

    return FileResponse(open(file.file.path, 'rb'))

@login_required
def upload_file(request):
    if request.method == "POST":
        if 'file' in request.FILES:
            file = request.FILES['file']
            folder_id = request.POST.get("folder")

            folder = Folder.objects.get(id=folder_id)

            if file.size > 40 * 1024 * 1024:
                return render(request, "drive/upload.html", {"files": File.objects.filter(owner=request.user), "error": "File is too large"})

            total = sum(file.size for file in request.user.files.all())
            if total + file.size > 100 * 1024 * 1024:
                return render(request, "drive/upload.html", {"files": File.objects.filter(owner=request.user), "error": "Storage is full"})

            File.objects.create(owner=request.user, file=file, size=file.size, folder=folder if folder_id else None)
            return redirect("upload_file")

        if 'folder_name' in request.POST:
            folder_name = request.POST.get('folder_name')
            parent_folder_id = request.POST.get('parent_folder')
            
            if folder_name:
                if parent_folder_id:
                    parent_folder = Folder.objects.get(id=parent_folder_id)
                    Folder.objects.create(owner=request.user, name=folder_name, parent=parent_folder)
                else:
                    Folder.objects.create(owner=request.user, name=folder_name)
                return redirect("upload_file")

    files = File.objects.filter(owner=request.user)
    folders = Folder.objects.filter(owner=request.user)

    return render(request, "drive/upload.html", {"files": files, "folders": folders})

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_login")
    else:
        form = CustomUserCreationForm()
    return render(request, "drive/register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("upload_file")
        else:
            messages.error(request, "Invalid username or password")
        
    return render(request, "drive/login.html")

def user_logout(request):
    logout(request)
    return redirect("login")

def account_info(request):
    user = request.user
    file_counts = {
        'images': user.files.filter(type='image').count(),
        'videos': user.files.filter(type='video').count(),
        'documents': user.files.filter(type='document').count(),
    }
    storage_used = sum(file.size for file in user.files.all())

    context = {
        'user': user,
        'file_counts': file_counts,
        'storage_used': storage_used,
    }
    return render(request, 'drive/data.html', context)