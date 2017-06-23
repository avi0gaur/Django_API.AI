from django.db import models

class Chat_Response(models.Model):
     user_id = models.IntegerField()
     bot_response = models.CharField(max_length=1000)
     source_data = models.CharField(max_length=1000)

     def __str__(self):
         return self.source_data