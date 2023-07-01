import logging
import os

from pretty_utils.miscellaneous.files import read_json, write_json, read_lines, join_path

from data import config
from utils.get_mafiles_dict import get_mafiles_dict
from utils.print_to_log import print_to_log

if __name__ == '__main__':
    try:
        created = 0
        with_mafiles = 0
        accounts = read_lines(path=config.ACCOUNTS_FILE, skip_empty_rows=True)
        mafiles = get_mafiles_dict()
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

                    if login in mafiles:
                        os.replace(mafiles[login], join_path((config.CONFIG_DIR, f'{login}.maFile')))
                        status = '[V]'
                        with_mafiles += 1

                    write_json(path=join_path((config.CONFIG_DIR, f'{login}.json')), obj=sample_config, indent=2)
                    created += 1

                else:
                    status = '[!]'

            except:
                logging.exception(f'account | {login}')

            finally:
                print_to_log(f'{status} {i + 1}/{len(accounts)} | {login}')

        print(f'''
Total accounts: {len(accounts)}
Created configs: {created}
Accounts with maFiles: {with_mafiles}''')

    except:
        logging.exception('main')

    finally:
        input('\nPress Enter to exit.\n')
