from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
Donation_Type ={
    ('GD','Giving Donation'),
    ('RD','Receiving Donations'),
}
PURPOSE_TYPE = {
    ('SP','startup'),
    ('ME','medical'),
    ('EU','education'),
}
STATUS_CHOICE ={
    (True, 'accepted'),
    (False, 'not accepted')
}
Transaction_Status ={
    (True, 'Transaction completed'),
    (False, 'Transaction not completed')
}
class Donation(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    amount  = models.IntegerField()
    purpose = models.CharField(max_length=2, choices=PURPOSE_TYPE)
    status  = models.BooleanField(choices=STATUS_CHOICE, null=True)
    transaction_status  = models.BooleanField(choices=Transaction_Status, default=False)
    donate_type = models.CharField(max_length=2, choices=Donation_Type)
    created_date = models.DateTimeField(default= timezone.now)

    def __str__(self):
        return self.user.username
    def donation_amount(self):
        return self.amount
    def donation_purpose(self):
        return self.purpose
    def donation_type(self):
        return self.donate_type
    def donation_status(self):
        return self.status
    def donation_transaction_status(self):
        return self.transaction_status
    def donation_created_date(self):
        return self.created_date
    

