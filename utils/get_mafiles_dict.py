import glob
import os
from typing import Dict

from pretty_utils.miscellaneous.files import read_json

from data import config


def get_mafiles_dict() -> Dict[str, str]:
    mafiles_dict = {}
    mafiles = glob.glob(os.path.join(config.MAFILES_DIR, '*.maFile'))
    for mafile in mafiles:
        content = read_json(mafile)
        login = content.get('account_name')
        mafiles_dict[login] = mafile

    return mafiles_dict
