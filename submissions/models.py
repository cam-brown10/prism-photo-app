from django.db import models

class Submission(models.Model):
    student_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='submissions/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} - {self.image.name}"

