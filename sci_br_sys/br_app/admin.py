from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html
from .models import (
    UserProfile, 
    EquipmentCategory, 
    ChemicalCategory, 
    Equipment, 
    Chemical,
    BorrowEquipment, 
    ChemicalWithdrawal
)

# Extend User Admin
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'get_role', 'is_active', 'last_login')
    list_filter = ('is_active', 'profile__role')
    
    def get_role(self, obj):
        return obj.profile.role if hasattr(obj, 'profile') else '-'
    get_role.short_description = 'Role'

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(EquipmentCategory)
class EquipmentCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(ChemicalCategory)
class ChemicalCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'category', 'quantity_available', 'unit', 'status', 'display_image')
    list_filter = ('type', 'status', 'category')
    search_fields = ('name',)
    ordering = ('name',)

    def display_image(self, obj):
        if obj.image_url:
            return format_html('<img src="{}" width="50" height="50" />', obj.image_url)
        return "No image"
    display_image.short_description = 'Image'

@admin.register(Chemical)
class ChemicalAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity_available', 'unit', 'category', 'status')
    list_filter = ('status', 'category')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(BorrowEquipment)
class BorrowEquipmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'equipment', 'borrow_date', 'return_date', 'actual_return_date', 'status', 'fine')
    list_filter = ('status', 'borrow_date', 'return_date')
    search_fields = ('user__username', 'equipment__name')
    ordering = ('-borrow_date',)
    date_hierarchy = 'borrow_date'

@admin.register(ChemicalWithdrawal)
class ChemicalWithdrawalAdmin(admin.ModelAdmin):
    list_display = ('user', 'chemical', 'withdrawal_date', 'quantity_withdrawn', 'remaining_quantity', 'status')
    list_filter = ('status', 'withdrawal_date')
    search_fields = ('user__username', 'chemical__name')
    ordering = ('-withdrawal_date',)
    date_hierarchy = 'withdrawal_date'