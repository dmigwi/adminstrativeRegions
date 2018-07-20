from django.db import models
from django.utils import timezone

# BaseModel defines the abstract model that contains the common properties 
# between the various administrative region models.
class BaseModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


    def __str__(self):
        return self.name

# CountyModel defines the county administrative region model that is the top most.
# It is on top of constituency and ward level.
class CountyModel(BaseModel):
    class Meta:
        db_table = 'county'

# ConstituencyModel defines the constituency administrative region model that is the second
# top most. It is lower than county but higher than ward level.
class ConstituencyModel(BaseModel):
    county = models.ForeignKey(CountyModel, related_name='constituencies', on_delete=models.CASCADE)

    class Meta:
        db_table = "constituency"

# WardModel defines the ward administrative region model that is the lowest.
# It is lower than county and constituency levels.
class WardModel(BaseModel):
    constituency = models.ForeignKey(ConstituencyModel, related_name='wards', on_delete=models.CASCADE)

    class Meta:
        db_table = "ward"

