# DO NOT EDIT THIS FILE!
#
# This file is generated from the CDP specification. If you need to make
# changes, edit the generator and regenerate all of the modules.
#
# CDP domain: Media (experimental)

from __future__ import annotations

import typing
from dataclasses import dataclass

from .util import T_JSON_DICT, event_class


class PlayerId(str):
    """
    Players will get an ID that is unique within the agent context.
    """

    def to_json(self) -> str:
        return self

    @classmethod
    def from_json(cls, json: str) -> PlayerId:
        return cls(json)

    def __repr__(self):
        return "PlayerId({})".format(super().__repr__())


class Timestamp(float):
    def to_json(self) -> float:
        return self

    @classmethod
    def from_json(cls, json: float) -> Timestamp:
        return cls(json)

    def __repr__(self):
        return "Timestamp({})".format(super().__repr__())


@dataclass
class PlayerMessage:
    """
    Have one type per entry in MediaLogRecord::Type
    Corresponds to kMessage
    """

    #: Keep in sync with MediaLogMessageLevel
    #: We are currently keeping the message level 'error' separate from the
    #: PlayerError type because right now they represent different things,
    #: this one being a DVLOG(ERROR) style log message that gets printed
    #: based on what log level is selected in the UI, and the other is a
    #: representation of a media::PipelineStatus object. Soon however we're
    #: going to be moving away from using PipelineStatus for errors and
    #: introducing a new error type which should hopefully let us integrate
    #: the error log level into the PlayerError type.
    level: str

    message: str

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["level"] = self.level
        json["message"] = self.message
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> PlayerMessage:
        return cls(
            level=str(json["level"]),
            message=str(json["message"]),
        )


@dataclass
class PlayerProperty:
    """
    Corresponds to kMediaPropertyChange
    """

    name: str

    value: str

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["name"] = self.name
        json["value"] = self.value
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> PlayerProperty:
        return cls(
            name=str(json["name"]),
            value=str(json["value"]),
        )


@dataclass
class PlayerEvent:
    """
    Corresponds to kMediaEventTriggered
    """

    timestamp: Timestamp

    value: str

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["timestamp"] = self.timestamp.to_json()
        json["value"] = self.value
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> PlayerEvent:
        return cls(
            timestamp=Timestamp.from_json(json["timestamp"]),
            value=str(json["value"]),
        )


@dataclass
class PlayerErrorSourceLocation:
    """
    Represents logged source line numbers reported in an error.
    NOTE: file and line are from chromium c++ implementation code, not js.
    """

    file: str

    line: int

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["file"] = self.file
        json["line"] = self.line
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> PlayerErrorSourceLocation:
        return cls(
            file=str(json["file"]),
            line=int(json["line"]),
        )


@dataclass
class PlayerError:
    """
    Corresponds to kMediaError
    """

    error_type: str

    #: Code is the numeric enum entry for a specific set of error codes, such
    #: as PipelineStatusCodes in media/base/pipeline_status.h
    code: int

    #: A trace of where this error was caused / where it passed through.
    stack: typing.List[PlayerErrorSourceLocation]

    #: Errors potentially have a root cause error, ie, a DecoderError might be
    #: caused by an WindowsError
    cause: typing.List[PlayerError]

    #: Extra data attached to an error, such as an HRESULT, Video Codec, etc.
    data: dict

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json["errorType"] = self.error_type
        json["code"] = self.code
        json["stack"] = [i.to_json() for i in self.stack]
        json["cause"] = [i.to_json() for i in self.cause]
        json["data"] = self.data
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> PlayerError:
        return cls(
            error_type=str(json["errorType"]),
            code=int(json["code"]),
            stack=[PlayerErrorSourceLocation.from_json(i) for i in json["stack"]],
            cause=[PlayerError.from_json(i) for i in json["cause"]],
            data=dict(json["data"]),
        )


def enable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Enables the Media domain
    """
    cmd_dict: T_JSON_DICT = {
        "method": "Media.enable",
    }
    json = yield cmd_dict


def disable() -> typing.Generator[T_JSON_DICT, T_JSON_DICT, None]:
    """
    Disables the Media domain.
    """
    cmd_dict: T_JSON_DICT = {
        "method": "Media.disable",
    }
    json = yield cmd_dict


@event_class("Media.playerPropertiesChanged")
@dataclass
class PlayerPropertiesChanged:
    """
    This can be called multiple times, and can be used to set / override /
    remove player properties. A null propValue indicates removal.
    """

    player_id: PlayerId
    properties: typing.List[PlayerProperty]

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> PlayerPropertiesChanged:
        return cls(
            player_id=PlayerId.from_json(json["playerId"]),
            properties=[PlayerProperty.from_json(i) for i in json["properties"]],
        )


@event_class("Media.playerEventsAdded")
@dataclass
class PlayerEventsAdded:
    """
    Send events as a list, allowing them to be batched on the browser for less
    congestion. If batched, events must ALWAYS be in chronological order.
    """

    player_id: PlayerId
    events: typing.List[PlayerEvent]

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> PlayerEventsAdded:
        return cls(
            player_id=PlayerId.from_json(json["playerId"]),
            events=[PlayerEvent.from_json(i) for i in json["events"]],
        )


@event_class("Media.playerMessagesLogged")
@dataclass
class PlayerMessagesLogged:
    """
    Send a list of any messages that need to be delivered.
    """

    player_id: PlayerId
    messages: typing.List[PlayerMessage]

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> PlayerMessagesLogged:
        return cls(
            player_id=PlayerId.from_json(json["playerId"]),
            messages=[PlayerMessage.from_json(i) for i in json["messages"]],
        )


@event_class("Media.playerErrorsRaised")
@dataclass
class PlayerErrorsRaised:
    """
    Send a list of any errors that need to be delivered.
    """

    player_id: PlayerId
    errors: typing.List[PlayerError]

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> PlayerErrorsRaised:
        return cls(
            player_id=PlayerId.from_json(json["playerId"]),
            errors=[PlayerError.from_json(i) for i in json["errors"]],
        )


@event_class("Media.playersCreated")
@dataclass
class PlayersCreated:
    """
    Called whenever a player is created, or when a new agent joins and receives
    a list of active players. If an agent is restored, it will receive the full
    list of player ids and all events again.
    """

    players: typing.List[PlayerId]

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> PlayersCreated:
        return cls(players=[PlayerId.from_json(i) for i in json["players"]])
