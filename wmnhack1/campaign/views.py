from django.shortcuts import render, redirect
from .models import Campaign
from .forms import WaterForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.utils import timezone
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def issue_list(request):
    return render(request, 'issues/issue_list.html')

def water_campaign_new(request):
    if request.method == "POST":
        #hform = HashtagForm(request.POST, instance=Hashtag())
        waterpform = WaterForm(request.POST,request.FILES, instance=Campaign())
        if waterpform.is_valid():

            new_water_campaign = waterpform.save(commit=False)
            new_water_campaign.iname = "Water Conservation"
            new_water_campaign.date = timezone.now()
            new_water_campaign.save()
            return redirect('campaign_detail', pk=new_water_campaign.pk)
        return render(request, 'campaign/water/campaign_list.html', {})
    else:
        #hform = HashtagForm(instance = Hashtag())
        waterpform = WaterForm(instance=Campaign())
    return render(request, 'campaign/water/create_campaign.html', {'water_campaign_form': waterpform})

def water_campaign_list(request):
    watercampaigns = Campaign.objects.filter(iname="Water Conservation")
    return render(request, 'campaign/water/campaign_list.html', {'watercampaigns': watercampaigns})

def water_campaign_detail(request, pk):
    watercampaign = get_object_or_404(Campaign, pk=pk)
    return render(request, 'campaign/water/campaign_detail.html', {'watercampaign': watercampaign})

class WaterCampaignDelete(DeleteView):
    template_name = 'campaign/water/campaign_delete.html'
    model = Campaign
    success_url = 'watercampaigns/'

def water_campaign_delete(request, pk, title):
    waterform = Campaign.objects.get(title=title).delete()
    return render(request, 'campaign/water/campaign_delete.html', {'water_form': waterform})

def issue_water(request):
    return render(request, 'issues/water.html')
