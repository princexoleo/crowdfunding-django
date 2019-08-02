from django.db import models
from django.contrib.auth.models import User

# Create your models here.
PURPOSE_TYPE = {
    ('SP','startup'),
    ('ME','medical'),
    ('EU','education'),
}
STATUS_CHOICE ={
    (True, 'accepted'),
    (False, 'not accepted')
}
class Donation(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    amount  = models.IntegerField()
    purpose = models.CharField(max_length=2, choices=PURPOSE_TYPE)
    status  = models.BooleanField(choices=STATUS_CHOICE, null=True)

    def __str__(self):
        return self.user.username
    def donation_amount(self):
        return self.amount
    def donation_purpose(self):
        return self.purpose
    

