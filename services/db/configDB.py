from deta import Deta
from config import settings
from typing import Optional


deta = Deta(settings.DETA_BASE_KEY)  # configure your Deta project
config_db = deta.Base('config')


async def get_config_from_db(key: str) -> Optional[str]:
    """
    Get a config from the database
    :param key: The key of the config
    :return: The value of the config
    """
    config = await config_db.get(key)
    if config:
        return config['value']
    return None