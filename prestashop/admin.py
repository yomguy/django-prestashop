from django.contrib import admin
from presta.models import PsCustomer
from eve.views import Presta2Eve
from eve.utils import Logger


class StudentAdmin(admin.ModelAdmin):

    model = PsCustomer
    search_field = ['id_customer', 'firstname', 'lastname', 'email',]
    actions = ['copy_to_eve',]

    def copy_to_eve(self, request, queryset):
        for customer in queryset:
            p2e = Presta2Eve(customer)
            p2e.run()

    copy_to_eve.short_description = "Copy to Eve"
