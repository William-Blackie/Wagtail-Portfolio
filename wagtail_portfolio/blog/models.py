from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page


class BlogIndexPage(Page):
    description = models.CharField(max_length=255, blank=True,)
    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full")
    ]


class BlogPage(Page):
    body = RichTextField(blank=True)
    description = RichTextField(blank=True)
    created_date = models.DateField("Post date", null=True)
    revision_date = models.DateField("Revision date", null=True)
    content_panels = Page.content_panels + [
        FieldPanel('description', classname='full'),
        FieldPanel('body', classname="full"),
        FieldPanel('created_date'),
        FieldPanel('revision_date'),
    ]