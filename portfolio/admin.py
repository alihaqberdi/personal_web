from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import *
from django.contrib.sessions.models import Session


admin.site.unregister([User, Group])
admin.site.register([Network, Index, BaseNetwork, Category, Tag, About, Session, PostView, Contact])


class AdminPortfolioMedia(admin.TabularInline):
    model = PortfolioMedia

@admin.register(Portfolio)
class AdminPortfolio(admin.ModelAdmin):
    list_display = ['name','id', 'view']
    list_filter = ['view']
    list_editable = ['view']
    inlines = [AdminPortfolioMedia]

@admin.register(Contact_Message)
class AdminContact(admin.ModelAdmin):
    list_display = ['name', 'option', 'created']

@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ['user', 'created', 'post']
    list_filter = ['user']



@admin.register(Base)
class AdminBase(admin.ModelAdmin):
    list_display = ['id','title', 'copyright']


admin.site.register(PortfolioMedia)