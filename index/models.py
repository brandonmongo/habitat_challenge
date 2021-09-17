from django.db import models

# Create your models here.


class tender_result(models.Model):
    Market_Name = models.CharField(max_length=250)
    Delivery_Date = models.CharField(max_length=250)
    Unique_bid_number = models.CharField(max_length=250)
    Response_Unit = models.CharField(max_length=250, null=False, blank=False)
    Unit_type = models.CharField(max_length=250)
    Agent_Or_Applicant = models.CharField(max_length=250)
    Related_Entity = models.CharField(max_length=250)
    Volume_offered = models.IntegerField()
    Volume_Accepted = models.IntegerField()
    Delivery_Start = models.CharField(max_length=250)
    Delivery_End = models.CharField(max_length=250)
    Service_Duration = models.IntegerField()
    Availability_Fee = models.IntegerField()
    Total_Cost = models.IntegerField(null=True, blank=True)
    RTM_Or_no_RTM = models.CharField(max_length=250)
    Accepted_Or_Rejected = models.CharField(max_length=250)
    Rejection_code = models.IntegerField(null=True, blank=True)
    Technology_Type = models.CharField(max_length=250)

    def __str__(self):
        return self.Market_Name
