# IOTA-easy-wallet

[![status](https://img.shields.io/badge/Status-Alpha-yellow.svg)](https://github.com/LarsVandenberghe/IOTA-easy-wallet)



## Introduction

A simple python IOTA wallet implementation. This module will help new developers tinker around with IOTA wallets with an easy to understand interface.



## Prerequisites

Download the IOTA wallet wheel file on the [official documentation](https://wallet-lib.docs.iota.org/libraries/python/getting_started.html). The easiest way is to download it from the nightly link. 



## What is in the module?

In the example console application `example-console-app.py`, on the first line, you can find all important classes and methods.

```python
from domain.iota_easy_wallet import create_account, restore_account, login, AccountInterface
```

* create_account
* restore_account
* login
* AccountInterface

The first three items are methods for retrieving the last item. In other words: create_account, restore_account and login will return a AccountInterface object. With this object you are already logged into the account and are able to do all actions described in the AccountInterface section.



## Create account

`create_account("username", "mypassword") -> AccountInterface` 

This method is designed to create an account based on a username and a password. A folder will be created starting with the username, followed by `-database`. If a database already exists for this user an error will be thrown.

An additional parameter can be provided to specify what node to connect to. Because this is mainly meant to be used for testing the default value is set to a testnet node.

`create_account(name, password, node="https://api.hornet-0.testnet.chrysalis2.com") -> AccountInterface`

**NOTE: Please becarefull with creating accounts on the mainnet and sending funds to them without creating a backup file first!** (more info on creating backup files in the AccountInterface section)

If you plan on making a production ready application make sure to also ready the documentation about [backup and security](https://chrysalis.docs.iota.org/guides/backup_security.html).



## Restore account

`restore_account("somedate-backup-wallet.stronghold", "username", "mypassword") -> AccountInterface`

For now you have to manually create a folder called `backup`in the root directory next to the `domain` folder. Once the backup file is in that folder the restore_method will be able to find this file. The username and password have to be the same as the ones used to create the stronghold file.



## Login

`login("username", "mypassword") -> AccountInterface`

This method kinda speaks for itself. You can only use this method if an account already has been created or restored. 



## AccountInterface

`This class should not be constructed from code. Thats why the previous 3 methods exist.`

In this section the methods for managing the logged in account are explained.



> ### 	Address
> `get_address() -> str`
>
> This method will return an address to send funds to.
>
> **NOTE: If you are developing on the testnet (default), use https://faucet.testnet.chrysalis2.com/ to request tokens.**



> ### 	Balance
> `available_balance() -> int`
>
> This method will return the balance on the account in IOTA. This is 1 MIOTA is 1_000_000 IOTA.



> ### 	Transfer
> `transfer(amount: int, address: str) -> object`
>
> This method can send tokens to other addresses. Amount is also expressed in IOTA (not in MIOTA).



> ### Backup
>
> `backup() -> None`
>
> This method will create a new `.stronghold` file in the `/backup` folder for the logged in user with its current username and password. If the folder doesn't exist it will create one.



>  ### All backup files
>
> `get_backup_files() -> List[str]`
>
> This method will return a list of all filesnames in the `/backup` folder.

