from django.db.models.signals import post_save, post_init
from django.dispatch import receiver

from telegram_bot.models import UserStatistic, User


@receiver(post_save, sender=User)
def set_max_dialogues(sender, instance, *args, **kwargs):
    tariff_dialogues_options = {
        'Gpt-3.5 4K': {
            'Basic': 50,
            'Professional': 300,
            'Premium': 500,
            'Startup': 750,
            'Corporate': 3000
        },
        'Gpt-3.5 16K': {
            'Basic': 10,
            'Professional': 30,
            'Premium': 50,
            'Startup': 75,
            'Corporate': 300
        },
        'Gpt-4 8K': {
            'Basic': 1,
            'Professional': 3,
            'Premium': 5,
            'Startup': 7,
            'Corporate': 15
        },
        'Gpt-4 32K': {
            'Basic': 1,
            'Professional': 3,
            'Premium': 5,
            'Startup': 7,
            'Corporate': 15
        }
    }

    for index, (key, value) in enumerate(tariff_dialogues_options.items()):
        max_dialogues_by_tariff = value.get(instance.tariff)

        # Пытаемся получить объект UserStatistic по условиям фильтрации
        user_stat, created = UserStatistic.objects.get_or_create(
            user_id=instance.id,
            model_id=index + 1,
            name=key,
            defaults={'max_dialogues': max_dialogues_by_tariff}
        )

        # Если объект не был создан, обновляем поле max_dialogues
        if not created:
            user_stat.max_dialogues = max_dialogues_by_tariff
            user_stat.save()


