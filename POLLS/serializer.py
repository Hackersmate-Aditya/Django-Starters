from django.db import models
import datetime

from rest_framework import serializers
from .models import Choice, Question


#serializer for choice

class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = '__all__'                                       #selecting all fields









#serializer for question

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'


       def validate(self, attrs):
        errors = list()

        if attrs['pub_date'] > datetime.datetime.now(attrs['pub_date'].tzinfo):                       #comparing our pub_date with current one and if pub_date>current,, it will throw an error
            errors.append('pub_date cannot be in future')

        if attrs['question_text'].find('?')== -1:                                              #if question_text doesnt have '?', error will be appended
            errors.append('question_text must contain question mark....')

        if attrs.__len__() > 0:
            raise serializers.ValidationError(' _###_ '.join(x for x in errors))                       

        return attrs
