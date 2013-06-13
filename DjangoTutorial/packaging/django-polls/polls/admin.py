# -*- coding: UTF-8 -*-
__author__ = 'ielkin'

from django.contrib import admin
from polls.models import Poll, Choice


# Separate page for choice and poll
# class PollAdmin(admin.ModelAdmin):
#     # Admin customization
#     #fields = ['pub_date', 'question']
#     fieldsets = [
#                 (None, {'fields': ['question']}),
#                 ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#                 ]
#
# admin.site.register(Poll, PollAdmin)
# admin.site.register(Choice)

# Single page for Poll with choices
# Stacked choices
#class ChoiceInline(admin.StackedInline):
# Tabled choices
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'

admin.site.register(Poll, PollAdmin)