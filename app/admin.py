from django.contrib import admin
from .models import Category,Question,Answer


# StackInline is class which is used show the foriegn key data in one line only
class AnswerAdmin(admin.StackedInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]    

# Register your models here.
admin.site.register(Category)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer)    