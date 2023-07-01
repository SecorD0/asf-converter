import os.path

from pretty_utils.miscellaneous.files import touch, write_json

from data import config


def create_files() -> None:
    touch(config.FILES_DIR)
    touch(config.MAFILES_DIR)
    touch(config.CONFIG_DIR)
    touch(config.LOG_FILE, True)
    touch(config.ACCOUNTS_FILE, True)
    if not os.path.exists(config.SAMPLE_CONFIG_FILE):
        current_config = {
            'SteamLogin': 'DO NOT TOUCH',
            'SteamPassword': 'DO NOT TOUCH',
            'SteamUserPermissions': {'76561XXXXXXXXXXXX': 3},
            'SteamTradeToken': 'https://steamcommunity.com/tradeoffer/new/?partner=00000000&token=XXXXXXXX',
            'AcceptGifts': False,
            'AutoSteamSaleEvent': True,
            'BotBehaviour': 0,
            'CompleteTypesToSend': [],
            'CustomGamePlayedWhileFarming': None,
            'CustomGamePlayedWhileIdle': None,
            'Enabled': True,
            'FarmingOrders': [],
            'FarmPriorityQueueOnly': False,
            'GamesPlayedWhileIdle': [],
            'HoursUntilCardDrops': 3,
            'LootableTypes': [
                0,
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12
            ],
            'MatchableTypes': [
                5
            ],
            'OnlineFlags': 0,
            'OnlineStatus': 0,
            'PasswordFormat': 0,
            'Paused': False,
            'RedeemingPreferences': 0,
            'RemoteCommunication': 3,
            'SendOnFarmingFinished': True,
            'SendTradePeriod': 24,
            'ShutdownOnFarmingFinished': False,
            'SkipRefundableGames': False,
            'TradingPreferences': 0,
            'TransferableTypes': [
                0,
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12
            ],
            'UseLoginKeys': True,
            'UserInterfaceMode': 0,
            'SteamMasterClanID': 0
        }

        write_json(config.SAMPLE_CONFIG_FILE, current_config, 2)


create_files()
