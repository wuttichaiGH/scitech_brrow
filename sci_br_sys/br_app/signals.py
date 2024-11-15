from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

# สร้าง UserProfile อัตโนมัติเมื่อสร้าง User
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # เมื่อ User ถูกสร้างครั้งแรก สร้าง UserProfile ใหม่
        UserProfile.objects.create(user=instance)
    else:
        # เมื่อ User ถูกอัพเดต ให้บันทึก UserProfile ถ้ามีการเปลี่ยนแปลง
        instance.profile.save()
