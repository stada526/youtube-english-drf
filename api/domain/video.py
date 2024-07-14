import datetime
from typing import TypedDict
import uuid


class Word(TypedDict):
    word: str
    start: float
    end: float


class Segment(TypedDict):
    start: float
    end: float
    text: str
    words: list[Word]


class Video:
    def __init__(
        self,
        id: uuid.UUID,
        title: str,
        youtube_video_id: str,
        created_at: datetime.datetime,
        caption: list[Segment],
    ) -> None:
        self.id = id
        self.title = title
        self.youtube_video_id = youtube_video_id
        self.created_at = created_at
        self.caption = caption
