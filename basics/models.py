from django.db import models


class Todo(models.Model):
    text = models.CharField(max_length=255)
    done = models.BooleanField(default=False)

    def __str__(self):
        string = self.text
        if self.done:
            string = f'Done. ~{string}~'
        return string

    def mark_as_done(self):
        self.done = True
        self.save()

    def mark_as_not_done(self):
        self.done = False
        self.save()
