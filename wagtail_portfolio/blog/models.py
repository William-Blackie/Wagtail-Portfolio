from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock


class BlogIndexPage(Page):
    description = models.CharField(max_length=255, blank=True,)
    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full")
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # Set page variables
        context['blog_posts'] = BlogPage.objects.live().public()
        print(context['blog_posts'])


class BlogPage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])
    description = RichTextField(blank=True)
    created_date = models.DateField("Post date", null=True)
    revision_date = models.DateField("Revision date", null=True)

    content_panels = Page.content_panels + [
        FieldPanel('description', classname='full'),
        StreamFieldPanel('body', classname="full"),
        FieldPanel('created_date'),
        FieldPanel('revision_date'),
    ]