from django.db import models

#getting rid of composite key idea
class Tag_table(models.Model):
    tag_id = models.IntegerField(primary_key=False, null=False)
    serial_num = models.IntegerField(primary_key=False, null=False)
    timestamp = models.DateTimeField(primary_key=False)
    tag_zone = models.IntegerField(primary_key=False, null=False)
    x_pos = models.DecimalField(primary_key=False, decimal_places=2, max_digits=4)
    y_pos = models.DecimalField(primary_key=False, decimal_places=2, max_digits=4)

    def __str__(self):
        return "tagid="+str(self.tag_id)
