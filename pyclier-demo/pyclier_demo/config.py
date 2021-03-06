import logging.config
import os
from enum import Enum
from typing import Dict, List, Optional

import appdirs
from pyclier import LDMixin, load_conf_parser

from . import prog_name

log = logging.getLogger(__name__)


# ======================   Config file locations   ====================== #

CONF_DIRS = [
    appdirs.user_config_dir(prog_name),
    os.path.join("$PYCLIER_DEMO_HOME", "conf"),
    "$PYCLIER_DEMO_CONF_DIR",
    os.path.join(os.curdir, "conf"),
]

# ======================   Config class definition   ====================== #


class Config1(LDMixin):
    number_type: int
    string_type: str


class Object(LDMixin):
    attr1: str
    attr2: int


class Config2(LDMixin):
    list_type: List[str]
    dict_type: Dict[str, Object]


class Config(LDMixin):
    config1: Config1
    config2: Config2


# ======================   Config   ====================== #

# global config
_conf: Optional[Config] = None


def set_conf(d: dict):
    global _conf
    _conf = Config.from_dict(d)


def get_conf():
    global _conf
    if _conf is None:
        load_conf_parser(set_conf, CONF_DIRS)
    return _conf


conf_parser = load_conf_parser(set_conf, CONF_DIRS)
