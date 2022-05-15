from django.shortcuts import render

# Create your views here.
def thank_you(request):
    return render(request, 'cars/thankyou.html')

def review(request):
    return render(request, 'cars/rental_review.html')