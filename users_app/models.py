from django.db import models
# Create your models here.
class users_list(models.Model):
    name=models.CharField(max_length=50,default=None)
    def __str__(self):
        return self.name

class owes(models.Model):
    name=models.ForeignKey(users_list, null=True, blank=True,on_delete=models.CASCADE)
    sachin=models.IntegerField(default=None)
    rahul=models.IntegerField(default=None)
    deepak=models.IntegerField(default=None)
    # owes_amount=models.IntegerField(default=None)


class owed_by(models.Model):
    name=models.ForeignKey(users_list, null=True, blank=True,on_delete=models.CASCADE)
    sachin=models.IntegerField(default=None)
    rohit=models.IntegerField(default=None)
    # owed_amount=models.IntegerField(default=None)

    # def __str__(self):
    #     return self.owed_name
class balance(models.Model):
    name=models.ForeignKey(users_list,null=True,blank=True,on_delete=models.CASCADE)
    balance=models.IntegerField(default=None)