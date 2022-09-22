from dataAccess.postgresql.connection import openConnection
from logger.logger import get_logger, close_handler
from util.string_to_number import str_to_int

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
        logger.error("BaseException : %s" % e, exc_info=True)

    else:
        conn.commit()
        
    finally:
        conn.close()
        close_handler(logger)

def insert_all_trading_details(data_dict):
    logger = get_logger()

    try:
        conn = openConnection()
        
        if not data_dict:
            return
        
        i = 0
        for data_row in data_dict['data_list']:

            conn.execute("""
                        INSERT INTO 
                        stock_trading_details 
                            (datetime, 
                            security_code, 
                            mainland_area_investors_total_buy, mainland_area_investors_total_sell, mainland_area_investors_difference, 
                            foreign_dealers_total_buy, foreign_dealers_total_sell, foreign_dealers_difference, 
                            securities_investment_trust_companies_total_buy, securities_investment_trust_companies_total_sell, securities_investment_trust_companies_difference, 
                            dealers_difference, 
                            dealers_proprietary_total_buy, dealers_proprietary_total_sell, dealers_proprietary_difference, 
                            dealers_hedge_total_buy, dealers_hedge_total_sell, dealers_hedge_difference, 
                            total_difference)
                        VALUES 
                            (%(datetime)s, 
                            %(security_code)s, 
                            %(mainland_area_investors_total_buy)s, %(mainland_area_investors_total_sell)s, %(mainland_area_investors_difference)s, 
                            %(foreign_dealers_total_buy)s, %(foreign_dealers_total_sell)s, %(foreign_dealers_difference)s, 
                            %(securities_investment_trust_companies_total_buy)s, %(securities_investment_trust_companies_total_sell)s, %(securities_investment_trust_companies_difference)s, 
                            %(dealers_difference)s, 
                            %(dealers_proprietary_total_buy)s, %(dealers_proprietary_total_sell)s, %(dealers_proprietary_difference)s, 
                            %(dealers_hedge_total_buy)s, %(dealers_hedge_total_sell)s, %(dealers_hedge_difference)s, 
                            %(total_difference)s);
                        """,
                        {'datetime' : data_dict['current_datetime'], 
                        'security_code' : data_row[0], 
                        'mainland_area_investors_total_buy' : str_to_int(data_row[1]),
                        'mainland_area_investors_total_sell' : str_to_int(data_row[2]),
                        'mainland_area_investors_difference' : str_to_int(data_row[3]),
                        'foreign_dealers_total_buy' : str_to_int(data_row[4]),
                        'foreign_dealers_total_sell' : str_to_int(data_row[5]),
                        'foreign_dealers_difference' : str_to_int(data_row[6]),
                        'securities_investment_trust_companies_total_buy' : str_to_int(data_row[7]),
                        'securities_investment_trust_companies_total_sell' : str_to_int(data_row[8]),
                        'securities_investment_trust_companies_difference' : str_to_int(data_row[9]),
                        'dealers_difference' : str_to_int(data_row[10]),
                        'dealers_proprietary_total_buy' : str_to_int(data_row[11]),
                        'dealers_proprietary_total_sell' : str_to_int(data_row[12]),
                        'dealers_proprietary_difference' : str_to_int(data_row[13]),
                        'dealers_hedge_total_buy' : str_to_int(data_row[14]),
                        'dealers_hedge_total_sell' : str_to_int(data_row[15]),
                        'dealers_hedge_difference' : str_to_int(data_row[16]),
                        'total_difference' : str_to_int(data_row[17])})       
        
    except BaseException as e:
        conn.rollback()
        logger.error("BaseException : %s" % e, exc_info=True)

    else:
        conn.commit()
        
    finally:
        conn.close()
        close_handler(logger)

def insert_trading_details(data_row, current_datetime):
    logger = get_logger()

    try:
        conn = openConnection()
        
        if not data_row:
            return
        
        conn.execute("""
                        INSERT INTO 
                        stock_trading_details 
                            (datetime, 
                            security_code, 
                            mainland_area_investors_total_buy, mainland_area_investors_total_sell, mainland_area_investors_difference, 
                            foreign_dealers_total_buy, foreign_dealers_total_sell, foreign_dealers_difference, 
                            securities_investment_trust_companies_total_buy, securities_investment_trust_companies_total_sell, securities_investment_trust_companies_difference, 
                            dealers_difference, 
                            dealers_proprietary_total_buy, dealers_proprietary_total_sell, dealers_proprietary_difference, 
                            dealers_hedge_total_buy, dealers_hedge_total_sell, dealers_hedge_difference, 
                            total_difference)
                        VALUES 
                            (%(datetime)s, 
                            %(security_code)s, 
                            %(mainland_area_investors_total_buy)s, %(mainland_area_investors_total_sell)s, %(mainland_area_investors_difference)s, 
                            %(foreign_dealers_total_buy)s, %(foreign_dealers_total_sell)s, %(foreign_dealers_difference)s, 
                            %(securities_investment_trust_companies_total_buy)s, %(securities_investment_trust_companies_total_sell)s, %(securities_investment_trust_companies_difference)s, 
                            %(dealers_difference)s, 
                            %(dealers_proprietary_total_buy)s, %(dealers_proprietary_total_sell)s, %(dealers_proprietary_difference)s, 
                            %(dealers_hedge_total_buy)s, %(dealers_hedge_total_sell)s, %(dealers_hedge_difference)s, 
                            %(total_difference)s);
                        """,
                        {'datetime' : current_datetime, 
                        'security_code' : data_row[0], 
                        'mainland_area_investors_total_buy' : str_to_int(data_row[1]),
                        'mainland_area_investors_total_sell' : str_to_int(data_row[2]),
                        'mainland_area_investors_difference' : str_to_int(data_row[3]),
                        'foreign_dealers_total_buy' : str_to_int(data_row[4]),
                        'foreign_dealers_total_sell' : str_to_int(data_row[5]),
                        'foreign_dealers_difference' : str_to_int(data_row[6]),
                        'securities_investment_trust_companies_total_buy' : str_to_int(data_row[7]),
                        'securities_investment_trust_companies_total_sell' : str_to_int(data_row[8]),
                        'securities_investment_trust_companies_difference' : str_to_int(data_row[9]),
                        'dealers_difference' : str_to_int(data_row[10]),
                        'dealers_proprietary_total_buy' : str_to_int(data_row[11]),
                        'dealers_proprietary_total_sell' : str_to_int(data_row[12]),
                        'dealers_proprietary_difference' : str_to_int(data_row[13]),
                        'dealers_hedge_total_buy' : str_to_int(data_row[14]),
                        'dealers_hedge_total_sell' : str_to_int(data_row[15]),
                        'dealers_hedge_difference' : str_to_int(data_row[16]),
                        'total_difference' : str_to_int(data_row[17])})     
        
    except BaseException as e:
        conn.rollback()
        logger.error("BaseException : %s" % e, exc_info=True)

    else:
        conn.commit()
        
    finally:
        conn.close()
        close_handler(logger)