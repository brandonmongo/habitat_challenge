from django.contrib import admin
from .models import TenderResult

# Register your models here.


class TenderResultAdmin(admin.ModelAdmin):
    list_display = (
        "Market_Name",
        "Unique_bid_number",
        "Delivery_Date"
    )

    ordering = ("pk",)


admin.site.register(TenderResult, TenderResultAdmin)
