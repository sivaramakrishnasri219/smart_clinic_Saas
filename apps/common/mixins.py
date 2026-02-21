class ClinicQuerysetMixin:

    def get_clinic(self):
        return self.request.user.doctorprofile.clinic

    def get_queryset(self):
        return super().get_queryset().filter(
            clinic=self.get_clinic()
        )

    def perform_create(self, serializer):
        serializer.save(clinic=self.get_clinic())
