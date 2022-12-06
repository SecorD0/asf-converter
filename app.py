import glob
import logging
import os

from pretty_utils.miscellaneous.files import read_json, write_json, read_lines, join_path

from data import config
from utils.miscellaneous.print_to_log import print_to_log

if __name__ == '__main__':
    try:
        accounts = read_lines('accounts.txt', True)
        created = 0
        with_mafiles = 0
        for i, account in enumerate(accounts):
            login = account
            status = '[!]'
            try:
                status = '[X]'
                sample_config = read_json(config.SAMPLE_CONFIG_FILE)
                if ';' in account:
                    account = account.split(';')
                else:
                    account = account.split('\t')

                login = account[0].lower()
                if login:
                    password = account[1]
                    sample_config['SteamLogin'] = login
                    sample_config['SteamPassword'] = password
                    if 'https://steamcommunity.com/' in sample_config['SteamTradeToken']:
                        sample_config['SteamTradeToken'] = sample_config['SteamTradeToken'].split('token=')[1]

                    for file in glob.glob(join_path((config.MAFILES_DIR, '*.maFile'))):
                        try:
                            content = read_json(file)
                            if content['account_name'] == login:
                                os.replace(file, join_path((config.CONFIG_DIR, f'{login}.maFile')))
                                status = '[V]'
                                with_mafiles += 1
                                break
                        except:
                            pass

                    write_json(path=join_path((config.CONFIG_DIR, f'{login}.json')), obj=sample_config, indent=2)
                    created += 1

                else:
                    status = '[!]'

            except:
                pass

            finally:
                print_to_log(f'{status} {i + 1}/{len(accounts)} | {login}')

        print(f'\nTotal accounts: {len(accounts)}'
              f'\nCreated configs: {created}'
              f'\nAccounts with maFiles: {with_mafiles}')

    except:
        logging.exception('script')

    finally:
        input('\nPress Enter to exit.\n')
