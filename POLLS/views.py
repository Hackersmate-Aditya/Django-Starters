from .serializer import QuestionSerializer, ChoiceSerializer
from .models import Question, Choice                                     #importing libraries
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pdb import set_trace as b


from polls.models import Choice


class ChoiceView(APIView):                                                 

    def get(self, request):
        choices = Choice.objects.all()                                                #ORM method to get all objects
        serializer = ChoiceSerializer(choices, many=True)
        return Response({"choices":  serializer.data}, status=status.HTTP_200_OK)         #returning output

    def post(self, request):
        #b()                                                                               #debugger(breakpoint)
        serializer = ChoiceSerializer(data=request.data)
        if serializer.is_valid():                                                          #checking condition
            serializer.save()                                                              #saving 
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response({"questions": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        #b()
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionByPK(APIView):                                           #PK defines primary key
    def get(self, request, id):
        #b()
        questions = Question.objects.get(id=id)                       #fetching data from record
        serializer = QuestionSerializer(questions)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        #b()
        snippet = Question.objects.filter(id=id).first()
        if snippet is None:
            return Response(status=status.HTTP_204_NO_CONTENT)
        if 'pub_date' not in request.data.keys():                         #if pub_date is not given,will requesting to take from database
            request.data['pub_date'] = snippet.pub_date
        serializer = QuestionSerializer(snippet, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        snippet = Question.objects.filter(id=id)
        if snippet.count() == 0:                                           #if there is no data
            return Response(status=status.HTTP_204_NO_CONTENT)
        snippet.delete()
        return Response([], status=status.HTTP_200_OK)


class ChoiceByFK(APIView):                                                   #FK means foreign key

    def get(self, request, id):
        choices = Choice.objects.get(id = id)
        serializer = ChoiceSerializer(choices)
        return Response({"choices":  serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, id):
        fire = Choice.objects.filter(id=id).first()
        if fire is None:                                                                #if its empty
            return Response(status=status.HTTP_204_NO_CONTENT)
        if 'choice_text' not in request.data.keys():
            request.data['choice_text'] = fire.choice_text                             #fetching
        serializer = ChoiceSerializer(fire, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        sack = Question.objects.filter(id=id)
        if sack.count() == 0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        sack.delete()                                                      #deleting it from table 
        return Response([], status=status.HTTP_200_OK)

class votes(APIView):
    def put(self, request, id):
        admin_vote = Choice.objects.filter(id=id).first()
        if admin_vote is None:
            return Response(status=status.HTTP_204_NO_CONTENT)
        if 'votes' not in request.data.keys():
            request.data['votes'] = admin_vote.votes+1                            #fetching the data of "votes" and incrementing it
        request.data['choice_text'] = admin_vote.choice_text
        request.data['question'] = admin_vote.question_id
        serializer = ChoiceSerializer(admin_vote, data=request.data)             #serializer requesting data from db
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)                  #returning outputs according to the given conditions
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
