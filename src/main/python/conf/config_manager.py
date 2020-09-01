import threading

from conf.config import ImageSimilarityConfig


class ConfigManager:
    __instance = None
    _lock = threading.RLock()


    @classmethod
    def get_instance(cls) -> ImageSimilarityConfig:
        if not cls.__instance:
            with cls._lock:
                if not cls.__instance:
                    cls.__instance = ImageSimilarityConfig()
        return cls.__instance
