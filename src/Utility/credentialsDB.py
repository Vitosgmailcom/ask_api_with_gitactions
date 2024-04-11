import logging as log
import os

def credentialsDB():
    db_user = os.getenv('db_user')
    db_pass = os.getenv('db_pass')
    db_name = os.getenv('db_name')
    db_port = os.getenv('db_port')
    db_host = os.getenv('db_host')

    if not db_user and not db_pass:
        raise Exception(f"The db_user and db_pass must be set up")
    else:
        cred_info={
            "db_user": db_user,
            "db_pass": db_pass,
            "db_name": db_name,
            "db_port": db_port,
            "db_host": db_host,
        }
        log.info(cred_info)
        # import pdb; pdb.set_trace()

        return cred_info

