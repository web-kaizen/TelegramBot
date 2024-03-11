from django.db import models


class User(models.Model):

    TARIFF_CHOICES = [
        ('Basic', 'Базовый'),
        ('Professional', 'Профессиональный'),
        ('Premium', 'Премиум'),
        ('Startup', 'Стартап'),
        ('Corporate', 'Корпоративный'),
    ]

    user_id = models.BigIntegerField(blank=True, null=True)
    user_core_id = models.BigIntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    password = models.CharField(max_length=255)
    balance = models.FloatField(blank=True, null=True)
    tariff = models.CharField(max_length=120, choices=TARIFF_CHOICES, default="Basic")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_id} | {self.email} | {self.created_at}"

    class Meta:
        ordering = ["id"]
        verbose_name = "User"
        verbose_name_plural = "Users"


class UserStatistic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model_id = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    current_dialogues = models.IntegerField(default=0)
    max_dialogues = models.IntegerField()

    def __str__(self):
        return f"{self.user} | {self.model_id} | {self.name}"

    class Meta:
        ordering = ["user_id"]
        verbose_name = "UserStatistic"
        verbose_name_plural = "UserStatistics"
