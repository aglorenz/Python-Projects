from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProfileForm
from .models import Profile


# Create your views here.
def admin_console(request):
    profiles = Profile.objects.all()
    # for profile in profiles:
    #     print(profile.first_name)
    return render(request, 'profiles/profiles_page.html', {'profiles': profiles})


def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Profile, pk=pk)
    form = ProfileForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('admin_console')
        else:
            print(form.errors)
    else:
        return render(request, 'profiles/present_profile.html', {'form': form})


def delete(request, pk):
    pk = int(pk)
    print("hi there")
    item = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        item.delete()
        print("deleting profile delete method")
        return redirect('admin_console')
    context = {"item": item, }
    return render(request, 'profiles/confirm_delete.html', context)


# def confirmed(request):
#     print("Entering confirmed method")
#     if request.method == 'POST':
#         print("Confirm method POST")
#         # creates form instance and binds data to it
#         form = ProfileForm(request.POST or None)
#         if form.is_valid():
#             print("deleting profile confirmed method")
#             form.delete()
#             return redirect('admin_console')
#         else:
#             print("not deleting profile confirmed method")
#             return redirect('admin_console')


def add_profile(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin_console')
    else:
        print(form.errors)
        form = ProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'profiles/add_profile.html', context)
