from rest_framework import serializers

from daiquiri.jobs.models import Job

from .utils import make_query_dict_upper_case


class JobListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ('id', 'phase')


class JobRetrieveSerializer(serializers.ModelSerializer):

    job_id = serializers.UUIDField(source='id')
    owner_id = serializers.UUIDField(source='owner.username')
    destruction = serializers.DateTimeField(source='destruction_time')

    class Meta:
        model = Job
        fields = (
            'job_id',
            'owner_id',
            'phase',
            'quote',
            'start_time',
            'end_time',
            'execution_duration',
            'destruction',
            'results',
            'parameters'
        )


class CaseInsensitiveSerializer(serializers.Serializer):

    def __init__(self, **kwargs):
        # make all the keys in kwargs['data'] upper case
        kwargs['data'] = make_query_dict_upper_case(kwargs.get('data'))

        super(CaseInsensitiveSerializer, self).__init__(**kwargs)


class JobUpdateSerializer(CaseInsensitiveSerializer):

    PHASE = serializers.CharField(required=False)


class SyncJobSerializer(CaseInsensitiveSerializer):

    RESPONSEFORMAT = serializers.CharField(required=False)
    MAXREC = serializers.IntegerField(required=False)
    RUNID = serializers.CharField(required=False)


class AsyncJobSerializer(CaseInsensitiveSerializer):

    PHASE = serializers.CharField(required=False)
    RESPONSEFORMAT = serializers.CharField(required=False)
    MAXREC = serializers.IntegerField(required=False)
    RUNID = serializers.CharField(required=False)