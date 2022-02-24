from django.db import models

# Create your models here.
class personal_details(models.Model):
    name = models.TextField(
        max_length = 512,
        null=False,
    )
    aadhaar_number = models.CharField(max_length=12, blank=True, null=False, primary_key=True)
    dob = models.DateTimeField(
        auto_now_add = False,
    )
    phone_no = models.CharField(max_length=12, blank=True, null=False)
    address  = models.TextField(
        max_length = 512,
        null=False,
    )
    class Meta:
        verbose_name = "Personal_Details"
        verbose_name_plural = "Personal_Details"
    
    

    
class id_card(models.Model):
    name = models.TextField(
        max_length = 512,
        null=False,
    )
    sex = models.CharField(max_length=12, blank=True, null=False, primary_key=True)
    
    aadhaar_number_fk = models.ForeignKey(personal_details, on_delete= models.CASCADE)
    def __str__(self):
        return self.name

class travel_details(models.Model):
    aadhaar_number_fk = models.ForeignKey(personal_details, on_delete= models.CASCADE)
    travelling_from = models.TextField(
        max_length = 512,
        null=False,
    )
    travelling_to = models.TextField(
        max_length = 512,
        null=False,
    )
    
   

class health_details(models.Model):
    aadhaar_number_fk = models.ForeignKey(personal_details, on_delete=models.CASCADE)
    travelling_from = models.TextField(
        max_length = 512,
        null=False,
    )
    post_coivd_symptoms = models.TextField(
        max_length = 512,
        null=False,
    )
    
    
class vaccination_details(models.Model):
    aadhaar_number_fk = models.ForeignKey(personal_details, on_delete=models.CASCADE)
    first_dose =  models.BooleanField(
        default = False
    )
    second_dose =  models.BooleanField(
        default = False
    )
    booster =  models.BooleanField(
        default = False
    )
    
    