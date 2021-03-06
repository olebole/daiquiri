import logging
import os

from sendfile import sendfile

from django.conf import settings
from django.utils.timezone import now
from django.shortcuts import render
from django.utils.safestring import mark_safe

from daiquiri.core.utils import get_client_ip
from daiquiri.stats.models import Record

from .models import Directory

logger = logging.getLogger(__name__)


def file_exists(file_path):
    absolute_file_path = os.path.join(settings.FILES_BASE_PATH, file_path)
    return os.path.isfile(absolute_file_path)


def get_directory(user, file_path):
    # loop over all directories beginning with the hights depth and return as soon as a directory matches
    for directory in Directory.objects.order_by('-depth'):
        if os.path.normpath(file_path).startswith(directory.path):
            try:
                return Directory.objects.filter_by_access_level(user).get(pk=directory.pk)
            except Directory.DoesNotExist:
                return None


def check_file(user, file_path):
    return get_directory(user, file_path) is not None


def render_with_layout(request, file_path):
    absolute_file_path = os.path.join(settings.FILES_BASE_PATH, file_path)

    context = {}

    with open(absolute_file_path) as f:
        context['content'] = mark_safe(f.read())

    return render(request, 'files/layout.html', context)


def send_file(request, file_path, search=None):
    # create a stats record for this download
    resource = {
        'file_path': file_path
    }
    if search:
        resource['search'] = search

    Record.objects.create(
        time=now(),
        resource_type='FILE',
        resource=resource,
        client_ip=get_client_ip(request),
        user=request.user if request.user.is_authenticated else None
    )

    # send the file to the client
    absolute_file_path = os.path.join(settings.FILES_BASE_PATH, file_path)
    return sendfile(request, absolute_file_path)
