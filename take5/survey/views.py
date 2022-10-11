from rest_framework.decorators import api_view
from rest_framework.response import Response
from survey.models import Survey
from survey.serializers import SurveySerializer
from survey.test_utils import calculate_db_queries

# Create your views here.


@api_view(['GET'])
def surveys(request) -> Response:
    """
    Rota para recurso Survey
    """

    if request.method == 'GET':
        if request.GET.get('id', False):
            try:
                query = Survey.objects.filter(
                    pk=request.query_params['id']).prefetch_related('questions')
                serializer = SurveySerializer(query, many=True)
                calculate_db_queries()
                return Response(serializer.data, 200)
            except Survey.DoesNotExist:
                return Response({'error': 'Survey not found'}, 404)
        else:
            query = Survey.objects.all().prefetch_related(
                'questions')
            serializer = SurveySerializer(query, many=True)
            calculate_db_queries()
            return Response(serializer.data, 200)
