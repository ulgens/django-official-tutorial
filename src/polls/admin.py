from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [  # noqa: RUF012
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]  # noqa: RUF012
    list_display = ["question_text", "pub_date", "was_published_recently"]  # noqa: RUF012
    list_filter = ["pub_date"]  # noqa: RUF012
    search_fields = ["question_text"]  # noqa: RUF012


admin.site.register(Question, QuestionAdmin)
