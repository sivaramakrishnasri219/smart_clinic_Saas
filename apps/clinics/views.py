from django.shortcuts import render
class PatientViewSet(ClinicQuerysetMixin, ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]
