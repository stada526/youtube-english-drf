import abc
import uuid

from api.domain.video import Video


class VideoRepositoryInterface(abc.ABC):
    @abc.abstractmethod
    def getAllVideos(self) -> list[Video]:
        pass

    @abc.abstractmethod
    def getVideo(self, id: uuid.UUID) -> Video:
        pass


class VideoUsecase:
    def __init__(self, repository: VideoRepositoryInterface) -> None:
        self.repository = repository

    def getAllVideos(self) -> list[Video]:
        return self.repository.getAllVideos()

    def getVideo(self, id: uuid.UUID) -> Video:
        return self.repository.getVideo(id)
