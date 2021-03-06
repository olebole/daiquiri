from django.urls import include, path

from rest_framework import routers

from .views import QueryView, JobsView, ExamplesView
from .viewsets import (
    StatusViewSet,
    FormViewSet,
    DropdownViewSet,
    QueryJobViewSet,
    ExampleViewSet,
    QueueViewSet,
    QueryLanguageViewSet,
    PhaseViewSet
)


app_name = 'query'

router = routers.DefaultRouter()
router.register(r'status', StatusViewSet, base_name='status')
router.register(r'forms', FormViewSet, base_name='form')
router.register(r'dropdowns', DropdownViewSet, base_name='dropdown')
router.register(r'jobs', QueryJobViewSet, base_name='job')
router.register(r'examples', ExampleViewSet, base_name='example')
router.register(r'queues', QueueViewSet, base_name='queue')
router.register(r'querylanguages', QueryLanguageViewSet, base_name='querylanguage')
router.register(r'phases', PhaseViewSet, base_name='phase')

urlpatterns = [
    path(r'', QueryView.as_view(), name='query'),
    path(r'jobs/', JobsView.as_view(), name='jobs'),
    path(r'examples/', ExamplesView.as_view(), name='examples'),

    # rest api
    path(r'api/', include(router.urls)),
]
