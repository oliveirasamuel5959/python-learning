import logging
import sys

# Nome do logger da sua aplicação
LOGGER_NAME = "account_api"

def get_logger() -> logging.Logger:
    logger = logging.getLogger(LOGGER_NAME)

    # Evita criar handlers duplicados quando o módulo é importado várias vezes
    if not logger.handlers:
        logger.setLevel(logging.INFO)

        # Handler para console
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)

        # Formato do log
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.propagate = False  # impede duplicação com uvicorn

    return logger


# Logger que você vai importar
logger = get_logger()

