from .models import Member, Detail, Activity
from .serializer import memberSerializer, detailSerializer,activitySerializer
from rest_framework import generics
from rest_framework import mixins


class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = memberSerializer
    queryset = Member.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)



class detailGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = detailSerializer
    queryset = Detail.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class activityGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = activitySerializer
    queryset = Activity.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)












'''
# class memberViewSet(viewsets.ViewSet):
# 
#     def list(self, request):
#         member = Member.objects.all()
#         serializer = memberSerializer(member, many=True)
#         return Response(serializer.data)
# 
#     def create(self, request):
#         serializer = memberSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 
#     def retrieve(self, request, pk=None):
#         queryset = Member.objects.all()
#         member = get_object_or_404(queryset, pk=pk)
#         serializer = memberSerializer(member)
#         return Response(serializer.data)


'''

'''

# class detailViewSet(viewsets.ViewSet):
# 
#     def list(self, request):
#         detail = Detail.objects.all()
#         serializer = detailSerializer(detail, many=True)
#         return Response(serializer.data)
# 
#     def create(self, request):
#         serializer = detailSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 
#     def retrieve(self, request, pk=None):
#         queryset = Detail.objects.all()
#         detail = get_object_or_404(queryset, pk=pk)
#         serializer = detailSerializer(detail)
#         return Response(serializer.data)
# 
# class activityViewSet(viewsets.ViewSet):
# 
#     def list(self, request):
#         activity = Activity.objects.all()
#         serializer = activitySerializer(activity, many=True)
#         return Response(serializer.data)
# 
#     def create(self, request):
#         serializer = activitySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 
#     def retrieve(self, request, pk=None):
#         queryset = Detail.objects.all()
#         activity = get_object_or_404(queryset, pk=pk)
#         serializer = activitySerializer(activity)
#         return Response(serializer.data)
'''