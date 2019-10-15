from django.contrib import admin
from .models import Feedback, QuesSubject, SubSeries, Paper, Prank


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ["category_title", "category_summary"]
    ordering = ["category_title"]
    fieldsets = [
        ("Basics", {"fields": ["category_title", "category_summary", "category_slug"]}),
        ("Media", {"fields": ["category_image"]}),
    ]

class EssayInline(admin.StackedInline):
    model = Paper
    extra = 2

class SubSeriesAdmin(admin.ModelAdmin):
    list_filter = ['category_title']
    list_display = ('series_title', 'category_title')
    ordering = ['category_title']
    fieldsets = [
        (None,               {'fields': ['series_title', 'series_summary', 'series_slug']}),
        ('Contents', {'fields': ['series_image', 'category_title'], 'classes': ['collapse']}),
    ]
    inlines = [EssayInline]


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('feedback_title', 'feedback_user_id', 'feedback_date')   # displays the info in row
    list_filter = ['feedback_user_id', 'feedback_date']
    # search_fields = ['essay_title', 'series_title']
    ordering = ['feedback_date']

    fieldsets = [
        ("Title/date", {'fields': ["feedback_title", "feedback_date", "feedback_user_id",]}),
        ("Content", {'fields': ['feedback_content']}),
    ]


admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(QuesSubject, SubCategoryAdmin)
admin.site.register(SubSeries, SubSeriesAdmin)
admin.site.register(Paper)
admin.site.register(Prank)