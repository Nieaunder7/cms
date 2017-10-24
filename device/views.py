from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccessPointCreateForm,SettopboxCreateForm,RemoteControllerCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, UpdateView, TemplateView
from django.core.urlresolvers import reverse_lazy 
from .models import BaseDevice, Settopbox, AccessPoint, RemoteController
import logging

logger = logging.getLogger(__name__)

# def device_list(request):
#     devices = BaseDevice.objects.all()
#     param = {
#         'title':"장치 리스트", 
#         'devices':devices
#         }
#     return render(request, 'device_list.html', param)

def device_list(request):
    devices_stb = Settopbox.objects.all()
    devices_ap = AccessPoint.objects.all()
    devices_rc = RemoteController.objects.all()
    param = {
        'title':"장치 리스트", 
        'devices_stb':devices_stb,
        'devices_ap':devices_ap,
        'devices_rc':devices_rc
        }
    return render(request, 'device_list.html', param)

##장비 추가(STB,AP,리모컨)
def device_add(request,types):
    try :
        if request.method == "POST":
            if types == "STB":
                forms = SettopboxCreateForm(request.POST)
                if forms.is_valid():
                    forms.save()
                    return redirect('device:device_list')
            elif types == "AP":
                forms = AccessPointCreateForm(request.POST)
                if forms.is_valid():
                    forms.save()
                    return redirect('device:device_list')
            elif types == "RC":
                forms = RemoteControllerCreateForm(request.POST)
                if forms.is_valid():
                    logger.error("리모컨 폼")
                    forms.save()
                    logger.error("리모컨 등록")
                    return redirect('device:device_list')          
        else :
            if types == "STB" :
                forms = SettopboxCreateForm()
                name = "STB 등록"
                types = "STB"
                return render(request, 'basedevice_form.html',{'form':forms,'name':name,'types':types})
            elif types == "AP" :
                forms = AccessPointCreateForm()
                name = "AP 등록"
                types = "AP"
                return render(request, 'basedevice_form.html',{'form':forms,'name':name,'types':types})
            elif types == "RC" :
                forms = RemoteControllerCreateForm()
                name = "리모컨 등록"
                types = "RC"
                return render(request, 'basedevice_form.html',{'form':forms,'name':name,'types':types}) 
    except Exception as e :
        logger.error(e)

## 장비 수정(STB,AP,리모컨)
def device_update(request,types,pk):
    try:
        if request.method == "POST":
             if types == "STB":
                model = get_object_or_404(Settopbox,pk=pk)
                forms = SettopboxCreateForm(request.POST,instance=model)
                if forms.is_valid():
                    forms.save()
                    return redirect('device:device_list')
             elif types == "AP":
                model = get_object_or_404(AccessPoint,pk=pk)
                forms = AccessPointCreateForm(request.POST,instance=model)
                if forms.is_valid():
                    forms.save()
                    return redirect('device:device_list') 
             elif types == "RC":
                model = get_object_or_404(RemoteController,pk=pk)
                forms = RemoteControllerCreateForm(request.POST,instance=model)
                if forms.is_valid():
                    forms.save()
                    return redirect('device:device_list')                                               
        else :
            if types == "STB" :
                model = get_object_or_404(Settopbox,pk=pk)
                forms = SettopboxCreateForm(instance=model)
                name = "STB 수정"
                types = "STB"
                return render(request, 'basedevice_form.html',{'form':forms,'name':name,'types':types})
            elif types == "AP" :
                model = get_object_or_404(AccessPoint,pk=pk)
                forms = AccessPointCreateForm(instance=model)
                name = "AP 수정"
                types = "AP"
                return render(request, 'basedevice_form.html',{'form':forms,'name':name,'types':types})
            elif types == "RC" :
                model = get_object_or_404(RemoteController,pk=pk)
                forms = RemoteControllerCreateForm(instance=model)
                name = "리모컨 수정"
                types = "RC"
                return render(request, 'basedevice_form.html',{'form':forms,'name':name,'types':types})            
    except Exception as e:
        logger.error(e)

def device_delete(request,types,pk):
    if types == "STB":
        device = Settopbox.objects.filter(pk=pk).delete()
        return redirect('device:device_list')
    elif types == "AP":
        device = AccessPoint.objects.filter(pk=pk).delete()
        return redirect('device:device_list')
    elif types == "RC":
        device = RemoteController.objects.filter(pk=pk).delete()
        return redirect('device:device_list')

# class STB_CreateV(CreateView):
#     model = Settopbox
#     ## image field에 추가 하면 생성 안됨.
#     fields=['name', 'model','manufacturer','service','firmware','comment','mac_address']
#     template_name = 'basedevice_form.html'

#     def form_valid(self, form):
#         form.instance.author_id = self.request.user.id
#         if form.is_valid:
#             form.instance.save()
#             return redirect('device:device_list')
#         else :
#             return self.render_to_response({'form':form})

# class STB_UpdateV(UpdateView):
#     model = Settopbox
#     fields=['name', 'model','manufacturer','service','firmware','comment','mac_address']
#     template_name = 'basedevice_form.html'
#     success_url = reverse_lazy('device:device_list')

# class STB_DeleteV(DeleteView):
#     model = Settopbox
#     template_name = 'device_confirm_delete.html'
#     success_url = reverse_lazy('device:device_list')


# class AP_CreateV(CreateView):
#     model = AccessPoint
#     ## image field에 추가 하면 생성 안됨.
#     fields=['name', 'model','manufacturer','service','firmware','comment','mac_address']
#     template_name = 'basedevice_form.html'

#     def form_valid(self, form):
#         form.instance.author_id = self.request.user.id
#         if form.is_valid:
#             form.instance.save()
#             return redirect('device:device_list')
#         else :
#             return self.render_to_response({'form':form})

# class AP_UpdateV(UpdateView):
#     model = AccessPoint
#     fields=['name', 'model','manufacturer','service','firmware','comment','mac_address']
#     template_name = 'basedevice_form.html'
#     success_url = reverse_lazy('device:device_list')

# class AP_DeleteV(DeleteView):
#     model = AccessPoint
#     template_name = 'device_confirm_delete.html'
#     success_url = reverse_lazy('device:device_list')


# class RC_CreateV(CreateView):
#     model = RemoteController
#     ## image field에 추가 하면 생성 안됨.
#     fields=['name', 'model','manufacturer','service','firmware','comment']
#     template_name = 'basedevice_form.html'

#     def form_valid(self, form):
#         form.instance.author_id = self.request.user.id
#         if form.is_valid:
#             form.instance.save()
#             return redirect('device:device_list')
#         else :
#             return self.render_to_response({'form':form})

# class RC_UpdateV(UpdateView):
#     model = RemoteController
#     fields=['name', 'model','manufacturer','service','firmware','comment']
#     template_name = 'basedevice_form.html'
#     success_url = reverse_lazy('device:device_list')

# class RC_DeleteV(DeleteView):
#     model = RemoteController
#     template_name = 'device_confirm_delete.html'
#     success_url = reverse_lazy('device:device_list')