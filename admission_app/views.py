from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import InternatDocuments
from django.contrib import messages
from .forms import InternatForm
from django.http import HttpResponseRedirect


def main_page(request):
    student_data = InternatDocuments.objects.all()
    return render(request, 'index.html', {'student_data' : student_data})


def student_detail(request, id):
    student = InternatDocuments.objects.get(pk=id)
    return render(request, 'student_detail.html', {'student': student})


def upload_files(request):
    if request.method == "POST":
        form = InternatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admission_app:main_page')
        else:
            return HttpResponse("Form is not valid")
    else:
        form = InternatForm()
    return render(request, 'upload.html', {'form': form})





            # first_name = request.POST.get('first_name')
            # last_name = request.POST.get('last_name')
            # category = request.POST.get('category')
            # oblast = request.POST.get('oblast')
            # gender = request.POST.get('gender')
            # copy_svid_rozh = request.FILES["copy_svid_rozh"]
            # copy_vkl_roj_IIN = request.FILES["copy_vkl_roj_IIN"]
            # copy_udos_lich = request.FILES["copy_udos_lich"]
            # copy_udos_lich_rod = request.FILES["copy_udos_lich_rod"]
            # adress_reg_vseh = request.FILES["adress_reg_vseh"]
            # copy_prikaz_rab = request.FILES["copy_prikaz_rab"]
            # sprv_akima_or_egov = request.FILES["sprv_akima_or_egov"]
            # sprv_rab_zrpl_or_mest_ispol_org = request.FILES["sprv_rab_zrpl_or_mest_ispol_org"]
            # inform_gnpf = request.FILES["inform_gnpf"]
            # copy_svd_rozh_mnodet = request.FILES["copy_svd_rozh_mnodet"]
            # sprv_invd = request.FILES["sprv_invd"]
            # sprv_asp = request.FILES["sprv_asp"]
            # sprv_neblag_semya = request.FILES["sprv_neblag_semya"]
            # copy_doc_nepol_semya = request.FILES["copy_doc_nepol_semya"]
            # documents = InternatDocuments.objects.create(first_name=first_name, last_name=last_name, category=category,
            #                                              oblast=oblast, gender=gender, copy_svid_rozh=copy_svid_rozh,
            #                                              copy_vkl_roj_IIN=copy_vkl_roj_IIN,
            #                                              copy_udos_lich=copy_udos_lich,
            #                                              copy_udos_lich_rod=copy_udos_lich_rod,
            #                                              adress_reg_vseh=adress_reg_vseh,
            #                                              copy_prikaz_rab=copy_prikaz_rab,
            #                                              sprv_akima_or_egov=sprv_akima_or_egov,
            #                                              sprv_rab_zrpl_or_mest_ispol_org=sprv_rab_zrpl_or_mest_ispol_org,
            #                                              inform_gnpf=inform_gnpf,
            #                                              copy_svd_rozh_mnodet=copy_svd_rozh_mnodet,
            #                                              sprv_invd=sprv_invd, sprv_asp=sprv_asp,
            #                                              sprv_neblag_semya=sprv_neblag_semya,
            #                                              copy_doc_nepol_semya=copy_doc_nepol_semya)
            # documents.save()
            # messages.success(request, "Ваша документы успешно загружено")
















