from django.contrib import admin
from django.utils.safestring import mark_safe


from myowngame.models import CategoryModel, ContactModel, CustomUser, QuestionModel


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'count', 'count_game', 'image_show')

    def image_show(self, obj):
        '''Вывод картинки в админке'''
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return None


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'create_date')
    ordering = ('-create_date',)


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(QuestionModel)
class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ('question', 'score', 'category', 'image_show')

    def image_show(self, obj):
        '''Вывод картинки в админке'''
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return None


