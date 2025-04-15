from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile, PortfolioItem
from .forms import ProfileForm, PortfolioItemForm

@login_required
def dashboard(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        return redirect('profiles:profile')
    return render(request, 'profiles/dashboard.html', {'profile': profile})

@login_required
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None
    return render(request, 'profiles/profile.html', {'profile': profile})

@login_required
def edit_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profiles:profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profiles/edit_profile.html', {'form': form})

@login_required
def add_portfolio_item(request):
    if request.method == 'POST':
        form = PortfolioItemForm(request.POST, request.FILES)
        if form.is_valid():
            portfolio_item = form.save(commit=False)
            portfolio_item.profile = request.user.profile
            portfolio_item.save()
            messages.success(request, 'Portfolio item added successfully!')
            return redirect('profiles:dashboard')
    else:
        form = PortfolioItemForm()
    return render(request, 'profiles/add_portfolio_item.html', {'form': form})

@login_required
def edit_portfolio_item(request, pk):
    portfolio_item = get_object_or_404(PortfolioItem, pk=pk, profile=request.user.profile)
    if request.method == 'POST':
        form = PortfolioItemForm(request.POST, request.FILES, instance=portfolio_item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Portfolio item updated successfully!')
            return redirect('profiles:dashboard')
    else:
        form = PortfolioItemForm(instance=portfolio_item)
    return render(request, 'profiles/edit_portfolio_item.html', {'form': form})

@login_required
def delete_portfolio_item(request, pk):
    portfolio_item = get_object_or_404(PortfolioItem, pk=pk, profile=request.user.profile)
    if request.method == 'POST':
        portfolio_item.delete()
        messages.success(request, 'Portfolio item deleted successfully!')
        return redirect('profiles:dashboard')
    return render(request, 'profiles/delete_portfolio_item.html', {'item': portfolio_item})

def browse_talents(request):
    profiles = Profile.objects.all()
    return render(request, 'profiles/browse_talents.html', {'profiles': profiles})

def view_profile(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'profiles/view_profile.html', {'profile': profile})
