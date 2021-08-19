from django.db import models
from django.db.models.base import Model

# Create your models here.
class tv_show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField(auto_now=False,auto_now_add=False)
    desc = models.TextField()
    zelda = models.CharField(max_length=500, default='https://media2.giphy.com/media/8L0Pky6C83SzkzU55a/giphy.gif?cid=ecf05e47mnvcxnlgry2pnecdjoe54nzctn9h5naumw04xddv&rid=giphy.gif&ct=g')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)