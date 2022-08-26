from dataAccess.postgresql.connection import openConnection
from logger.logger import get_logger

def insert_all_exchange_rate(input_object_list):
    logger = get_logger()

    conn = openConnection()
    
    try:
        for object in input_object_list:
            conn.execute("""
                        INSERT INTO 
                        foreign_exchange_rate (quoted_date, currency, cash_buy, cash_sell, spot_buy, spot_sell)
                        VALUES (%(quoted_date)s, %(currency)s, %(cash_buy)s, %(cash_sell)s, %(spot_buy)s, %(spot_sell)s);
                        """,
                        {'quoted_date' : object.quoted_date, 
                        'currency' : object.currency, 
                        'cash_buy' : object.cash_buying,
                        'cash_sell' : object.cash_selling,
                        'spot_buy' : object.spot_buying,
                        'spot_sell' : object.spot_selling})

    except BaseException as e:
        conn.rollback()
        print("BaseException : %s", e)
        logger.error("BaseException : %s", e)

    else:
        conn.commit()
        print("All Currency Exchange Rate Insert Success")
        logger.info("All Currency Exchange Rate Insert Success")
        
    finally:
        conn.close()
