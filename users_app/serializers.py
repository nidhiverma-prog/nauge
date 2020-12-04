from users_app.models import *
from rest_framework import serializers

class OwesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = owes
        # name=owes.objects.values_list('owes_amount',flat=True).get(pk=1)
        # print(name)
        fields = ['sachin','rahul','deepak']
class OwedbySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = owed_by
        fields = ['sachin', 'rohit',]
class BalanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = balance
        fields=['balance']
class ModelSerializer(serializers.HyperlinkedModelSerializer):
    owes = OwesSerializer(many=True,read_only=True,source='owes_set')
    owed_by=OwedbySerializer(many=True,read_only=True,source='owed_by_set')
    balance=BalanceSerializer(many=True,read_only=True,source='balance_set')
    class Meta:
        model=users_list
        fields=['name','owes','owed_by','balance']
        
    

class UpdateSerializer(serializers.HyperlinkedModelSerializer):
    lender=serializers.CharField(style={'input_type':'text'},write_only=True)
    borrower=serializers.CharField(style={'input_type':'text'},write_only=True)
    amount=serializers.IntegerField(style={'input_type':'integer'},write_only=True)
    data=ModelSerializer(many=True,read_only=True,source='users_list_set')
    class Meta:
        model=owes,owed_by
        fields=['lender','borrower','amount','data']   
