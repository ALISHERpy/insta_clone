# signalssss
from django.db.models.signals import post_save,post_delete
from django.dispatch import Signal,receiver
# signalsss
from django.contrib.auth.models import User
from users_profile.models import Profile





# profile yaratadi,user yaratilgan vaqtida

@receiver(post_save, sender=User)
def profile_creator(sender,instance,created,**kwargs):
    print(f"INFO:\nsender: {sender}\ninctance:{instance}\ncreated:{created}\n\n")

    if created:
        print("Yay,user has just created !!")
        
        Profile.objects.create(
            user=instance
        )
    else:
        my_obj=Profile.objects.get(user=instance)
        my_obj.first_name=f"{instance.first_name}/////{instance.last_name}"
        my_obj.last_name=f"ism: {instance.first_name} ////"
        my_obj.bio=f"bog'lanish uchun: {instance.email}"
        my_obj.save()

@receiver(post_delete, sender=Profile)
def user_delete(sender,instance,**kwargs):
    print(f"INFO:\nsender: {sender}\ninctance:{instance}\n\n")
    my_obj=instance.user
    my_obj.delete()


# Signal.connect(post_save,profile_creator,sender=User)

# Signal.connect(post_delete,user_delete,sender=Profile)