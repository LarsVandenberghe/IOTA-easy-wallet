
import iota_wallet as iw
import os
from typing import List

class AccountInterface(object):
    def __init__(self, name, password):
        self.__password = password
        self.__name = name
        
        self.__account_manager = iw.AccountManager(
            storage_path='./{}-database'.format(self.__name)
        )
        self.__account_manager.set_stronghold_password(password)
        self.__account = self.__account_manager.get_account(self.__name)
        self.__account.sync().execute()

    def get_address(self) -> str:
        return self.__account.latest_address()['address']['inner']
        
    def available_balance(self) -> int:
        return self.__account.balance()["available"]

    def transfer(self, amount: int, address: str) -> object:
        transfer = iw.Transfer(
            amount=amount,
            address=address,
            remainder_value_strategy='ReuseAddress'
        )

        node_response: WalletMessage = self.__account.transfer(transfer)
        print(node_response)
        return node_response
        
    def backup(self):
        backup_dir_path = './backup'
        if not os.path.exists(backup_dir_path):
            os.makedirs(backup_dir_path)
        backup_file_path = self.__account_manager.backup(backup_dir_path, self.__password)
        
        print(f'Backup path: {backup_file_path}')
        
    def get_backup_files(self) -> List[str]:
        return os.listdir('./backup')

def create_account(name, password, node="https://api.hornet-0.testnet.chrysalis2.com") -> AccountInterface:
    temp_account_manager = iw.AccountManager(
        storage_path='./{}-database'.format(name)
    )
    temp_account_manager.set_stronghold_password(password)
    temp_account_manager.store_mnemonic("Stronghold")
    client_options = {
        "nodes": [
            {
                "url": node,
                "auth": None,
                "disabled": False
            }
        ],
        "local_pow": True
    }
    account_initialiser = temp_account_manager.create_account(client_options)
    account_initialiser.alias(name)
    account_initialiser.initialise()
    return login(name, password)
    

def restore_account(file_name, name, password) -> AccountInterface:
    backup_file_path = './backup/{}'.format(file_name)
    temp_account_manager = iw.AccountManager(
        storage_path='./{}-database'.format(name)
    )
    temp_account_manager.import_accounts(backup_file_path, password)
    temp_account_manager = None
    return login(name, password)

def login(name, password) -> AccountInterface:
    return AccountInterface(name, password)
