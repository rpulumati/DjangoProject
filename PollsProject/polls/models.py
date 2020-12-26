from django.db import models


# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=300)

    option1 = models.TextField(max_length=30)
    option2 = models.TextField(max_length=30)
    option3 = models.TextField(max_length=30)

    option1_count = models.IntegerField(default=0)
    option2_count = models.IntegerField(default=0)
    option3_count = models.IntegerField(default=0)

    class Meta:
        db_table = 'PGT_Polls'
        order_with_respect_to = 'question'
        indexes = [
            models.Index(fields=['question'])
        ]

    def totalVotes(self):
        return self.option1_count + self.option2_count + self.option3_count
