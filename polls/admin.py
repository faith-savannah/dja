from django.contrib import admin

# Register your models here.
from .models import Question, Choice

#let the Choice objects be edited on the Question admin page...
#...instead of one of its own admin page.
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3 #provide 3-choices-fields by default

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
	(None,   				{'fields':['question_text']}),
	('Date information',	{'fields':['pub_date'], 'classes': ['collapse']}),
	]

	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'was_published_recently') #set the field names to display in change list page
	list_filter = ['pub_date']
	search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
