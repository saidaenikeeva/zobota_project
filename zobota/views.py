from django.shortcuts import render


def profile(request):
    return render(request, "profile.html")

def saveprofile(request):

    print(request.POST['name'])
    print(request.POST['age_number'])
    print(request.POST['microcalcinate'])
    print(request.POST['solidity'])
    print(request.POST['echogenicity'])
    print(request.POST['contours'])
    print(request.POST['blood flow1'])
    print(request.POST['blood flow2'])
    print(request.POST['verticalization'])
    print(request.POST['histology'])
    print(request.POST['date'])

    return render(request, "profile.html")