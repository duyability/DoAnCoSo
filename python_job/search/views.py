from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from vlance.models import Job


def search(request):

    vl = Job.objects.all()

    search = request.GET.get('q')
    if search:
        vl = vl.filter(
            Q(title__icontains=search) | Q(description__icontains=search)

        )
    tp = request.GET.get('thanhpho')
    if tp:
        vl = vl.filter(
            Q(Thanh_Pho__in=tp)

        )

    nn = request.GET.get('nganhnghe')
    if tp:
        vl = vl.filter(
            Q(Nganh_Nghe__in=nn)

        )

    context = {
        "vl": vl,
        "search": search,
        "tp": tp,
        "nn": nn,
    }
    return render(request, 'layout/search_job.html', context)
