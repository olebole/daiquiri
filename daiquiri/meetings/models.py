from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from jsonfield import JSONField


@python_2_unicode_compatible
class Meeting(models.Model):

    title = models.CharField(
        max_length=256,
        verbose_name=_('Title'),
        help_text=_('Title of the meeting')
    )
    slug = models.SlugField(
        max_length=256,
        verbose_name=_('Slug'),
        help_text=_('Slug for the URL of the meeting')
    )
    registration_message = models.TextField(
        blank=True, null=True,
        verbose_name=_('Registration message'),
        help_text=_('Message on registration page')
    )
    participants_message = models.TextField(
        blank=True, null=True,
        verbose_name=_('Participants message'),
        help_text=_('Message on participants page')
    )
    contributions_message = models.TextField(
        blank=True, null=True,
        verbose_name=_('Contributions message'),
        help_text=_('Message on contributions page')
    )
    registration_open = models.BooleanField(
        default=False,
        verbose_name=_('Registration open'),
        help_text=_('Designates whether the registration page is publicly accessible.')
    )
    participants_open = models.BooleanField(
        default=False,
        verbose_name=_('Participants list open'),
        help_text=_('Designates whether the participants page is publicly accessible.')
    )
    contributions_open = models.BooleanField(
        default=False,
        verbose_name=_('Contributions list open'),
        help_text=_('Designates whether the contributions page is publicly accessible.')
    )

    class Meta:
        ordering = ('title', )

        verbose_name = _('Meeting')
        verbose_name_plural = _('Meetings')

        permissions = (('view_meeting', 'Can view Meeting'),)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Participant(models.Model):

    meeting = models.ForeignKey(
        Meeting, related_name='participants',
        verbose_name=_('Meeting'),
        help_text=_('Meeting this participant has registered for')
    )
    first_name = models.CharField(
        max_length=256,
        verbose_name=_('First name'),
    )
    last_name = models.CharField(
        max_length=256,
        verbose_name=_('Last name'),
    )
    email = models.EmailField(
        max_length=256,
        verbose_name=_('Email'),
    )
    details = JSONField(
        null=True, blank=True,
        verbose_name=_('Details'),
        help_text=_('Choices are given by settings.MEETINGS_PARTICIPANT_DETAIL_KEYS')
    )
    registered_on = models.DateTimeField(
        verbose_name=_('Registered on'),
        help_text=_('Datetime this participant has submitted his/her registration')
    )
    accepted = models.BooleanField(
        default=False,
        verbose_name=_('Accepted'),
        help_text=_('Designates whether the participant is accepted.')
    )

    class Meta:
        ordering = ('meeting', 'last_name', 'first_name')

        verbose_name = _('Participant')
        verbose_name_plural = _('Participants')

        permissions = (('view_participant', 'Can view Participant'),)

    def __str__(self):
        return '%s (%s)' % (self.full_name, self.meeting)

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)


@python_2_unicode_compatible
class Contribution(models.Model):

    participant = models.ForeignKey(
        Participant, related_name='contributions',
        verbose_name=_('Participant'),
        help_text=_('Participant who submitted this contribution')
    )
    title = models.CharField(
        max_length=256,
        verbose_name=_('Title')
    )
    abstract = models.TextField(
        blank=True, null=True,
        verbose_name=_('Abstract')
    )
    contribution_type = models.CharField(
        max_length=8,
        verbose_name=_('Contribution type'),
        help_text=_('Choices are given by settings.MEETINGS_CONTRIBUTION_TYPES')
    )
    accepted = models.BooleanField(
        default=False,
        verbose_name=_('Accepted'),
        help_text=_('Designates whether the contribution is accepted.')
    )

    class Meta:
        ordering = ('participant', 'title')

        verbose_name = _('Contribution')
        verbose_name_plural = _('Contributions')

        permissions = (('view_contribution', 'Can view Contribution'),)

    def __str__(self):
        return '%s: %s' % (self.participant.full_name, self.title)
