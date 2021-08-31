from django.db import models
import datetime

from rest_framework import serializers
from .models import Choice, Question


#serializer for choice

class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = '__all__'









#serializer for question

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'


    '''def validate(self, attrs):
        errors = list()

        if attrs['pub_date'] > datetime.datetime.now(attrs['pub_date'].tzinfo):
            errors.append('pub_date cannot be in future')

        if attrs['question_text'].find('?')== -1:
            errors.append('question_text must contain question mark....')

        if attrs.__len__() > 0:
            raise serializers.ValidationError(' _###_ '.join(x for x in errors))

        return attrs'''