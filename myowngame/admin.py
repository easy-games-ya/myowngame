from django.contrib import admin
from django.utils.safestring import mark_safe


from myowngame.models import CategoryModel, ContactModel, CustomUser, QuestionModel


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'avatar', 'username', 'gender', 'count', 'count_game')

    # def image_show(self, obj):
    # #     '''Вывод картинки в админке'''
    # #     if obj.image:
    # #         return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
    #     return None


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'create_date')
    ordering = ('-create_date',)


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','slug', 'description')


@admin.register(QuestionModel)
class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'score', 'category', 'image_show')

    def image_show(self, obj):
        '''Вывод картинки в админке'''
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return None


