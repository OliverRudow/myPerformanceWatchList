"""myPerformanceWatchList.py."""

__title__: str = "myPerformanceWatchList"
__version__: str = "0.1.1"
__author__: str = "Oliver Rudow"
__email__: str = "oliver.rudow@googlemail.com"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import dataclasses
import statistics
from typing import Optional
from mytuple import myTuple
from mydatabase import mySQLDataBase
from myfilebase import myFileBase
from mysharesdefinition import myPerformanceWatchListDefinitions
from myperformancewatchlist import myTableSQLPerformanceWatchList, myTableSQLPerformanceCreditWatchList
from myyfinance import myYFinance


def calculate_change_percent_score(performance_value, avg_value, std_dev_value) -> int:

    if performance_value is None:

        return 0

    elif performance_value > avg_value + 2 * std_dev_value:

        # out-performer
        return 5

    elif performance_value > avg_value + 1 * std_dev_value:

        # high-performer
        return 3

    elif performance_value > avg_value:

        # performer
        return 1

    elif performance_value > avg_value - 1 * std_dev_value:

        # low performer
        return -1

    elif performance_value > avg_value - 2 * std_dev_value:

        # under-performer
        return -3

    else:

        return -5


@dataclasses.dataclass(init=False)
class MyPerformanceWatchList(mySQLDataBase.MySQLDataBase):
    """
        myPerformanceWatchList is a Python class that holds the SQLite table of a static watch list comprising the table columns
            - quote_isin,
            - ask,
            - ask_size,
            - bid,
            - bid_size,
            - current_price
            - day_high,
            - interday_momentum,
            - day_low,
            - relative_daily_span,
            - open,
            - previous_close,
            - regular_market_change_percent,
            - intraday_momentum,
            - volume,
            - average_volume,
            - relative_volume,
            - average_daily_volume_10_day,
            - relative_volume_10_day,
            - beta,
            - fifty_two_week_low,
            - fifty_two_week_low_momentum,
            - fifty_two_week_high,
            - fifty_two_week_high_momentum,
            - fifty_day_average,
            - fifty_day_momentum,
            - two_hundred_day_average,
            - two hundred_day_momentum

        myPerformanceWatchList is working in two different modi, i.e.
            - read only modus with myYFinance.MyYFinance = None
            - write modus with myYFinance being active.
    """
    # Tuple Definition
    _index_tuple: myTuple.MyTuple = dataclasses.field(repr=False, default_factory=type(myTuple.MyTuple))

    # FileBase
    _my_file: myFileBase.MyFileBase = dataclasses.field(repr=False, default_factory=type(myFileBase.MyFileBase))

    # YFinance
    _my_y_finance: myYFinance.MyYFinance | None = dataclasses.field(repr=False, default_factory=type(myYFinance.MyYFinance))

    # SQL Table Static Watch List
    _my_table_sql_performance_watch_list: myTableSQLPerformanceWatchList.MyTableSQLPerformanceWatchList = (
        dataclasses.field(repr=False, default_factory=type(myTableSQLPerformanceWatchList.MyTableSQLPerformanceWatchList)))

    # SQL Table Performance Credit Watch List
    _my_table_sql_performance_credit_watch_list: myTableSQLPerformanceCreditWatchList.MyTableSQLPerformanceCreditWatchList = (
        dataclasses.field(repr=False, default_factory=type( myTableSQLPerformanceCreditWatchList.MyTableSQLPerformanceCreditWatchList)))

    # flag_scan_watch_list
    _flag_scan_watch_list: bool = dataclasses.field(repr=False, default=True)

    # tuple indices
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
    _int_performance_watch_list_regular_market_change_percent_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_intraday_momentum_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_volume_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_average_volume_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_relative_volume_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_average_daily_volume_10_day_column_index: int = (
        dataclasses.field(repr=False, default=0))
    _int_performance_watch_list_relative_volume_10_day_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_beta_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_fifty_two_week_low_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_fifty_two_week_high_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_fifty_two_week_high_momentum_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_fifty_day_average_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_fifty_day_momentum_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_two_hundred_day_average_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_two_hundred_day_momentum_column_index: int = dataclasses.field(repr=False, default=0)

    # table data as list of dict from SQL Data Base
    _list_table_data: list = dataclasses.field(repr=False, default_factory=list)

    _int_actual_quote_index: int = dataclasses.field(repr=False, default=0)

    _int_max_quote_index: int = dataclasses.field(repr=False, default=0)

    _str_actual_quote_isin: str = dataclasses.field(repr=False, default='')

    _list_column_names: list = dataclasses.field(repr=False, default_factory=list)

    _int_num_columns: int = dataclasses.field(repr=False, default=0)

    _list_performance_watch_list_tables: list[str] = dataclasses.field(repr=False, default=list[str])

    _float_average_change_percent: float = dataclasses.field(repr=False, default=0)

    _float_std_dev_change_percent: float = dataclasses.field(repr=False, default=0)

    _list_sectors: list = dataclasses.field(repr=False, default_factory=list)

    _list_industries: list = dataclasses.field(repr=False, default_factory=list)

    _list_sectors_change_percent_table: list = dataclasses.field(repr=False, default_factory=list)

    _list_industries_change_percent_table: list = dataclasses.field(repr=False, default_factory=list)

    _list_sectors_change_percent_score_table: list = dataclasses.field(repr=False, default_factory=list)

    def __init__(self, y_finance: Optional[myYFinance.MyYFinance] = None,
                 str_working_directory: Optional[str] = None,
                 str_data_base_filename: Optional[str] = None,
                 flag_scan_watch_list: Optional[bool] = None)-> None:
        super().__init__()

        # init myTuple
        self._index_tuple = myTuple.MyTuple

        # init FileBase w/o Config
        self._my_file = myFileBase.MyFileBase()

        # init scan modus
        if flag_scan_watch_list is not None:

            self._flag_scan_watch_list = flag_scan_watch_list

        else:

            self._flag_scan_watch_list = True

        # init y_finance
        if y_finance is not None:

            # write modus
            self._my_y_finance = y_finance

        else:

            # read only modus
            self._my_y_finance = None

            # in read only mode the scan flag shall almost be Dalse
            self._flag_scan_watch_list = False

        # init working directory for Data Base
        if str_working_directory is not None:

            self._my_file.set_directory(str_working_directory)

        else:

            self._my_file.set_directory(myPerformanceWatchListDefinitions.STR_DATA_BASE_DIR_NAME)

        # init data base filename
        if str_data_base_filename is not None:

            self._my_file.set_file_name(str_data_base_filename)

        else:

            self._my_file.set_file_name(myPerformanceWatchListDefinitions.STR_DATA_BASE_FILE_NAME)

        self._list_column_names = []

        # SQL Data Base Name
        self.set_sql_data_base_name(self._my_file.get_entire_file_name)

        # SQL Data Base Connection Settings
        self.set_sql_connection_timeout(myPerformanceWatchListDefinitions.DATA_BASE_TIMEOUT)

        self.set_sql_connection_uri(myPerformanceWatchListDefinitions.DATA_BASE_CONNECTION_URI)

        # Open SQL DataBase
        self.open_sql_data_base()

        self. _my_table_sql_performance_watch_list = myTableSQLPerformanceWatchList.MyTableSQLPerformanceWatchList(
            self._my_sql_connection,
            self._my_sql_cursor,
            self._flag_scan_watch_list)

        self._my_table_sql_performance_credit_watch_list = myTableSQLPerformanceCreditWatchList.MyTableSQLPerformanceCreditWatchList(
            self._my_sql_connection,
            self._my_sql_cursor)

        self._list_column_names = self. _my_table_sql_performance_watch_list.get_column_names()

        if self._list_column_names.__len__() == 0:

            self._list_column_names = myPerformanceWatchListDefinitions.LIST_PERFORMANCE_WATCH_LIST_COLUMN_NAMES

        elif self._list_column_names.__len__() < len(
                myPerformanceWatchListDefinitions.LIST_PERFORMANCE_WATCH_LIST_COLUMN_NAMES):

            self._list_column_names = myPerformanceWatchListDefinitions.LIST_PERFORMANCE_WATCH_LIST_COLUMN_NAMES

        self._int_num_columns = self._list_column_names.__len__()

        self._init_watch_list_column_indices()

        self._get_available_performance_watch_list_tables()

        self._list_sectors = []

        self._list_industries = []

        self._list_sectors_change_percent_table = []

        self._list_industries_change_percent_table = []

        self._list_sectors_change_percent_score_table = []

    def _get_table_data(self) -> None:

        self._list_table_data = self._my_table_sql_performance_watch_list.get_table_all_data_as_list_of_dicts()

        self._int_max_quote_index = self._list_table_data.__len__()

    def _transfer_latest_table_name(self) -> None:

        _str_latest_table_name = self._my_table_sql_performance_watch_list.get_table_name

        if _str_latest_table_name not in self._list_performance_watch_list_tables:

            if self._list_performance_watch_list_tables.__len__() > 0:

                _str_latest_table_name = self._list_performance_watch_list_tables[0]

            else:

                _str_latest_table_name = myPerformanceWatchListDefinitions.STR_DATA_BASE_TABLE_NAME

        self._my_table_sql_performance_credit_watch_list.set_source_table_name(_str_latest_table_name)

    def _init_watch_list_column_indices(self) -> None:

        self._int_performance_watch_list_quote_isin_column_index = self._list_column_names.index(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_QUOTE_ISIN[
                self._index_tuple.OPTION_NAME])

        self._int_performance_watch_list_ask_column_index = self._list_column_names.index(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_ASK[
                self._index_tuple.OPTION_NAME])

        self._int_performance_watch_list_ask_size_column_index = self._list_column_names.index(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_ASK_SIZE[
                self._index_tuple.OPTION_NAME])

        self._int_performance_watch_list_bid_column_index = self._list_column_names.index(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_BID[
                self._index_tuple.OPTION_NAME])

        self._int_performance_watch_list_bid_size_column_index = self._list_column_names.index(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_BID_SIZE[
                self._index_tuple.OPTION_NAME])

        self._int_performance_watch_list_current_price_column_index = self._list_column_names.index(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_CURRENT_PRICE[
                self._index_tuple.OPTION_NAME])

        self._int_performance_watch_list_day_high_column_index = self._list_column_names.index(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_DAY_HIGH[
                self._index_tuple.OPTION_NAME])

        self._int_performance_watch_list_interday_momentum_column_index = self._list_column_names.index(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_INTERDAY_MOMENTUM[
                self._index_tuple.OPTION_NAME])

        self._int_performance_watch_list_day_low_column_index = self._list_column_names.index(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_DAY_LOW[
                self._index_tuple.OPTION_NAME])

        self._int_performance_watch_list_relative_daily_span_column_index = self._list_column_names.index(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_RELATIVE_DAILY_SPAN[
                self._index_tuple.OPTION_NAME])

        self._int_performance_watch_list_open_column_index = self._list_column_names.index(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_OPEN[
                self._index_tuple.OPTION_NAME])

        self._int_performance_watch_list_previous_close_column_index = self._list_column_names.index(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_PREVIOUS_CLOSE[
                self._index_tuple.OPTION_NAME])

        self._int_performance_watch_list_regular_market_change_percent_column_index = self._list_column_names.index(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_REGULAR_MARKET_CHANGE_PERCENT[
                self._index_tuple.OPTION_NAME])

        self._int_performance_watch_list_intraday_momentum_column_index = self._list_column_names.index(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_INTRADAY_MOMENTUM[
                self._index_tuple.OPTION_NAME])

        self._int_performance_watch_list_volume_column_index = self._list_column_names.index(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_VOLUME[
                self._index_tuple.OPTION_NAME])

        self._int_performance_watch_list_average_volume_column_index = self._list_column_names.index(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_AVERAGE_VOLUME[
                self._index_tuple.OPTION_NAME])

        self._int_performance_watch_list_relative_volume_column_index = self._list_column_names.index(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_RELATIVE_VOLUME[
                self._index_tuple.OPTION_NAME])

        self._int_performance_watch_list_average_daily_volume_10_day_column_index = self._list_column_names.index(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_AVERAGE_DAILY_VOLUME_10_DAY[
                self._index_tuple.OPTION_NAME])

        self._int_performance_watch_list_relative_volume_10_day_column_index = self._list_column_names.index(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_RELATIVE_VOLUME_10_DAY[
                self._index_tuple.OPTION_NAME])

        self._int_performance_watch_list_beta_column_index = self._list_column_names.index(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_BETA[
                self._index_tuple.OPTION_NAME])

        self._int_performance_watch_list_fifty_two_week_low_column_index = self._list_column_names.index(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_LOW[
                self._index_tuple.OPTION_NAME])

        self._int_performance_watch_list_fifty_two_week_high_column_index = self._list_column_names.index(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_HIGH[
                self._index_tuple.OPTION_NAME])

        self._int_performance_watch_list_fifty_two_week_high_momentum_column_index = self._list_column_names.index(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_HIGH_MOMENTUM[
                self._index_tuple.OPTION_NAME])

        self._int_performance_watch_list_fifty_day_average_column_index = self._list_column_names.index(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_DAY_AVERAGE[
                self._index_tuple.OPTION_NAME])

        self._int_performance_watch_list_fifty_day_momentum_column_index = self._list_column_names.index(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_DAY_MOMENTUM[
                self._index_tuple.OPTION_NAME])

        self._int_performance_watch_list_two_hundred_day_average_column_index = self._list_column_names.index(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_TWO_HUNDRED_DAY_AVERAGE[
                self._index_tuple.OPTION_NAME])

        self._int_performance_watch_list_two_hundred_day_momentum_column_index = self._list_column_names.index(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_TWO_HUNDRED_DAY_MOMENTUM[
                self._index_tuple.OPTION_NAME])

    def _get_available_performance_watch_list_tables(self) -> None:

        self._list_performance_watch_list_tables = self._my_table_sql_performance_watch_list.get_available_performance_watch_list_tables

    def _calculate_sectors_average_change_percent(self):

        _list_sectors_percentage = []

        _list_change_percent = []

        self._float_average_change_percent = 0

        self._float_std_dev_change_percent = 0

        _str_latest_table_name = self._my_table_sql_performance_watch_list.get_table_name

        if _str_latest_table_name not in self._list_performance_watch_list_tables:

            if self._list_performance_watch_list_tables.__len__() > 0:

                _str_latest_table_name = self._list_performance_watch_list_tables[0]

            else:

                _str_latest_table_name = myPerformanceWatchListDefinitions.STR_DATA_BASE_TABLE_NAME

        _list_sectors_percentage.append(('Sector', '# Quotes', '%'))

        _list_helper: list[str | int | float] = ['Total',
                                                 self._my_table_sql_performance_watch_list.get_table_number_rows(
                                                     _str_latest_table_name)]

        self._float_average_change_percent = self._my_table_sql_performance_watch_list.get_global_average_change_percent(
            _str_latest_table_name)

        _list_helper.append(self._float_average_change_percent)

        _list_sectors_percentage.append(tuple(_list_helper))

        if self._list_sectors.__len__() > 0:

            for element in self._list_sectors:

                _str_sector = element[0]

                _list_helper = []

                if not _str_sector == '':
                    _list_helper.append(_str_sector)

                    _list_helper.append(element[1])

                    _float_single_change_percent = self._my_table_sql_performance_watch_list.get_segment_category_average_change_percent(
                        _str_latest_table_name, _str_sector)

                    _list_helper.append(_float_single_change_percent)

                    _list_sectors_percentage.append(tuple(_list_helper))

                    _list_change_percent.append(_float_single_change_percent)

        # remove None
        _list_change_percent = [0 if x is None else x for x in _list_change_percent]

        self._list_sectors_change_percent_table = _list_sectors_percentage

        self._float_std_dev_change_percent = round(statistics.stdev(_list_change_percent), 2)

        # create score table
        self._list_sectors_change_percent_score_table = [(first_tuple, third_tuple) for first_tuple, _, third_tuple in
                                                         _list_sectors_percentage[2:]]

        self._list_sectors_change_percent_score_table = \
            [(sector, calculate_change_percent_score(percentage,
                                                     self._float_average_change_percent,
                                                     self._float_std_dev_change_percent)) for sector, percentage in
             self._list_sectors_change_percent_score_table]

    def _calculate_industries_average_change_percent(self):

        _list_industries_percentage = []

        _str_latest_table_name = self._my_table_sql_performance_watch_list.get_table_name

        if _str_latest_table_name not in self._list_performance_watch_list_tables:

            if self._list_performance_watch_list_tables.__len__() > 0:

                _str_latest_table_name = self._list_performance_watch_list_tables[0]

            else:

                _str_latest_table_name = myPerformanceWatchListDefinitions.STR_DATA_BASE_TABLE_NAME

        if self._list_industries.__len__() > 0:

            for element in self._list_industries:

                _str_industry = element[0]

                _list_helper = []

                if not _str_industry == '':
                    _list_helper.append(_str_industry)

                    _list_helper.append(element[1])

                    _float_single_change_percent = self._my_table_sql_performance_watch_list.get_industry_category_average_change_percent(
                        _str_latest_table_name, _str_industry)

                    _list_helper.append(_float_single_change_percent)

                    _list_industries_percentage.append(tuple(_list_helper))

        _list_industries_percentage = [(t[0], t[1], 0 if t[2] is None else t[2]) for t in _list_industries_percentage]

        _list_industries_percentage = sorted(_list_industries_percentage, key=lambda x: x[2], reverse=True)

        _list_industries_percentage.insert(0, ('Industries', '# Quotes', '%'))

        self._list_industries_change_percent_table = _list_industries_percentage

    def reset_performance_watch_list(self) -> None:

        self._my_table_sql_performance_watch_list.drop_sql_table()

        self._my_table_sql_performance_watch_list.create_sql_data_base_table()

    def set_sectors_list(self, list_sectors_list: list[tuple]) -> None:

        self._list_sectors = list_sectors_list

    def set_industries_list(self, list_industries_list: list[tuple]) -> None:

        self._list_industries = list_industries_list

    def set_sectors_change_percent_score_list(self) -> None:

        self._calculate_sectors_average_change_percent()

        self._my_table_sql_performance_credit_watch_list.set_sectors_change_percent_score_list(self._list_sectors_change_percent_score_table)

    def get_table_data(self) -> list:

        return self._list_table_data

    @property
    def get_available_performance_watch_list_tables(self) -> list[str]:

        return self._list_performance_watch_list_tables

    def get_table_column_names(self) -> list:

        return self._list_column_names

    def set_flag_scan_watch_list(self, flag_scan_watch_list: bool) -> None:

        self._flag_scan_watch_list = flag_scan_watch_list

    def set_actual_quote(self, int_index: int) -> None:

        if self._my_table_sql_performance_watch_list.check_sql_data_base_table_is_not_empty():

            try:

                if int_index > self._int_max_quote_index:

                    raise ValueError(f'----- Value Error in {__title__}, {self.set_actual_quote.__name__}: '
                                     f'the index {int_index} is out of range! -----')

                my_actual_tuple = self._my_table_sql_performance_watch_list.get_table_entire_row(int_index, False)

                self._str_actual_quote_isin = my_actual_tuple[
                    self._int_performance_watch_list_quote_isin_column_index]

            except ValueError as e:

                print(e)

                exit(1)

    def set_performance_data_of_quote(self, str_quote_isin: str) -> None:

        if self._my_y_finance is not None:

            if not self.check_quote_in_watch_list(str_quote_isin):

                self._my_y_finance.set_actual_quote_isin(str_quote_isin)

                self._my_y_finance.get_actual_quote_ticker_data_from_y_finance()

                self._my_table_sql_performance_watch_list.set_sql_table_performance_watch_list_entire_row(
                    self._my_y_finance.get_actual_quote_dict_performance_watch_list_data)

        else:

            print(f'----- Info from {__title__}, {self.set_performance_data_of_quote.__name__}: '
                  f'Instance y_fiance is None and thus setting of new quotes is not supported!  ')

    def get_performance_data_of_quote(self) -> None:

        if self._my_y_finance is not None:

            self._my_table_sql_performance_watch_list.set_sql_table_performance_watch_list_entire_row(
                self._my_y_finance.get_actual_quote_dict_performance_watch_list_data)

        else:

            print(f'----- Info from {__title__}, {self.get_performance_data_of_quote.__name__}: '
                  f'Instance y_fiance is None and thus getting data of new quotes is not supported!  ')

    def del_quote(self, str_isin_number: str) -> None:

        self._my_table_sql_performance_watch_list.del_sql_table_performance_watch_list_single_quote(str_isin_number)

    def check_quote_in_watch_list(self, str_isin_number: str) -> bool:

        return self._my_table_sql_performance_watch_list.check_sql_table_performance_watch_list_is_quote_per_isin(
            str_isin_number)

    def get_num_quotes_in_watch_list(self) -> int:

        return self._my_table_sql_performance_watch_list.get_table_number_rows()

    def evaluate_performance_credits(self) -> None:

        # performance watch lists offer a date, and thus we need to transfer into the performance credit watch list the latest one
        self._transfer_latest_table_name()

        self._get_available_performance_watch_list_tables()

        self._my_table_sql_performance_credit_watch_list.set_available_performance_watch_list_tables(self._list_performance_watch_list_tables)

        self._my_table_sql_performance_credit_watch_list.evaluate_performance_credits()

    def get_segmented_average_change_percent(self) -> list:

        return  self._list_sectors_change_percent_table

    def get_industries_average_change_percent(self) -> list:

        self._calculate_industries_average_change_percent()

        return self._list_industries_change_percent_table

    def get_performance_watch_list_data_per_quote_isin(self, str_quote_isin) -> dict:

        return self. _my_table_sql_performance_watch_list.get_performance_watch_list_date_per_quote_isin(str_quote_isin)



if __name__ == "__main__":
    my_y_finance = myYFinance.MyYFinance()
    my_watch_list = MyPerformanceWatchList(None, '/Users/oliverrudow/PycharmProjects/Data', 'shares_data_base.db')
    # my_watch_list.set_performance_data_of_quote('US0378331005')
    # print(my_watch_list.get_table_column_names())
    print(my_watch_list.get_available_performance_watch_list_tables)
    print(my_watch_list.check_quote_in_watch_list('US0378331005'))
    print(my_watch_list.get_performance_watch_list_data_per_quote_isin('US0378331005'))
    my_watch_list.close_sql_data_base()