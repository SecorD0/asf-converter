import os
import sys
from pathlib import Path

if getattr(sys, 'frozen', False):
    ROOT_DIR = Path(sys.executable).parent.absolute()
else:
    ROOT_DIR = Path(__file__).parent.parent.absolute()

CONFIG_DIR = os.path.join(ROOT_DIR, 'config')
MAFILES_DIR = os.path.join(ROOT_DIR, 'maFiles')

LOG_FILE = os.path.join(ROOT_DIR, 'log.log')
ERRORS_FILE = os.path.join(ROOT_DIR, 'errors.log')

ACCOUNTS_FILE = os.path.join(ROOT_DIR, 'accounts.txt')
SAMPLE_CONFIG_FILE = os.path.join(ROOT_DIR, 'sample_config.json')
