"""myTableSQLPerformanceWatchList.py."""

__title__: str = "myTableSQLPerformanceWatchList"
__version__: str = "0.1.1"
__author__: str = "Oliver Rudow"
__email__: str = "oliver.rudow@googlemail.com"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import dataclasses
import sqlite3
from mydatabase import mySQLDataBase, myTableSQL
from myauxiliary import myAuxiliary
from mysharesdefinition import myPerformanceWatchListDefinitions, myStaticWatchListDefinitions


@dataclasses.dataclass(init=False)
class MyTableSQLPerformanceWatchList(myTableSQL.MyTableSQL):
    """
        Class for providing variables and functions to manage the Web Shop List.
        The Class is based on SQLite3.
    """

    _str_performance_watch_list_name: str = dataclasses.field(repr=False, default='')

    _dict_table_settings: dict[str, tuple] = dataclasses.field(repr=False, default=dict[str, tuple])

    _list_performance_watch_list_tables: list[str] = dataclasses.field(repr=False, default=list[str])

    _flag_scan_watch_list: bool = dataclasses.field(repr=False, default=True)

    # column indices
    _int_performance_watch_list_quote_isin_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_ask_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_ask_size_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_bid_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_bid_size_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_current_price_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_day_high_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_interday_momentum_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_day_low_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_relative_daily_span_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_open_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_previous_close_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_regular_market_change_percent_column_index: int = dataclasses.field(repr=False,
                                                                                                    default=0)
    _int_performance_watch_list_intraday_momentum_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_volume_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_average_volume_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_relative_volume_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_average_daily_volume_10_day_column_index: int = (
        dataclasses.field(repr=False, default=0))
    _int_performance_watch_list_relative_volume_10_day_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_beta_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_fifty_two_week_low_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_fifty_two_week_low_momentum_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_fifty_two_week_high_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_fifty_two_week_high_momentum_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_fifty_day_average_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_fifty_day_momentum_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_two_hundred_day_average_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_two_hundred_day_momentum_column_index: int = dataclasses.field(repr=False, default=0)

    # column names
    _str_performance_watch_list_quote_isin_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_ask_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_ask_size_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_bid_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_bid_size_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_current_price_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_day_high_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_interday_momentum_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_day_low_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_relative_daily_span_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_open_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_previous_close_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_regular_market_change_percent_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_intraday_momentum_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_volume_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_average_volume_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_relative_volume_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_average_daily_volume_10_day_column_name: (
        str) = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_relative_volume_10_day_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_beta_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_fifty_two_week_low_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_fifty_two_week_low_momentum_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_fifty_two_week_high_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_fifty_two_week_high_momentum_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_fifty_day_average_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_fifty_day_momentum_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_two_hundred_day_average_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_two_hundred_day_momentum_column_name: str = dataclasses.field(repr=False, default='')

    # value
    _str_performance_watch_list_quote_isin_value: str = dataclasses.field(repr=False, default='')
    _float_performance_watch_list_ask_value: float | str = dataclasses.field(repr=False, default='')
    _int_performance_watch_list_ask_size_value: int | str = dataclasses.field(repr=False, default='')
    _float_performance_watch_list_bid_value: float | str = dataclasses.field(repr=False, default='')
    _int_performance_watch_list_bid_size_value: int | str = dataclasses.field(repr=False, default='')
    _float_performance_watch_list_current_price_value: float | str = dataclasses.field(repr=False, default='')
    _float_performance_watch_list_day_high_value: float | str = dataclasses.field(repr=False, default='')
    _float_performance_watch_list_interday_momentum_value: float | str = dataclasses.field(repr=False, default='')
    _float_performance_watch_list_day_low_value: float | str = dataclasses.field(repr=False, default='')
    _float_performance_watch_list_relative_daily_span_value: float | str = dataclasses.field(repr=False, default='')
    _float_performance_watch_list_open_value: float | str = dataclasses.field(repr=False, default='')
    _float_performance_watch_list_previous_close_value: float | str = dataclasses.field(repr=False, default='')
    _float_performance_watch_list_regular_market_change_percent_value: float | str = dataclasses.field(repr=False, default='')
    _float_performance_watch_list_intraday_momentum_value: float | str = dataclasses.field(repr=False, default='')
    _int_performance_watch_list_volume_value: int | str = dataclasses.field(repr=False, default='')
    _int_performance_watch_list_average_volume_value: int | str = dataclasses.field(repr=False, default='')
    _float_performance_watch_list_relative_volume_value: float | str = dataclasses.field(repr=False, default='')
    _int_performance_watch_list_average_daily_volume_10_day_value: int | str = (
        dataclasses.field(repr=False, default=''))
    _float_performance_watch_list_relative_volume_10_day_value: float | str = dataclasses.field(repr=False, default='')
    _float_performance_watch_list_beta_value: float | str = dataclasses.field(repr=False, default='')
    _float_performance_watch_list_fifty_two_week_low_column_value: float | str  = (
        dataclasses.field(repr=False, default=''))
    _float_performance_watch_list_fifty_two_week_low_momentum_column_value: float | str = (
        dataclasses.field(repr=False, default=''))
    _float_performance_watch_list_fifty_two_week_high_column_value: float | str = (
        dataclasses.field(repr=False, default=''))
    _float_performance_watch_list_fifty_two_week_high_momentum_column_value: float | str = (
        dataclasses.field(repr=False, default=''))
    _float_performance_watch_list_fifty_day_average_column_value: float | str  = (
        dataclasses.field(repr=False, default=''))
    _float_performance_watch_list_fifty_day_momentum_column_value: float | str = (
        dataclasses.field(repr=False, default=''))
    _float_performance_watch_list_two_hundred_day_average_column_value: float | str  = (
        dataclasses.field(repr=False, default=''))
    _float_performance_watch_list_two_hundred_day_momentum_column_value: float | str = (
        dataclasses.field(repr=False, default=''))

    # source
    _str_source_table_name: str = dataclasses.field(repr=False, default='')
    _str_source_quote_isin_column_name: str = dataclasses.field(repr=False, default='')
    _str_source_quote_sector_column_name: str = dataclasses.field(repr=False, default='')
    _str_source_quote_industry_column_name: str = dataclasses.field(repr=False, default='')

    # Variables for use with SQLite3
    _str_insert_string: str = dataclasses.field(repr=False, default='')

    _list_entire_row: list = dataclasses.field(repr=False, default_factory=list)

    def __init__(self, the_sql_connection: sqlite3.Connection,
                 the_sql_cursor: sqlite3.Cursor,
                 flag_scan_watch_list: bool) -> None:
        super().__init__(the_sql_connection, the_sql_cursor)

        self._dict_table_settings = {}

        # SQL Data Base Scheme
        self.set_sql_data_base_schema(myPerformanceWatchListDefinitions.STR_DATA_BASE_SCHEMA_NAME)

        # SQL Table Name
        self.set_flag_add_date_2_table_name(myPerformanceWatchListDefinitions.DATA_BASE_FLAG_ADD_DATE)
        self.set_table_name(myPerformanceWatchListDefinitions.STR_DATA_BASE_TABLE_NAME)

        # delete preceding tables
        self.set_flag_clean_preceded_tables(myPerformanceWatchListDefinitions.DATA_BASE_FLAG_CLEAN_PRECEDED_DATA)
        self.set_number_preceded_tables(myPerformanceWatchListDefinitions.DATA_BASE_INT_NUMBER_PRECEDED_DATA)

        self._get_available_performance_watch_list_tables()

        # flag scan watch list true = creates a new watch list
        self.set_flag_scan_watch_list(flag_scan_watch_list)

        if self._flag_scan_watch_list:
            # write modus

            if self._flag_clean_preceded_tables:

                self.clean_preceded_tables(self._str_table_name)

            # add date to table name
            if self._flag_add_date_2_file_name:

                self.set_table_name(myAuxiliary.add_date_2_object_name(self.get_table_name, 'tailing'))

        else:
            # read only modus

            if self._list_performance_watch_list_tables.__len__() > 0:

                self.set_table_name(self._list_performance_watch_list_tables[0])

            else:

                self.set_table_name(myPerformanceWatchListDefinitions.STR_DATA_BASE_TABLE_NAME)

        # column quote isin
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_QUOTE_ISIN

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column ask
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_ASK

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column ask size
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_ASK_SIZE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column bid
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_BID

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column bid size
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_BID_SIZE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column current price
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_CURRENT_PRICE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column day high
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_DAY_HIGH

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column day high
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_INTERDAY_MOMENTUM

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column day low
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_DAY_LOW

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column daily span
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_RELATIVE_DAILY_SPAN

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column open
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_OPEN

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column previous close
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_PREVIOUS_CLOSE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column regular market change percent
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_REGULAR_MARKET_CHANGE_PERCENT

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column intraday_momentum
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_INTRADAY_MOMENTUM

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column volume
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_VOLUME

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column average volume
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_AVERAGE_VOLUME

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column relative volume
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_RELATIVE_VOLUME

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column average daily volume 10 day
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_AVERAGE_DAILY_VOLUME_10_DAY

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column relative volume 10 day
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_RELATIVE_VOLUME_10_DAY

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column beta
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_BETA

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column fifty two week low
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_LOW

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column fifty two week low momentum
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_LOW_MOMENTUM

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column fifty two week high
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_HIGH

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column fifty two week momentum
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_HIGH_MOMENTUM

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column fifty day average
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_DAY_AVERAGE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column fifty day average
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_DAY_MOMENTUM

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column two hundred day average
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_TWO_HUNDRED_DAY_AVERAGE

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # column two hundred day momentum
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_TWO_HUNDRED_DAY_MOMENTUM

        self._dict_table_settings.update(
            {my_special_tuple[self._index_tuple.OPTION_NAME]: my_special_tuple[
                self._index_tuple.DATA_CONTENT]})

        # SQL Data Base Column Settings
        self.set_dict_table_settings(self._dict_table_settings)

        # check performance watch list exists
        self._str_some_table_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_QUOTE_ISIN)

        self._bool_sql_data_base_table = (self.check_sql_data_base_table_exists() and
                                      self.check_sql_data_base_table_column_name(self._str_some_table_column_name) and
                                      self.check_sql_data_base_table_is_not_empty())

        self._init_performance_watch_list_columns()

        self._init_source_table()

        if not self._bool_sql_data_base_table and self._flag_scan_watch_list:

            self.create_sql_data_base_table()

        # create SQL insert string for entire row
        self._helper_sql_data_base_insert_entire_row_string()

    def _init_performance_watch_list_columns(self) -> None:

        self._str_performance_watch_list_quote_isin_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_QUOTE_ISIN)

        self._int_performance_watch_list_quote_isin_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_QUOTE_ISIN)

        self._str_performance_watch_list_ask_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_ASK)

        self._int_performance_watch_list_ask_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_ASK)

        self._str_performance_watch_list_ask_size_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_ASK_SIZE)

        self._int_performance_watch_list_ask_size_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_ASK_SIZE)

        self._str_performance_watch_list_bid_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_BID)

        self._int_performance_watch_list_bid_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_BID)

        self._str_performance_watch_list_bid_size_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_BID_SIZE)

        self._int_performance_watch_list_bid_size_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_BID_SIZE)

        self._str_performance_watch_list_current_price_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_CURRENT_PRICE)

        self._int_performance_watch_list_current_price_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_CURRENT_PRICE)

        self._str_performance_watch_list_day_high_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_DAY_HIGH)

        self._int_performance_watch_list_day_high_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_DAY_HIGH)

        self._str_performance_watch_list_interday_momentum_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_INTERDAY_MOMENTUM)

        self._int_performance_watch_list_interday_momentum_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_INTERDAY_MOMENTUM)

        self._str_performance_watch_list_day_low_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_DAY_LOW)

        self._int_performance_watch_list_day_low_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_DAY_LOW)

        self._str_performance_watch_list_relative_daily_span_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_RELATIVE_DAILY_SPAN)

        self._int_performance_watch_list_relative_daily_span_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_RELATIVE_DAILY_SPAN)

        self._str_performance_watch_list_open_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_OPEN)

        self._int_performance_watch_list_open_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_OPEN)

        self._str_performance_watch_list_previous_close_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_PREVIOUS_CLOSE)

        self._int_performance_watch_list_previous_close_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_PREVIOUS_CLOSE)

        self._str_performance_watch_list_regular_market_change_percent_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_REGULAR_MARKET_CHANGE_PERCENT)

        self._int_performance_watch_list_regular_market_change_percent_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_REGULAR_MARKET_CHANGE_PERCENT)

        self._str_performance_watch_list_intraday_momentum_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_INTRADAY_MOMENTUM)

        self._int_performance_watch_list_intraday_momentum_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_INTRADAY_MOMENTUM)

        self._str_performance_watch_list_volume_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_VOLUME)

        self._int_performance_watch_list_volume_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_VOLUME)

        self._str_performance_watch_list_average_volume_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_AVERAGE_VOLUME)

        self._int_performance_watch_list_average_volume_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_AVERAGE_VOLUME)

        self._str_performance_watch_list_relative_volume_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_RELATIVE_VOLUME)

        self._int_performance_watch_list_relative_volume_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_RELATIVE_VOLUME)

        self._str_performance_watch_list_beta_column_name = (
            self.get_column_name_from_dict(
                myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_BETA))

        self._int_performance_watch_list_beta_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_BETA)

        self._str_performance_watch_list_average_daily_volume_10_day_column_name = (
            self.get_column_name_from_dict(
                myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_AVERAGE_DAILY_VOLUME_10_DAY))

        self._int_performance_watch_list_average_daily_volume_10_day_column_index = (
            self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_AVERAGE_DAILY_VOLUME_10_DAY))

        self._str_performance_watch_list_relative_volume_10_day_column_name = (
            self.get_column_name_from_dict(
                myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_RELATIVE_VOLUME_10_DAY))

        self._int_performance_watch_list_relative_volume_10_day_column_index = (
            self.get_column_index_from_list(
                myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_RELATIVE_VOLUME_10_DAY))

        self._str_performance_watch_list_fifty_two_week_low_column_name = self.get_column_name_from_dict(
                myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_LOW)

        self._int_performance_watch_list_fifty_two_week_low_column_index = self.get_column_index_from_list(
                myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_LOW)

        self._str_performance_watch_list_fifty_two_week_low_momentum_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_LOW_MOMENTUM)

        self._int_performance_watch_list_fifty_two_week_low_momentum_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_LOW_MOMENTUM)

        self._str_performance_watch_list_fifty_two_week_high_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_HIGH)

        self._int_performance_watch_list_fifty_two_week_high_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_HIGH)

        self._int_performance_watch_list_fifty_two_week_high_momentum_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_HIGH_MOMENTUM)

        self._str_performance_watch_list_fifty_two_week_high_momentum_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_HIGH_MOMENTUM)

        self._str_performance_watch_list_fifty_day_average_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_DAY_AVERAGE)

        self._int_performance_watch_list_fifty_day_average_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_DAY_AVERAGE)

        self._str_performance_watch_list_fifty_day_momentum_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_DAY_MOMENTUM)

        self._int_performance_watch_list_fifty_day_momentum_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_DAY_MOMENTUM)

        self._str_performance_watch_list_two_hundred_day_average_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_TWO_HUNDRED_DAY_AVERAGE)

        self._int_performance_watch_list_two_hundred_day_average_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_TWO_HUNDRED_DAY_AVERAGE)

        self._str_performance_watch_list_two_hundred_day_momentum_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_TWO_HUNDRED_DAY_MOMENTUM)

        self._int_performance_watch_list_two_hundred_day_momentum_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_TWO_HUNDRED_DAY_MOMENTUM)

    def _helper_sql_data_base_insert_entire_row_string(self) -> None:

        string_column_names: str = ', '.join(list(self._dict_table_columns.values()))
        # built string question mark

        str_question_mark = '?'

        list_question_marks = []

        for num in range(self._int_table_columns_number):
            list_question_marks.append(str_question_mark)

        str_question_marks = ', '.join(list_question_marks)

        # built SQL command
        self._str_insert_string = (f'INSERT OR IGNORE INTO {self._str_sql_schema}.{self._str_table_name} '
                                  f'({string_column_names}) VALUES ({str_question_marks})')

    def _init_source_table(self) -> None:

        self._str_source_table_name = myStaticWatchListDefinitions.STR_DATA_BASE_TABLE_NAME

        self._str_source_quote_isin_column_name = (
            myStaticWatchListDefinitions.TUPLE_STATIC_WATCH_LIST_QUOTE_ISIN[
                self._index_tuple.DATA_CONTENT][0])

        self._str_source_quote_sector_column_name = (
            myStaticWatchListDefinitions.TUPLE_STATIC_WATCH_LIST_QUOTE_SECTOR[
                self._index_tuple.DATA_CONTENT][0])

        self._str_source_quote_industry_column_name = (
            myStaticWatchListDefinitions.TUPLE_STATIC_WATCH_LIST_QUOTE_INDUSTRY[
                self._index_tuple.DATA_CONTENT][0])

    def _get_available_performance_watch_list_tables(self) -> None:

        self._list_performance_watch_list_tables = self.get_sql_set_of_tables(
            myPerformanceWatchListDefinitions.STR_DATA_BASE_TABLE_NAME)

    def _set_sql_table_performance_watch_list_entire_row(self) -> None:
        if self._list_entire_row is not None:

            if self._list_entire_row.__len__() == self._int_table_columns_number:

                for ind, elem in enumerate(self._list_entire_row):

                    if elem is None:
                        self._list_entire_row[ind] = ''

                # check PRIMARY KEY
                if self._list_entire_row[myPerformanceWatchListDefinitions.INDEX_PRIMARY_KEY] != '':

                    self.set_table_entire_row(self._str_insert_string, tuple(self._list_entire_row))

                else:

                    print(f'---- Operational Error in {__title__}, {self.set_table_entire_row.__name__},'
                          f' the primary key is not set!')
            else:

                print(f'---- Operational Error in {__title__}, '
                      f'{self._set_sql_table_performance_watch_list_entire_row.__name__},'
                      f' the list_entire_row {self._list_entire_row} does not fit the number of columns requirement!')

    def _built_list_entire_row(self) -> None:

        self._list_entire_row = [self._str_performance_watch_list_quote_isin_value,
                                 self._float_performance_watch_list_ask_value,
                                 self._int_performance_watch_list_ask_size_value,
                                 self._float_performance_watch_list_bid_value,
                                 self._int_performance_watch_list_bid_size_value,
                                 self._float_performance_watch_list_current_price_value,
                                 self._float_performance_watch_list_day_high_value,
                                 self._float_performance_watch_list_interday_momentum_value,
                                 self._float_performance_watch_list_day_low_value,
                                 self._float_performance_watch_list_relative_daily_span_value,
                                 self._float_performance_watch_list_open_value,
                                 self._float_performance_watch_list_previous_close_value,
                                 self._float_performance_watch_list_regular_market_change_percent_value,
                                 self._float_performance_watch_list_intraday_momentum_value,
                                 self._int_performance_watch_list_volume_value,
                                 self._int_performance_watch_list_average_volume_value,
                                 self._float_performance_watch_list_relative_volume_value,
                                 self._int_performance_watch_list_average_daily_volume_10_day_value,
                                 self._float_performance_watch_list_relative_volume_10_day_value,
                                 self._float_performance_watch_list_beta_value,
                                 self._float_performance_watch_list_fifty_two_week_low_column_value,
                                 self._float_performance_watch_list_fifty_two_week_low_momentum_column_value,
                                 self._float_performance_watch_list_fifty_two_week_high_column_value,
                                 self._float_performance_watch_list_fifty_two_week_high_momentum_column_value,
                                 self._float_performance_watch_list_fifty_day_average_column_value,
                                 self._float_performance_watch_list_fifty_day_momentum_column_value,
                                 self._float_performance_watch_list_two_hundred_day_average_column_value,
                                 self._float_performance_watch_list_two_hundred_day_momentum_column_value,
                                 ]

    def _get_sql_table_performance_watch_list_quote_per_isin(self, str_isin: str) -> bool:

        if self._bool_sql_data_base_table:

            str_text = (f'SELECT * FROM {self._str_sql_schema}.{self._str_table_name} '

                        f'WHERE {self._str_performance_watch_list_quote_isin_column_name} = "{str_isin}"')

            bool_result = False

            if self._my_sql_connection and self._my_sql_cursor:

                try:

                    self._my_sql_cursor.execute(str_text)

                    tuple_result = self._my_sql_cursor.fetchone()

                    if tuple_result is not None:

                        bool_result = True

                        self._float_performance_watch_list_ask_value = tuple_result[
                            self._int_performance_watch_list_ask_column_index]

                        self._int_performance_watch_list_ask_size_value = tuple_result[
                            self._int_performance_watch_list_ask_size_column_index]

                        self._float_performance_watch_list_bid_value = tuple_result[
                            self._int_performance_watch_list_bid_column_index]

                        self._int_performance_watch_list_bid_size_value = tuple_result[
                            self._int_performance_watch_list_bid_size_column_index]

                        self._float_performance_watch_list_current_price_value = tuple_result[
                            self._int_performance_watch_list_current_price_column_index]

                        self._float_performance_watch_list_day_high_value = tuple_result[
                            self._int_performance_watch_list_day_high_column_index]

                        self._float_performance_watch_list_interday_momentum_value = tuple_result[
                            self._int_performance_watch_list_interday_momentum_column_index]

                        self._float_performance_watch_list_day_low_value = tuple_result[
                            self._int_performance_watch_list_day_low_column_index]

                        self._float_performance_watch_list_relative_daily_span_value = tuple_result[
                            self._int_performance_watch_list_relative_daily_span_column_index]

                        self._float_performance_watch_list_open_value = tuple_result[
                            self._int_performance_watch_list_open_column_index]

                        self._float_performance_watch_list_previous_close_value = tuple_result[
                            self._int_performance_watch_list_previous_close_column_index]

                        self._float_performance_watch_list_regular_market_change_percent_value = tuple_result[
                            self._int_performance_watch_list_relative_volume_10_day_column_index]

                        self._float_performance_watch_list_intraday_momentum_value = tuple_result[
                            self._int_performance_watch_list_intraday_momentum_column_index]

                        self._int_performance_watch_list_volume_value = tuple_result[
                            self._int_performance_watch_list_volume_column_index]

                        self._int_performance_watch_list_average_volume_value = tuple_result[
                            self._int_performance_watch_list_average_volume_column_index]

                        self._float_performance_watch_list_relative_volume_value = tuple_result[
                            self._int_performance_watch_list_relative_volume_column_index]

                        self._int_performance_watch_list_average_daily_volume_10_day_value = tuple_result[
                            self._int_performance_watch_list_average_daily_volume_10_day_column_index]

                        self._float_performance_watch_list_relative_volume_10_day_value = tuple_result[
                            self._int_performance_watch_list_relative_volume_10_day_column_index]

                        self._float_performance_watch_list_beta_value = tuple_result[
                            self._int_performance_watch_list_beta_column_index]

                        self._float_performance_watch_list_fifty_two_week_low_column_value = tuple_result[
                            self._int_performance_watch_list_fifty_day_average_column_index]

                        self._float_performance_watch_list_fifty_two_week_low_momentum_column_value = tuple_result[
                            self._int_performance_watch_list_fifty_two_week_low_momentum_column_index]

                        self._float_performance_watch_list_fifty_two_week_high_column_value = tuple_result[
                            self._int_performance_watch_list_fifty_two_week_high_column_index]

                        self._float_performance_watch_list_fifty_two_week_high_momentum_column_value = tuple_result[
                            self._int_performance_watch_list_fifty_two_week_high_momentum_column_index]

                        self._float_performance_watch_list_fifty_day_average_column_value = tuple_result[
                            self._int_performance_watch_list_fifty_day_average_column_index]

                        self._float_performance_watch_list_fifty_day_momentum_column_value = tuple_result[
                            self._int_performance_watch_list_fifty_day_momentum_column_index]

                        self._float_performance_watch_list_two_hundred_day_average_column_value = tuple_result[
                            self._int_performance_watch_list_two_hundred_day_average_column_index]

                        self._float_performance_watch_list_two_hundred_day_momentum_column_value = tuple_result[
                            self._int_performance_watch_list_two_hundred_day_momentum_column_index]

                    else:

                        self._float_performance_watch_list_ask_value = ''

                        self._int_performance_watch_list_ask_size_value = ''

                        self._float_performance_watch_list_bid_value = ''

                        self._int_performance_watch_list_bid_size_value = ''

                        self._float_performance_watch_list_current_price_value = ''

                        self._float_performance_watch_list_day_high_value = ''

                        self._float_performance_watch_list_interday_momentum_value = ''

                        self._float_performance_watch_list_day_low_value = ''

                        self._float_performance_watch_list_relative_daily_span_value = ''

                        self._float_performance_watch_list_open_value = ''

                        self._float_performance_watch_list_previous_close_value = ''

                        self._float_performance_watch_list_regular_market_change_percent_value = ''

                        self._float_performance_watch_list_intraday_momentum_value = ''

                        self._int_performance_watch_list_volume_value = ''

                        self._int_performance_watch_list_average_volume_value = ''

                        self._float_performance_watch_list_relative_volume_value = ''

                        self._int_performance_watch_list_average_daily_volume_10_day_value = ''

                        self._float_performance_watch_list_relative_volume_10_day_value = ''

                        self._float_performance_watch_list_beta_value = ''

                        self._float_performance_watch_list_fifty_two_week_low_column_value = ''

                        self._float_performance_watch_list_fifty_two_week_low_momentum_column_value = ''

                        self._float_performance_watch_list_fifty_two_week_high_column_value = ''

                        self._float_performance_watch_list_fifty_two_week_high_momentum_column_value = ''

                        self._float_performance_watch_list_fifty_day_average_column_value = ''

                        self._float_performance_watch_list_fifty_day_momentum_column_value = ''

                        self._float_performance_watch_list_two_hundred_day_average_column_value = ''

                        self._float_performance_watch_list_two_hundred_day_momentum_column_value = ''

                    self._my_sql_connection.commit()

                except sqlite3.OperationalError as err:

                    print(
                        f'---- Operational Error in {__title__}, '
                        f'{self._get_sql_table_performance_watch_list_quote_per_isin.__name__} ----, \n'
                        f'---- the Text {str_text} has caused an Error {err} ! ----')

                    exit(1)

            return bool_result

        else:

            self._float_performance_watch_list_ask_value = ''

            self._int_performance_watch_list_ask_size_value = ''

            self._float_performance_watch_list_bid_value = ''

            self._int_performance_watch_list_bid_size_value = ''

            self._float_performance_watch_list_current_price_value = ''

            self._float_performance_watch_list_day_high_value = ''

            self._float_performance_watch_list_interday_momentum_value = ''

            self._float_performance_watch_list_day_low_value = ''

            self._float_performance_watch_list_relative_daily_span_value = ''

            self._float_performance_watch_list_open_value = ''

            self._float_performance_watch_list_previous_close_value = ''

            self._float_performance_watch_list_regular_market_change_percent_value = ''

            self._float_performance_watch_list_intraday_momentum_value = ''

            self._int_performance_watch_list_volume_value = ''

            self._int_performance_watch_list_average_volume_value = ''

            self._float_performance_watch_list_relative_volume_value = ''

            self._int_performance_watch_list_average_daily_volume_10_day_value = ''

            self._float_performance_watch_list_relative_volume_10_day_value = ''

            self._float_performance_watch_list_beta_value = ''

            self._float_performance_watch_list_fifty_two_week_low_column_value = ''

            self._float_performance_watch_list_fifty_two_week_low_momentum_column_value = ''

            self._float_performance_watch_list_fifty_two_week_high_column_value = ''

            self._float_performance_watch_list_fifty_two_week_high_momentum_column_value = ''

            self._float_performance_watch_list_fifty_day_average_column_value = ''

            self._float_performance_watch_list_fifty_day_momentum_column_value = ''

            self._float_performance_watch_list_two_hundred_day_average_column_value = ''

            self._float_performance_watch_list_two_hundred_day_momentum_column_value = ''

            return False

    @property
    def get_performance_watch_list_quote_isin_column_name(self) -> str:

        return self._str_performance_watch_list_quote_isin_column_name

    @property
    def get_available_performance_watch_list_tables(self) -> list[str]:

        return self._list_performance_watch_list_tables

    def set_flag_scan_watch_list(self, flag_scan_watch_list: bool) -> None:

        self._flag_scan_watch_list = flag_scan_watch_list

    def check_sql_table_performance_watch_list_is_quote_per_isin(self, str_isin: str) -> bool:

        str_text = (f'SELECT * FROM {self._str_sql_schema}.{self._str_table_name} '
                    
                    f'WHERE {self._str_performance_watch_list_quote_isin_column_name} = "{str_isin}"')

        bool_result = False

        if self._my_sql_connection and self._my_sql_cursor:

            try:

                self._my_sql_cursor.execute(str_text)

                tuple_result = self._my_sql_cursor.fetchone()

                if tuple_result is not None:

                    bool_result = True


                self._my_sql_connection.commit()


            except sqlite3.OperationalError as err:

                print(
                    f'---- Operational Error in {__title__}, '
                    f'{self.check_sql_table_performance_watch_list_is_quote_per_isin.__name__} ----, \n'
                    f'---- the Text {str_text} has caused an Error {err} ! ----')

                exit(1)

        return bool_result

    def del_sql_table_performance_watch_list_single_quote(self, str_isin: str) -> None:

        self.delete_sql_data_base_rows(self._str_table_name,
                                       self._str_performance_watch_list_quote_isin_column_name,
                                       str_isin)

    def set_sql_table_performance_watch_list_entire_row(self,
                                dict_performance_watch_list_data: dict[str, str | int | float | None]) -> None:

        self._str_performance_watch_list_quote_isin_value = str(dict_performance_watch_list_data[
                                                                     myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_QUOTE_ISIN[
                                                                         self._index_tuple.OPTION_NAME]])

        self._get_sql_table_performance_watch_list_quote_per_isin(self._str_performance_watch_list_quote_isin_value)

        # ask value
        _float_performance_watch_list_ask_value = dict_performance_watch_list_data[
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_ASK[self._index_tuple.OPTION_NAME]]

        if isinstance(_float_performance_watch_list_ask_value, float):

            self._float_performance_watch_list_ask_value = _float_performance_watch_list_ask_value

        else:

            self._float_performance_watch_list_ask_value = ''

        # ask size value
        _int_performance_watch_list_ask_size_value = dict_performance_watch_list_data[
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_ASK_SIZE[self._index_tuple.OPTION_NAME]]

        if isinstance(_int_performance_watch_list_ask_size_value, int):

            self._int_performance_watch_list_ask_size_value = _int_performance_watch_list_ask_size_value

        else:

            self._int_performance_watch_list_ask_size_value = ''

        # bid value
        _float_performance_watch_list_bid_value = dict_performance_watch_list_data[
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_BID[self._index_tuple.OPTION_NAME]]

        if isinstance(_float_performance_watch_list_bid_value, float):

            self._float_performance_watch_list_bid_value = _float_performance_watch_list_bid_value

        else:

            self._float_performance_watch_list_bid_value = ''

        # bid size
        _int_performance_watch_list_bid_size_value = dict_performance_watch_list_data[
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_BID_SIZE[self._index_tuple.OPTION_NAME]]

        if isinstance(_int_performance_watch_list_bid_size_value, int):

            self._int_performance_watch_list_bid_size_value = _int_performance_watch_list_bid_size_value

        else:

            self._int_performance_watch_list_bid_size_value = ''

        # current price
        _float_performance_watch_list_current_price_value = dict_performance_watch_list_data[
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_CURRENT_PRICE[self._index_tuple.OPTION_NAME]]

        if isinstance(_float_performance_watch_list_current_price_value, float):

            self._float_performance_watch_list_current_price_value = _float_performance_watch_list_current_price_value

        else:

            self._float_performance_watch_list_current_price_value = ''

        # day high
        _float_performance_watch_list_day_high_value = dict_performance_watch_list_data[
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_DAY_HIGH[self._index_tuple.OPTION_NAME]]

        if isinstance(_float_performance_watch_list_day_high_value, float):

            self._float_performance_watch_list_day_high_value = _float_performance_watch_list_day_high_value

        else:

            self._float_performance_watch_list_day_high_value = ''

        # interday momentum
        _float_performance_watch_list_interday_momentum_value = dict_performance_watch_list_data[
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_INTERDAY_MOMENTUM[self._index_tuple.OPTION_NAME]]

        if isinstance(_float_performance_watch_list_interday_momentum_value, float):

            self._float_performance_watch_list_interday_momentum_value = _float_performance_watch_list_interday_momentum_value

        else:

            self._float_performance_watch_list_interday_momentum_value = ''

        # day low
        _float_performance_watch_list_day_low_value = dict_performance_watch_list_data[
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_DAY_LOW[self._index_tuple.OPTION_NAME]]

        if isinstance(_float_performance_watch_list_day_low_value, float):

            self._float_performance_watch_list_day_low_value = _float_performance_watch_list_day_low_value

        else:

            self._float_performance_watch_list_day_low_value = ''

        # relative daily span
        _float_performance_watch_list_relative_daily_span_value = dict_performance_watch_list_data[
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_RELATIVE_DAILY_SPAN[self._index_tuple.OPTION_NAME]]

        if isinstance(_float_performance_watch_list_relative_daily_span_value, float):

            self._float_performance_watch_list_relative_daily_span_value = _float_performance_watch_list_relative_daily_span_value

        else:

            self._float_performance_watch_list_relative_daily_span_value = ''

        # open
        _float_performance_watch_list_open_value = dict_performance_watch_list_data[
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_OPEN[self._index_tuple.OPTION_NAME]]

        if isinstance(_float_performance_watch_list_open_value, float):

            self._float_performance_watch_list_open_value = _float_performance_watch_list_open_value

        else:

            self._float_performance_watch_list_open_value = ''

        # previous close
        _float_performance_watch_list_previous_close_value = dict_performance_watch_list_data[
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_PREVIOUS_CLOSE[self._index_tuple.OPTION_NAME]]

        if isinstance(_float_performance_watch_list_previous_close_value, float):

            self._float_performance_watch_list_previous_close_value = _float_performance_watch_list_previous_close_value

        else:

            self._float_performance_watch_list_previous_close_value = ''

        # regular market change percent
        _float_performance_watch_list_regular_market_change_percent_value = dict_performance_watch_list_data[
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_REGULAR_MARKET_CHANGE_PERCENT[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_float_performance_watch_list_regular_market_change_percent_value, float):

            self._float_performance_watch_list_regular_market_change_percent_value = _float_performance_watch_list_regular_market_change_percent_value

        else:

            self._float_performance_watch_list_regular_market_change_percent_value = ''

        # intraday momentum
        _float_performance_watch_list_intraday_momentum_value = dict_performance_watch_list_data[
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_INTRADAY_MOMENTUM[self._index_tuple.OPTION_NAME]]

        if isinstance(_float_performance_watch_list_intraday_momentum_value, float):

            self._float_performance_watch_list_intraday_momentum_value = _float_performance_watch_list_intraday_momentum_value

        else:

            self._float_performance_watch_list_intraday_momentum_value = ''

        # volume
        _int_performance_watch_list_volume_value = dict_performance_watch_list_data[
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_VOLUME[self._index_tuple.OPTION_NAME]]

        if isinstance(_int_performance_watch_list_volume_value, int):

            self._int_performance_watch_list_volume_value = _int_performance_watch_list_volume_value

        else:

            self._int_performance_watch_list_volume_value = ''

        # average volume
        _int_performance_watch_list_average_volume_value = dict_performance_watch_list_data[
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_AVERAGE_VOLUME[self._index_tuple.OPTION_NAME]]

        if isinstance(_int_performance_watch_list_average_volume_value, int):

            self._int_performance_watch_list_average_volume_value = _int_performance_watch_list_average_volume_value

        else:

            self._int_performance_watch_list_average_volume_value = ''

        # relative volume
        _float_performance_watch_list_relative_volume_value = dict_performance_watch_list_data[
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_RELATIVE_VOLUME[self._index_tuple.OPTION_NAME]]

        if isinstance(_float_performance_watch_list_relative_volume_value, float):

            self._float_performance_watch_list_relative_volume_value = _float_performance_watch_list_relative_volume_value

        else:

            self._float_performance_watch_list_relative_volume_value = ''

        # average daily volume 10 day
        _int_performance_watch_list_average_daily_volume_10_day_value = dict_performance_watch_list_data[
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_AVERAGE_DAILY_VOLUME_10_DAY[self._index_tuple.OPTION_NAME]]

        if isinstance(_int_performance_watch_list_average_daily_volume_10_day_value, int):

            self._int_performance_watch_list_average_daily_volume_10_day_value = _int_performance_watch_list_average_daily_volume_10_day_value

        else:

            self._int_performance_watch_list_average_daily_volume_10_day_value = ''

        # relative volume 10 day
        _float_performance_watch_list_relative_volume_10_day_value = dict_performance_watch_list_data[
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_RELATIVE_VOLUME_10_DAY[self._index_tuple.OPTION_NAME]]

        if isinstance(_float_performance_watch_list_relative_volume_10_day_value, float):

            self._float_performance_watch_list_relative_volume_10_day_value = _float_performance_watch_list_relative_volume_10_day_value

        else:

            self._float_performance_watch_list_relative_volume_10_day_value = ''

        # beta
        _float_performance_watch_list_beta_value = dict_performance_watch_list_data[
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_BETA[self._index_tuple.OPTION_NAME]]

        if isinstance(_float_performance_watch_list_beta_value, float):

            self._float_performance_watch_list_beta_value = _float_performance_watch_list_beta_value

        else:

            self._float_performance_watch_list_beta_value = ''

        # fifty two weeks low
        _float_performance_watch_list_fifty_two_week_low_column_value = dict_performance_watch_list_data[
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_LOW[self._index_tuple.OPTION_NAME]]

        if isinstance(_float_performance_watch_list_fifty_two_week_low_column_value, float):

            self._float_performance_watch_list_fifty_two_week_low_column_value = _float_performance_watch_list_fifty_two_week_low_column_value

        else:

            self._float_performance_watch_list_fifty_two_week_low_column_value = ''

        # fifty two weeks low momentum
        _float_performance_watch_list_fifty_two_week_low_momentum_column_value = dict_performance_watch_list_data[
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_LOW_MOMENTUM[self._index_tuple.OPTION_NAME]]

        if isinstance(_float_performance_watch_list_fifty_two_week_low_momentum_column_value, float):

            self._float_performance_watch_list_fifty_two_week_low_momentum_column_value = _float_performance_watch_list_fifty_two_week_low_momentum_column_value

        else:

            self._float_performance_watch_list_fifty_two_week_low_momentum_column_value = ''

        # fifty two weeks high
        _float_performance_watch_list_fifty_two_week_high_column_value = dict_performance_watch_list_data[
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_HIGH[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_float_performance_watch_list_fifty_two_week_high_column_value, float):

            self._float_performance_watch_list_fifty_two_week_high_column_value = _float_performance_watch_list_fifty_two_week_high_column_value

        else:

            self._float_performance_watch_list_fifty_two_week_high_column_value = ''

        # fifty two weeks high momentum
        _float_performance_watch_list_fifty_two_week_high_momentum_column_value = dict_performance_watch_list_data[
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_HIGH_MOMENTUM[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_float_performance_watch_list_fifty_two_week_high_momentum_column_value, float):

            self._float_performance_watch_list_fifty_two_week_high_momentum_column_value = _float_performance_watch_list_fifty_two_week_high_momentum_column_value

        else:

            self._float_performance_watch_list_fifty_two_week_high_momentum_column_value = ''

        # fifty day average
        _float_performance_watch_list_fifty_day_average_column_value = dict_performance_watch_list_data[
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_DAY_AVERAGE[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_float_performance_watch_list_fifty_day_average_column_value, float):

            self._float_performance_watch_list_fifty_day_average_column_value = _float_performance_watch_list_fifty_day_average_column_value

        else:

            self._float_performance_watch_list_fifty_day_average_column_value = ''

        # fifty day momentum
        _float_performance_watch_list_fifty_day_momentum_column_value = dict_performance_watch_list_data[
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_DAY_MOMENTUM[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_float_performance_watch_list_fifty_day_momentum_column_value, float):

            self._float_performance_watch_list_fifty_day_momentum_column_value = _float_performance_watch_list_fifty_day_momentum_column_value

        else:

            self._float_performance_watch_list_fifty_day_momentum_column_value = ''

        # two hundred day average
        _float_performance_watch_list_two_hundred_day_average_column_value = dict_performance_watch_list_data[
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_TWO_HUNDRED_DAY_AVERAGE[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_float_performance_watch_list_two_hundred_day_average_column_value, float):

            self._float_performance_watch_list_two_hundred_day_average_column_value = _float_performance_watch_list_two_hundred_day_average_column_value

        else:

            self._float_performance_watch_list_two_hundred_day_average_column_value = ''

        # two hundred day momentum
        _float_performance_watch_list_two_hundred_day_momentum_column_value = dict_performance_watch_list_data[
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_TWO_HUNDRED_DAY_MOMENTUM[
                self._index_tuple.OPTION_NAME]]

        if isinstance(_float_performance_watch_list_two_hundred_day_momentum_column_value, float):

            self._float_performance_watch_list_two_hundred_day_momentum_column_value = _float_performance_watch_list_two_hundred_day_momentum_column_value

        else:

            self._float_performance_watch_list_two_hundred_day_momentum_column_value = ''

        self._built_list_entire_row()

        self._set_sql_table_performance_watch_list_entire_row()

    def get_global_average_change_percent(self, str_table_name: str) -> float:

        _str_change_percent_col = self._str_performance_watch_list_regular_market_change_percent_column_name

        _str_table_name = str_table_name

        _str_text = (f'SELECT '
                     f' ROUND(AVG({_str_change_percent_col}), 2) '
                     f' FROM {_str_table_name} '
                     f' WHERE {_str_change_percent_col} <> 0 ')

        try:

            self._my_sql_cursor.execute(_str_text)

            list_result = self._my_sql_cursor.fetchall()

            self._my_sql_connection.commit()

        except sqlite3.OperationalError as err:

            print(f'---- Operational Error in {__title__}, {self.get_global_average_change_percent.__name__} ----, \n'
                  f'---- the Text {_str_text} has caused an Error {err} ! ----')

            exit(1)

        if list_result.__len__() > 0:

            return list_result[0][0]

        else:

            return 0

    def get_segment_category_average_change_percent(self, str_table_name: str, str_category_name: str) -> float:

        _str_change_percent_col = self._str_performance_watch_list_regular_market_change_percent_column_name

        _str_table_name = str_table_name

        _str_target_reference_column = self._str_performance_watch_list_quote_isin_column_name

        _str_table_name_source = self._str_source_table_name

        _str_source_reference_column = self._str_source_quote_isin_column_name

        _str_source_category_column = self._str_source_quote_sector_column_name

        _str_source_category_name = str_category_name

        _str_text = (f'SELECT '
                     f' ROUND(AVG({_str_change_percent_col}), 2) '
                     f' FROM {_str_table_name} AS t '
                     f' INNER JOIN {_str_table_name_source} AS s ON t.{_str_target_reference_column} = s.{_str_source_reference_column} '
                     f' WHERE s.{_str_source_category_column} = "{_str_source_category_name}" '
                     f'   AND t.{_str_change_percent_col} <> 0 ')

        try:

            self._my_sql_cursor.execute(_str_text)

            list_result = self._my_sql_cursor.fetchall()

            self._my_sql_connection.commit()

        except sqlite3.OperationalError as err:

            print(f'---- Operational Error in {__title__}, {self.get_segment_category_average_change_percent.__name__} ----, \n'
                  f'---- the Text {_str_text} has caused an Error {err} ! ----')

            exit(1)

        if list_result.__len__() > 0:

            return list_result[0][0]

        else:

            return 0

    def get_industry_category_average_change_percent(self, str_table_name: str, str_category_name: str) -> float:

        _str_change_percent_col = self._str_performance_watch_list_regular_market_change_percent_column_name

        _str_table_name = str_table_name

        _str_target_reference_column = self._str_performance_watch_list_quote_isin_column_name

        _str_table_name_source = self._str_source_table_name

        _str_source_reference_column = self._str_source_quote_isin_column_name

        _str_source_category_column = self._str_source_quote_industry_column_name

        _str_source_category_name = str_category_name

        _str_text = (f'SELECT '
                     f' ROUND(AVG({_str_change_percent_col}), 2) '
                     f' FROM {_str_table_name} AS t '
                     f' INNER JOIN {_str_table_name_source} AS s ON t.{_str_target_reference_column} = s.{_str_source_reference_column} '
                     f' WHERE s.{_str_source_category_column} = "{_str_source_category_name}" '
                     f'   AND t.{_str_change_percent_col} <> 0 ')

        try:

            self._my_sql_cursor.execute(_str_text)

            list_result = self._my_sql_cursor.fetchall()

            self._my_sql_connection.commit()

        except sqlite3.OperationalError as err:

            print(f'---- Operational Error in {__title__}, {self.get_industry_category_average_change_percent.__name__} ----, \n'
                  f'---- the Text {_str_text} has caused an Error {err} ! ----')

            exit(1)

        if list_result.__len__() > 0:

            return list_result[0][0]

        else:

            return 0

    def get_performance_watch_list_date_per_quote_isin(self, str_quote_isin: str) -> dict:

        _data = {}

        self._get_sql_table_performance_watch_list_quote_per_isin(str_quote_isin)

        self._str_performance_watch_list_quote_isin_value  = str_quote_isin

        _data[self._str_performance_watch_list_quote_isin_column_name] = self._str_performance_watch_list_quote_isin_value
        _data[self._str_performance_watch_list_ask_column_name] = self._float_performance_watch_list_ask_value
        _data[self._str_performance_watch_list_ask_size_column_name] = self._int_performance_watch_list_ask_size_value
        _data[self._str_performance_watch_list_bid_column_name] = self._float_performance_watch_list_bid_value
        _data[self._str_performance_watch_list_bid_size_column_name] = self._int_performance_watch_list_bid_size_value
        _data[self._str_performance_watch_list_current_price_column_name] = self._float_performance_watch_list_current_price_value
        _data[self._str_performance_watch_list_day_high_column_name] = self._float_performance_watch_list_day_high_value
        _data[self._str_performance_watch_list_interday_momentum_column_name] = self._float_performance_watch_list_interday_momentum_value
        _data[self._str_performance_watch_list_day_low_column_name] = self._float_performance_watch_list_day_low_value
        _data[self._str_performance_watch_list_relative_daily_span_column_name] = self._float_performance_watch_list_relative_daily_span_value
        _data[self._str_performance_watch_list_open_column_name] = self._float_performance_watch_list_open_value
        _data[self._str_performance_watch_list_previous_close_column_name] = self._float_performance_watch_list_previous_close_value
        _data[self._str_performance_watch_list_regular_market_change_percent_column_name] = self._float_performance_watch_list_regular_market_change_percent_value
        _data[self._str_performance_watch_list_intraday_momentum_column_name] = self._float_performance_watch_list_intraday_momentum_value
        _data[self._str_performance_watch_list_volume_column_name] = self._int_performance_watch_list_volume_value
        _data[self._str_performance_watch_list_average_volume_column_name] = self._int_performance_watch_list_average_volume_value
        _data[self._str_performance_watch_list_relative_volume_column_name] = self._float_performance_watch_list_relative_volume_value
        _data[self._str_performance_watch_list_average_daily_volume_10_day_column_name] = self._int_performance_watch_list_average_daily_volume_10_day_value
        _data[self._str_performance_watch_list_relative_volume_10_day_column_name] = self._float_performance_watch_list_relative_volume_10_day_value
        _data[self._str_performance_watch_list_beta_column_name] = self._float_performance_watch_list_beta_value
        _data[self._str_performance_watch_list_fifty_two_week_low_column_name] = self._float_performance_watch_list_fifty_two_week_low_column_value
        _data[self._str_performance_watch_list_fifty_two_week_low_momentum_column_name] = self._float_performance_watch_list_fifty_two_week_low_momentum_column_value
        _data[self._str_performance_watch_list_fifty_two_week_high_column_name] = self._float_performance_watch_list_fifty_two_week_high_column_value
        _data[self._str_performance_watch_list_fifty_two_week_high_momentum_column_name] = self._float_performance_watch_list_fifty_two_week_high_momentum_column_value
        _data[self._str_performance_watch_list_fifty_day_average_column_name] = self._float_performance_watch_list_fifty_day_average_column_value
        _data[self._str_performance_watch_list_fifty_day_momentum_column_name] = self._float_performance_watch_list_fifty_day_momentum_column_value
        _data[self._str_performance_watch_list_two_hundred_day_average_column_name] = self._float_performance_watch_list_two_hundred_day_average_column_value
        _data[self._str_performance_watch_list_two_hundred_day_momentum_column_name] = self._float_performance_watch_list_two_hundred_day_momentum_column_value

        return _data


if __name__ == "__main__":
    mySQLDB = mySQLDataBase.MySQLDataBase()
