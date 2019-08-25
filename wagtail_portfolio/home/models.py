from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Orderable, Page
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    introduction = RichTextField(blank=True)
    interests = RichTextField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, null=True, related_name='+'
    )
    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
        ImageChooserPanel('image'),
        InlinePanel('work_experience', label='Work Experience'),
        InlinePanel('education', label='Education'),
        InlinePanel('awards', label='Awards'),
        InlinePanel('project', label='Project'),
        InlinePanel('languages_and_tools', label='Languages and Tools'),
        FieldPanel('interests', classname='full')
    ]


class WorkExperience(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='work_experience', default=1)
    job_title = models.CharField(max_length=255, blank=True)
    company_title = models.CharField(max_length=255, blank=True)
    job_description = RichTextField(blank=True)
    job_date = models.CharField(max_length=255, blank=True)

    panels = [
        FieldPanel('job_title', classname="full"),
        FieldPanel('company_title', classname='full'),
        FieldPanel('job_description', classname='full'),
        FieldPanel('job_date', classname='full')
    ]


class Education(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='education', default=1)
    education_provider = models.CharField(max_length=255, blank=True)
    course_level = models.CharField(max_length=255, blank=True)
    course_description = RichTextField(blank=True)
    course_date = models.CharField(max_length=255, blank=True)
    course_results = models.CharField(max_length=255, blank=True)

    panels = [
        FieldPanel('education_provider', classname="full"),
        FieldPanel('course_description', classname="full"),
        FieldPanel('course_level', classname='full'),
        FieldPanel('course_date', classname='full'),
        FieldPanel('course_results', classname='full'),
    ]


class Awards(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='awards', default=1)
    award_name = models.CharField(max_length=255, blank=True)
    awarded_by = RichTextField(blank=True)
    award_date = models.CharField(max_length=255, blank=True)

    panels = [
        FieldPanel('award_name', classname="full"),
        FieldPanel('awarded_by', classname="full"),
        FieldPanel('award_date', classname='full'),
    ]


class LanguagesAndTools(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='languages_and_tools', default=1)
    language = models.CharField(max_length=255, blank=True)
    tools = RichTextField(blank=True)

    panels = [
        FieldPanel('language', classname="full"),
        FieldPanel('tools', classname="full"),
    ]


class ProjectMember(models.Model):
    project = ParentalKey('Project', related_name='project_members', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    languages_and_frameworks = models.CharField(max_length=255, blank=True)
    description = RichTextField(blank=True)
    url = models.CharField(max_length=255, blank=True)

    panels = [
        FieldPanel('title', classname='full'),
        FieldPanel('languages_and_frameworks', classname='full'),
        FieldPanel('description', classname='full'),
        FieldPanel('url', classname='full'),
    ]


class Project(ClusterableModel, Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='project', default=1)
    project_group_title = models.CharField(max_length=255, blank=True, default=" ")
    project_member = ParentalManyToManyField(ProjectMember, related_name='project_member', blank=True)
    panels = [
        FieldPanel('project_group_title', classname='full'),
        InlinePanel('project_members', label='Project Member'),
    ]