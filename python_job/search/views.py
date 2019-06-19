from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from vlance.models import Job, NganhNghe, ThanhPho


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
    if tp:
        vl = vl.filter(
            Q(Thanh_Pho__in=stp)

        )

    nn = request.GET.get('nganhnghe')
    if tp:
        vl = vl.filter(
            Q(Nganh_Nghe__in=nn)

        )

    context = {
        "vl": vl,
        "search": search,
        "stp": stp,
        "tp": tp,
        "nn": nn,
        "NN" : NN,
    }
    return render(request, 'layout/search_job.html', context)
