from django.contrib import admin

from myowngame.models import CategoryModel, ContactModel, CustomUser, QuestionModel


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'count', 'count_game')


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'create_date')
    ordering = ('-create_date',)


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(QuestionModel)
class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ('question', 'score', 'category')


