from rest_framework import generics,mixinsfrom django.shortcuts import get_object_or_404from pizza.models import  Pizzafrom .serializers import PizzaSerializerfrom rest_framework.views import APIViewfrom rest_framework.response import Responseclass StatusListSearchAPIView(APIView):    permission_classes = []    authentication_classes =  []    def get(self,request,format=None):        qs = Pizza.objects.all()        serializer = PizzaSerializer(qs,many=True)        return Response(serializer.data)    def post(self,request,format=None):        qs = Pizza.objects.all()        serializer = PizzaSerializer(qs,many=True)        return Response(serializer.data)class StatusAPIView(mixins.CreateModelMixin,generics.ListAPIView): # create ,list    permission_classes = []    authentication_classes = []    queryset =  Pizza.objects.all()    serializer_class = PizzaSerializer    def get_queryset(self):        qs = Pizza.objects.all()        query = self.request.GET.get('q')        if query is not None:            qs = qs.filter(content__icontains=query)        return qs    def post(self,request,*args,**kwargs):        return self.create(request,*args,**kwargs)class PizzaCreateAPIView(generics.CreateAPIView):    permission_classes = []    authentication_classes = []    queryset = Pizza.objects.all()    serializer_class = PizzaSerializerclass PizzaDetailAPIView(mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.RetrieveAPIView):    permission_classes = []    authentication_classes = []    queryset = Pizza.objects.all()    serializer_class = PizzaSerializer    def put(self,request,*args,**kwargs):        return self.update(request,*args,**kwargs)    def delete(self, request, *args, **kwargs):        return self.destroy(request,*args,**kwargs)class PizzaUpdateAPIView(generics.UpdateAPIView):    permission_classes          = []    authentication_classes      = []    queryset                    = Pizza.objects.all()    serializer_class            = PizzaSerializerclass PizzaDeleteAPIView(generics.DestroyAPIView):    permission_classes          = []    authentication_classes      = []    queryset                    = Pizza.objects.all()    serializer_class            = PizzaSerializer