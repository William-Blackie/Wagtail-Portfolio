from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register

from blog.models import BlogPageType, BlogPageSubType


class BlogPageTypeModelAdmin(ModelAdmin):
    model = BlogPageType
    menu_icon = 'tag'
    inlines = [BlogPageType]


class BlogPageSubTypeModelAdmin(ModelAdmin):
    model = BlogPageSubType
    menu_icon = 'tag'


class TaxonomiesModelAdminGroup(ModelAdminGroup):
    menu_label = 'Taxonomies'
    list_filter = ('title', )
    search_fields = ('title', )
    items = (BlogPageTypeModelAdmin, BlogPageSubTypeModelAdmin)


modeladmin_register(TaxonomiesModelAdminGroup)