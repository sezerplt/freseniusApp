from django.db import models
# Create your models here.
class WorkUser(models.Model):
    userName=models.CharField(blank=True,null=True,max_length=300)
    telNumber=models.CharField(blank=True,null=True,max_length=300)
    def __str__(self) -> str:
        return self.userName
class WorkTime(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    

    def __str__(self) -> str:
        return f"{self.start_time} {self.end_time}"

class WorkDate(models.Model):
    startWorkDate=models.DateField(blank=True,null=True)
    time = models.ForeignKey(WorkTime,on_delete=models.CASCADE)
    user=models.ManyToManyField(WorkUser)
    
    def __str__(self) -> str:
        return f"{self.startWorkDate}"

