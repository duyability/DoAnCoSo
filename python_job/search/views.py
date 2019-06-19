from django.shortcuts import render
from django.db.models import Q
from vlance.models import Job, NganhNghe, ThanhPho, JobPartTime


def search(request):
    NN = NganhNghe.objects.all()
    tp = ThanhPho.objects.all()
    vl = Job.objects.all()

    search = request.GET.get('q')
    if search:
        vl = vl.filter(
            Q(title__icontains=search) | Q(description__icontains=search)
        )

    stp = request.GET.get('thanhpho')
    if stp:
        vl = vl.filter(
            Q(Thanh_Pho__in=stp)
        )

    nn = request.GET.get('nganhnghe')
    if nn:
        vl = vl.filter(
            Q(Nganh_Nghe__in=nn)
        )

    context = {
        "vl": vl,
        "search": search,
        "stp": stp,
        "tp": tp,
        "nn": nn,
        "NN": NN,
    }
    return render(request, 'layout/search_job.html', context)


def search_onsite(request):
    NN = NganhNghe.objects.all()
    tp = ThanhPho.objects.all()
    JPT = JobPartTime.objects.all()

# tim theo title
    search = request.GET.get('q')
    if search:
        JPT = JPT.filter(
            Q(title__icontains=search) | Q(description__icontains=search)| Q(company_name__icontains=search)

        )
# tim theo so nam kinh nghiem
    year_exp = request.GET.get('year_exp')
    if year_exp:
        JPT = JPT.filter(
            Q(year_exp__icontains=year_exp)

        )
#Hinh thuc lam viec
    location = request.GET.get('location')
    if year_exp:
        JPT = JPT.filter(
            Q(location__icontains=location)

        )
# thanh pho
    stp = request.GET.get('thanhpho')
    if stp:
        JPT = JPT.filter(
            Q(Thanh_Pho__in=stp)

        )
# nganh nghe
    nn = request.GET.get('nganhnghe')
    if nn:
        JPT = JPT.filter(
            Q(Nganh_Nghe__in=nn)

        )

    context = {
        "JPT": JPT,
        "search": search,
        "stp": stp,
        "tp": tp,
        "nn": nn,
        "NN": NN,
        "year_exp": year_exp,
        "location": location,
    }
    return render(request, 'layout/search_job_onsite.html', context)
