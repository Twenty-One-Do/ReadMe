from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class PortfolioListView(APIView):

    def get(self, request):
        pass

    def post(self, request):
        pass

class PortfolioDetailView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        pass

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass
