from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock


class BlogPageType(models.Model):
    class Meta:
        ordering = ['title']

    title = models.CharField(max_length=125)
    plural_title = models.CharField(max_length=125)
    description = models.CharField(max_length=150)
    blog_sub_type = models.ForeignKey('BlogPageSubType',
                                  on_delete=models.SET_NULL,
                                  blank=True,
                                  null=True,
                                  related_name='+'
                                  )

    filter_by = models.ForeignKey('BlogPageType',
                                  on_delete=models.SET_NULL,
                                  blank=True,
                                  null=True,
                                  related_name='+'
                                )

    panels = [
        FieldPanel('title'),
        FieldPanel('plural_title'),
        FieldPanel('description'),
        FieldPanel('blog_sub_type')
    ]

    def __str__(self):
        return self.title


class BlogPageSubType(models.Model):
    class Meta:
        ordering = ['title']

    title = models.CharField(max_length=125)
    plural_title = models.CharField(max_length=125150)
    description = models.CharField(max_length=150)
    filter_by = models.ForeignKey('BlogPageSubType',
                                  on_delete=models.SET_NULL,
                                  blank=True,
                                  null=True,
                                  related_name='+'
                                  )

    panels = [
        FieldPanel('title'),
        FieldPanel('plural_title'),
        FieldPanel('description'),
        FieldPanel('filter_by')
    ]
    def __str__(self):
        return self.title


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

    page_type = models.ForeignKey('BlogPageSubType',
                                      on_delete=models.SET_NULL,
                                      blank=True,
                                      null=True,
                                      related_name='+'
                                      )

    page_sub_type = models.ForeignKey('BlogPageType',
                                  on_delete=models.SET_NULL,
                                  blank=True,
                                  null=True,
                                  related_name='+'
                                  )

    content_panels = Page.content_panels + [
        FieldPanel('description', classname='full'),
        StreamFieldPanel('body', classname="full"),
        FieldPanel('created_date'),
        FieldPanel('revision_date'),
        FieldPanel('page_type'),
        FieldPanel('page_sub_type'),
    ]