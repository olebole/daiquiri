from __future__ import unicode_literals

import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Job(models.Model):

    PHASE_PENDING = 'PENDING'
    PHASE_QUEUED = 'QUEUED'
    PHASE_EXECUTING = 'EXECUTING'
    PHASE_COMPLETED = 'COMPLETED'
    PHASE_ERROR = 'ERROR'
    PHASE_ABORTED = 'ABORTED'
    PHASE_UNKNOWN = 'UNKNOWN'
    PHASE_HELD = 'HELD'
    PHASE_SUSPENDED = 'SUSPENDED'
    PHASE_ARCHIVED = 'ARCHIVED'
    PHASE_RUN = 'RUN'
    PHASE_ABORT = 'ABORT'
    PHASE_ACTIVE = (
        PHASE_PENDING,
        PHASE_QUEUED,
        PHASE_EXECUTING
    )
    PHASE_CHOICES = (
        (PHASE_PENDING, _('Pending')),
        (PHASE_QUEUED, _('Queued')),
        (PHASE_EXECUTING, _('Executing')),
        (PHASE_COMPLETED, _('Completed')),
        (PHASE_ERROR, _('Error')),
        (PHASE_ABORTED, _('Aborted')),
        (PHASE_UNKNOWN, _('Unknown')),
        (PHASE_HELD, _('Held')),
        (PHASE_SUSPENDED, _('Suspended')),
        (PHASE_ARCHIVED, _('Archived'))
    )

    JOB_TYPE_QUERY = 'QUERY'
    JOB_TYPE_CUTOUT = 'CUTOUT'
    JOB_TYPE_CHOICES = (
        (JOB_TYPE_QUERY, _('Query')),
        (JOB_TYPE_CUTOUT, _('Cutout')),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    owner = models.ForeignKey(User, blank=True, null=True)

    run_id = models.CharField(max_length=256, blank=True)

    phase = models.CharField(max_length=10, choices=PHASE_CHOICES)

    creation_time = models.DateTimeField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    execution_duration = models.PositiveIntegerField(blank=True, default=0)
    destruction_time = models.DateTimeField(blank=True, null=True)

    error_summary = models.CharField(max_length=256, blank=True, null=True)

    job_type = models.CharField(max_length=10, choices=JOB_TYPE_CHOICES)

    class Meta:
        ordering = ('start_time', )

        verbose_name = _('Job')
        verbose_name_plural = _('Jobs')

        permissions = (('view_job', 'Can view Job'),)

    def __str__(self):
        return self.get_str()

    def get_str(self):
        return "id=%s; phase=%s; job_type=%s" % (str(self.id), self.phase, self.job_type)

    @property
    def owner_username(self):
        return self.owner.username if self.owner else 'anonymous'

    @property
    def parameters(self):
        raise NotImplementedError

    @property
    def results(self):
        raise NotImplementedError

    @property
    def error(self):
        raise NotImplementedError

    @property
    def quote(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError

    def abort(self):
        raise NotImplementedError

    def archive(self):
        raise NotImplementedError

    # def run(self):
    #     if self.phase == PHASE_PENDING:
    #         self.phase = PHASE_QUEUED
    #         self.save()
    #     else:
    #         raise UWSException('Job is not in PENDING phase')

    # def abort(self):
    #     if self.phase in PHASE_ACTIVE:
    #         self.phase = PHASE_ABORTED
    #         self.save()
    #     else:
    #         raise UWSException('Job is not in PENDING, QUEUED or EXECUTING phase')

    # def archive(self):
    #     if hasattr(self, 'queryjob'):
    #         self.queryjob.drop_table()

    #     if self.phase != PHASE_ARCHIVED:
    #         self.phase = PHASE_ARCHIVED
    #         self.save()
    #     else:
    #         raise UWSException('Job is already in ARCHIVED phase')
