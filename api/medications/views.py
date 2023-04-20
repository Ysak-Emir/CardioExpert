from django.db.models import Q
from rest_framework import generics, filters, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.medications.models import Medication
from api.medications.serializers import MedicationSerializer, MedicationDeleteSerializer


class MedicationCreateAPIVIew(generics.CreateAPIView):
    """
    Создание препарата
    """

    serializer_class = MedicationSerializer
    permission_classes = (permissions.IsAuthenticated, )
    def get_queryset(self):
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        queryset = Medication.objects.all()
        if start_date and end_date:
            queryset = queryset.filter(Q(start_date__gte=start_date) & Q(end_date__lte=end_date))
        return queryset


class MedicationListAPIView(generics.ListAPIView):
    """
    Для получения списка лекарств с возможностью поиска.
    """
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('dosege', 'title',)


class DeleteMedicationAPIView(APIView):
    """
    Удаление препарата по ИД
    """
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk):
        try:
            obj = Medication.objects.get(pk=pk)
            obj.delete()
            return Response({'message': 'Object deleted successfully!'})
        except Medication.DoesNotExist:
            return Response({'message': 'Object does not exist!'}, status=status.HTTP_404_NOT_FOUND)


class DeleteMedicationByNameAPIView(APIView):
    """
    Удаление препарата по названию
    """
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = MedicationDeleteSerializer(data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data['title']
            try:
                obj = Medication.objects.get(title=title)
                obj.delete()
                return Response({'success': f'Препарат: "{title}" был удален'})
            except Medication.DoesNotExist:
                return Response({'error': f'Препарат: "{title}" не существует'})
        else:
            return Response(serializer.errors, status=400)


