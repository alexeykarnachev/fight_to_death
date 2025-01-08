from typing import Literal

from pydantic_settings import BaseSettings

Resolution = Literal[
    "1280x720",
    "1920x1080",
    "2560x1440",
    "3840x2160",
]


class GraphicsSettings(BaseSettings):
    resolution: Resolution = "1920x1080"
    is_fullscreen: bool = False
    is_vsync: bool = True


class Settings(BaseSettings):
    graphics: GraphicsSettings = GraphicsSettings()

    class Config:
        config_file = "settings.toml"
