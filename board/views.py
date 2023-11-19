from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from board.models import Board
from board.serializers import BoardSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class BoardAPIView(viewsets.ModelViewSet):
    queryset = Board.objects.all().order_by('created')
    serializer_class = BoardSerializer

    @swagger_auto_schema(
        tags=['board'],
        operation_summary='게시글 리스트',
        responses={
            200: openapi.Response('게시글 리스트 응답 예시', BoardSerializer),
            401: 'Authenticaion Failed',
            403: 'Permission denied(403)',
            404: 'Not Found(404)'
        }
    )
    @method_decorator(cache_page(60*60*24*7))
    def list(self, request, *args, **kwargs):
        queryset = cache.get('boards')
        if not queryset:
            queryset = self.get_queryset()
            cache.set('foods', queryset, 60*60*24*7)
        serializer = BoardSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        tags=['board'],
        operation_summary='게시글 생성',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='이름(최대 100자)'),
                'content': openapi.Schema(type=openapi.TYPE_STRING, description='내용')

            }
        ),
        responses={
            201: openapi.Response('게시글 생성 예시', BoardSerializer),
            401: 'Authenticaion Failed',
            403: 'Permission denied(403)',
            404: 'Not Found(404)'
        }
    )
    def create(self, request):
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            result = serializer.save()
            return Response(BoardSerializer(result).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        tags=['board'],
        operation_summary='게시글 수정',
        manual_parameters=[
            openapi.Parameter('id', in_=openapi.IN_QUERY, description='게시글 고유 아이디', type=openapi.TYPE_STRING)],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='이름(최대 100자)'),
                'content': openapi.Schema(type=openapi.TYPE_STRING, description='내용')

            }
        ),
        responses={
            200: openapi.Response('게시글 수정', BoardSerializer),
            401: 'Authenticaion Failed',
            403: 'Permission denied(403)',
            404: 'Not Found(404)'
        }
    )
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['board'],
        operation_summary='게시글 수정',
        manual_parameters=[
            openapi.Parameter('id', in_=openapi.IN_QUERY, description='게시글 고유 아이디', type=openapi.TYPE_STRING)],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='이름(최대 100자)'),
                'content': openapi.Schema(type=openapi.TYPE_STRING, description='내용')

            }
        ),
        responses={
            200: openapi.Response('게시글 수정', BoardSerializer),
            401: 'Authenticaion Failed',
            403: 'Permission denied(403)',
            404: 'Not Found(404)'
        }
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


    @swagger_auto_schema(
        tags=['board'],
        operation_summary='게시글 상세 조회',
        manual_parameters=[openapi.Parameter('id', in_=openapi.IN_QUERY, description='게시글 고유 아이디', type=openapi.TYPE_STRING)],
        responses={
            200: openapi.Response('게시글 응답 예시', BoardSerializer),
            401: 'Authenticaion Failed',
            403: 'Permission denied(403)',
            404: 'Not Found(404)'
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(self, request, *args, **kwargs)

    @swagger_auto_schema(
        tags=['board'],
        operation_summary='게시글 삭제',
        manual_parameters=[openapi.Parameter('id', in_=openapi.IN_QUERY, description='게시글 고유 아이디', type=openapi.TYPE_STRING)],
        responses={
            204: 'No Content',
            401: 'Authenticaion Failed',
            403: 'Permission denied(403)',
            404: 'Not Found(404)'
        }
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(self, request, *args, **kwargs)
