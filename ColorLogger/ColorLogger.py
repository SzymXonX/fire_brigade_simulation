import logging
import colorlog


class ColorLogger:
    def __init__(self, default_color="white"):
        self.default_color = default_color
        self.loggers = {}

    def getLogger(self, name, color=None):
        if name in self.loggers:
            return self.loggers[name]

        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        handler = colorlog.StreamHandler()
        handler.setFormatter(colorlog.ColoredFormatter(
            "%(log_color)s %(name)s %(message)s",
            log_colors={"INFO": color or self.default_color}
        ))

        logger.addHandler(handler)
        self.loggers[name] = logger
        return logger
