from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import PostImageSerializer


class PostImageUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = PostImageSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # post_id = request.data.get('post')
        # images = request.data.get('images')
        # for _, img in images:
        #     data = {
        #         'post': post_id,
        #         'image': img
        #     }
        #     file_serializer = PostImageSerializer(data=data)
        #
        #     if file_serializer.is_valid():
        #         file_serializer.save()
        #     else:
        #         return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return Response({'msg': '图片上传成功！'}, status=status.HTTP_201_CREATED)
