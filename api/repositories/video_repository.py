import uuid
from api import models
from api.domain.video import Video
from api.usecases.video_usecase import VideoRepositoryInterface


class VideoRepository(VideoRepositoryInterface):
    def getAllVideos(self) -> list[Video]:
        videos = models.Video.objects.all()
        return [
            Video(
                id=x.id,
                title=x.title,
                youtube_video_id=x.youtube_video_id,
                caption=x.caption,
                created_at=x.created_at,
            )
            for x in videos
        ]

    def getVideo(self, id: uuid.UUID) -> Video:
        video = models.Video.objects.get(pk=id)
        return Video(
            id=video.id,
            title=video.title,
            youtube_video_id=video.youtube_video_id,
            caption=video.caption,
            created_at=video.created_at,
        )
