from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class Car(models.Model):
    title = models.CharField(max_length=100) 
    description = models.TextField()
    image = CloudinaryField('image')
    started_bid = models.DecimalField(max_digits=5, decimal_places=2)
    end_auction = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    Winner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='buyer')
    is_auction_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.owner}-{self.title}' 
    
class Bid(models.Model):  # Renamed from Big to Bid for clarity
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='bids')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.car} - {self.user} - {self.amount}'

