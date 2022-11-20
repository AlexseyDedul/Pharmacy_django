from django.contrib import admin

from app.models import *

# Register your models here.


class PharmacyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'state_number')


class AddressAdmin(admin.ModelAdmin):
    list_display = ('country', 'city', 'street', 'number')


class ReleaseFormAdmin(admin.ModelAdmin):
    list_display = ('name', )


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number')


class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'treatment')


class MedicamentAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'form_release', 'disease', 'manufacturer', 'dosage')


class MedicamentInPharmacyAdmin(admin.ModelAdmin):
    list_display = ('pharmacy', 'medicament', 'number', 'price')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('pharmacy', 'date', 'reason', 'total_price', 'writeoff')


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('order', 'reason', 'total_price')


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'reason', 'total_price')


admin.site.register(Pharmacy, PharmacyAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(ReleaseForm, ReleaseFormAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Disease, DiseaseAdmin)
admin.site.register(Medicament, MedicamentAdmin)
admin.site.register(MedicamentInPharmacy, MedicamentInPharmacyAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Application)
