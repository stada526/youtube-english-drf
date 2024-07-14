from typing import Any, TypedDict
import uuid
from django.http import HttpRequest
from rest_framework import views, status
from rest_framework.response import Response

from api.repositories.video_repository import VideoRepository
from api.usecases.video_usecase import VideoUsecase


class VideoListItemContract(TypedDict):
    id: str
    youtubeVideoId: str
    title: str
    createdAt: str


class WordContract(TypedDict):
    word: str
    start: float
    end: float


class SegmentContract(TypedDict):
    start: float
    end: float
    text: str
    words: list[WordContract]


class VideoItemContract(TypedDict):
    id: str
    youtubeVideoId: str
    title: str
    caption: list[SegmentContract]


class VideoListAPIView(views.APIView):
    def get(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> Response[VideoListItemContract]:
        usecase = VideoUsecase(repository=VideoRepository())
        videos = usecase.getAllVideos()

        videoList: list[VideoListItemContract] = [
            VideoListItemContract(
                id=str(video.id),
                youtubeVideoId=video.youtube_video_id,
                title=video.title,
                createdAt=str(video.created_at),
            )
            for video in videos
        ]

        return Response(videoList, status=status.HTTP_200_OK)


class VideoItemAPIView(views.APIView):
    def get(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> Response[VideoItemContract]:
        id: uuid.UUID = kwargs["id"]

        usecase = VideoUsecase(repository=VideoRepository())
        video = usecase.getVideo(id=id)

        return Response(
            VideoItemContract(
                id=str(video.id),
                youtubeVideoId=video.youtube_video_id,
                title=video.title,
                caption=video.caption,
            ),
            status=status.HTTP_200_OK,
        )
