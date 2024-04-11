import logging as log
import os

def credentialsDB():
    db_user = os.environ['db_user']
    db_pass = os.environ['db_pass']
    db_name = os.environ['db_name']
    db_port = os.environ['db_port']
    db_host = os.environ['db_host']

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

