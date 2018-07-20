from regions.models import CountyModel, ConstituencyModel, WardModel
from regions.serializers import CountySerializer, ConstituencySerializer, WardSerializer
from rest_framework.serializers import ValidationError
from rest_framework import generics

class CountyListView(generics.ListCreateAPIView):
    queryset = CountyModel.objects.all()
    serializer_class = CountySerializer

class CountyMemberView(generics.RetrieveDestroyAPIView):
    queryset = CountyModel.objects.all()
    serializer_class = CountySerializer
     # This is the name of the county
    lookup_field = ('name')

class ConstituencyListView(generics.ListCreateAPIView):
    queryset = ConstituencyModel.objects.all()
    serializer_class = ConstituencySerializer

    def perform_create(self, serializer):
        c = CountyModel.objects.get(name=self.request.data['county'])
        try:
            serializer.save(county=c, name=self.request.data['name'])
        except:
            raise ValidationError('unique "name" constraint failed violated.')

class ConstituencyMemberView(generics.RetrieveDestroyAPIView):
    queryset = ConstituencyModel.objects.all()
    serializer_class = ConstituencySerializer
    # This is the name of the constituency
    lookup_field = ('name') 

class WardListView(generics.ListCreateAPIView):
    queryset = WardModel.objects.all()
    serializer_class = WardSerializer

    def perform_create(self, serializer):
        c = ConstituencyModel.objects.get(name=self.request.data['constituency'])
        try:
            serializer.save(constituency=c, name=self.request.data['name'])
        except:
            raise ValidationError('unique "name" constraint failed violated.')

class WardMemberView(generics.RetrieveDestroyAPIView):
    queryset = WardModel.objects.all()
    serializer_class = WardSerializer
    # This is the name of the ward
    lookup_field = ('name')

    