from django.shortcuts import render

# Create your views here.


# class ItemListView():
#     permission_classes = [AllowAny]
#     serializer_class = ChartSerializer
#     queryset = ChartTest.objects.all()
#
#     def get_queryset(self):
#         return self.queryset
#
#     def get(self, request, *args, **kwargs):
#         page = self.paginate_queryset(self.get_queryset())
#         serializer = self.get_serializer(page, many=True)
#         return self.get_paginated_response(serializer.data)