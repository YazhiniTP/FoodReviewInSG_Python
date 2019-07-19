from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Review,Hotel,Category
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import ReviewForm
import datetime


def review_list(request):
    latest_review_list=Review.objects.order_by('-pub_date')[:9]
    context={
        'latest_review_list': latest_review_list
    }
    return render(request,'reviews/review_list.html',context)

def review_detail(request,review_id):
    review=get_object_or_404(Review,pk='review_id')
    return render(request,'reviews/review_detail.html',{'-review': review})

def hotel_list(request):
    hotel_list=Hotel.objects.order_by('name')
    context={
        'hotel_list':hotel_list
    }
    return render(request,'reviews/hotel_list.html',context)

def hotel_detail(request,hotel_id):
    hotel=get_object_or_404(Hotel,pk=hotel_id)
    return render(request,'reviews/hotel_detail.html',{'hotel':hotel})

def add_review(request, hotel_id):
    hotel = get_object_or_404(Wine, pk=hotel_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = form.cleaned_data['user_name']
        review = Review()
        review.hotel = hotel
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('reviews:hotel_detail', args=(hotel.id,)))

    return render(request, 'reviews/hotel_detail.html', {'hotel': hotel, 'form': form})
# Create your views here.
