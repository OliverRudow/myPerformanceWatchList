"""myTableSQLPerformanceCreditWatchList.py."""

__title__: str = "myTableSQLPerformanceCreditWatchList"
__version__: str = "0.1.1"
__author__: str = "Oliver Rudow"
__email__: str = "oliver.rudow@googlemail.com"
__copyright__: str = "Copyright 2026, Brain Center Höfen"

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import dataclasses
import sqlite3
from typing import Optional
from mydatabase import mySQLDataBase, myTableSQL
from myauxiliary import myAuxiliary
from mysharesdefinition import myPerformanceWatchListDefinitions, myStaticWatchListDefinitions


def helper_built_inner_text_from_performance_watch_list_tables(str_id: str, str_col: str, list_tables: list) -> str:

    str_text: str = ''

    if list_tables.__len__() > 0:

        for index, element in enumerate(list_tables):

            index = index + 1

            str_text = str_text + f' SELECT {str_id}, {index} AS tab_order, CASE WHEN {str_col} >= 0 THEN 1 ELSE 0 END AS bin_val FROM {element} UNION ALL'

        str_text = str_text.rstrip().removesuffix("UNION ALL")
        str_text = str_text + ' '

    return str_text


@dataclasses.dataclass(init=False)
class MyTableSQLPerformanceCreditWatchList(myTableSQL.MyTableSQL):
    """
        Class for providing variables and functions to manage the Web Shop List.
        The Class is based on SQLite3.
    """

    _str_performance_watch_list_name: str = dataclasses.field(repr=False, default='')

    _dict_table_settings: dict[str, tuple] = dataclasses.field(repr=False, default=dict[str, tuple])

    # column indices
    _int_performance_watch_list_quote_isin_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_relative_daily_span_credit_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_interday_momentum_credit_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_intraday_momentum_credit_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_relative_volume_credit_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_relative_volume_10_day_credit_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_fifty_two_weeks_low_momentum_credit_column_index: int = dataclasses.field(repr=False, default=0)
    _int_performance_watch_list_fifty_two_weeks_high_momentum_credit_column_index: int = dataclasses.field(repr=False,
                                                                                                          default=0)
    _int_performance_watch_list_fifty_day_momentum_credit_column_index: int = dataclasses.field(repr=False,
                                                                                                           default=0)
    _int_performance_watch_list_two_hundred_day_momentum_credit_column_index: int = dataclasses.field(repr=False,
                                                                                                default=0)
    _int_performance_watch_list_segment_change_percent_credit_column_index: int = dataclasses.field(repr=False,
                                                                                                      default=0)

    _int_performance_watch_list_twenty_day_change_percent_json_object_credit_column_index: int = dataclasses.field(
                                                                                                    repr=False,
                                                                                                    default=0)
    _int_performance_watch_list_twenty_day_change_percent_credit_column_index: int = dataclasses.field(repr=False,
                                                                                                       default=0)

    _int_performance_watch_list_absolut_score_column_index: int = dataclasses.field(repr=False,
                                                                                default=0)

    # column names
    _str_performance_watch_list_quote_isin_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_relative_daily_span_credit_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_interday_momentum_credit_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_intraday_momentum_credit_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_relative_volume_credit_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_relative_volume_10_day_credit_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_fifty_two_weeks_low_momentum_credit_column_name: str = dataclasses.field(repr=False, default='')
    _str_performance_watch_list_fifty_two_weeks_high_momentum_credit_column_name: str = dataclasses.field(repr=False,
                                                                                                         default='')
    _str_performance_watch_list_fifty_day_momentum_credit_column_name: str = dataclasses.field(repr=False,
                                                                                                          default='')
    _str_performance_watch_list_two_hundred_day_momentum_credit_column_name: str = dataclasses.field(repr=False,
                                                                                               default='')
    _str_performance_watch_list_segment_change_percent_credit_column_name: str = dataclasses.field(repr=False,
                                                                                                     default='')
    _str_performance_watch_list_twenty_day_change_percent_json_object_credit_column_name: str = dataclasses.field(repr=False,
                                                                                                   default='')
    _str_performance_watch_list_twenty_day_change_percent_credit_column_name: str = dataclasses.field(repr=False,
                                                                                                   default='')
    _str_performance_watch_list_absolut_score_column_name: str = dataclasses.field(repr=False, default='')

    # value
    _str_performance_watch_list_quote_isin_value: str = dataclasses.field(repr=False, default='')
    _int_performance_watch_list_relative_daily_span_credit_value: int | str = dataclasses.field(repr=False, default='')
    _int_performance_watch_list_interday_momentum_credit_value: int | str = dataclasses.field(repr=False, default='')
    _int_performance_watch_list_intraday_momentum_credit_value: int | str = dataclasses.field(repr=False, default='')
    _int_performance_watch_list_relative_volume_credit_value: int | str = dataclasses.field(repr=False, default='')
    _int_performance_watch_list_relative_volume_10_day_credit_value: int | str = dataclasses.field(repr=False, default='')
    _int_performance_watch_list_fifty_two_weeks_low_momentum_credit_value: int | str = dataclasses.field(repr=False, default='')
    _int_performance_watch_list_fifty_two_weeks_high_momentum_credit_value: int | str = dataclasses.field(repr=False,
                                                                                                         default='')
    _int_performance_watch_list_fifty_day_momentum_credit_value: int | str = dataclasses.field(repr=False,
                                                                                                          default='')
    _int_performance_watch_list_two_hundred_day_momentum_credit_value: int | str = dataclasses.field(repr=False,
                                                                                               default='')
    _int_performance_watch_list_segment_change_percent_credit_value: int | str = dataclasses.field(repr=False,
                                                                                                     default='')
    _b_performance_watch_list_twenty_day_change_percent_json_object_credit_value: bytes | str = dataclasses.field(repr=False,
                                                                                                   default='')
    _int_performance_watch_list_twenty_day_change_percent_credit_value: int | str = dataclasses.field(repr=False,
                                                                                                   default='')
    _float_performance_watch_list_absolute_score_value: float | str = dataclasses.field(repr=False, default='')

    # source column names
    _str_source_table_name: str = dataclasses.field(repr=False, default='')
    _str_source_quote_isin_column_name: str = dataclasses.field(repr=False, default='')
    _str_source_relative_daily_span_column_name: str = dataclasses.field(repr=False, default='')
    _str_source_change_percent: str = dataclasses.field(repr=False, default='')
    _str_source_interday_momentum_column_name: str = dataclasses.field(repr=False, default='')
    _str_source_intraday_momentum_column_name: str = dataclasses.field(repr=False, default='')
    _str_source_relative_volume_column_name: str = dataclasses.field(repr=False, default='')
    _str_source_relative_volume_10_day_column_name: str = dataclasses.field(repr=False, default='')
    _str_source_fifty_two_weeks_low_momentum_column_name: str = dataclasses.field(repr=False, default='')
    _str_source_fifty_two_weeks_high_momentum_column_name: str = dataclasses.field(repr=False, default='')
    _str_source_fifty_day_momentum_column_name: str = dataclasses.field(repr=False, default='')
    _str_source_two_hundred_day_momentum_column_name: str = dataclasses.field(repr=False, default='')
    _str_source_segment_column_name: str = dataclasses.field(repr=False, default='')

    # score table
    _str_score_table_name: str = dataclasses.field(repr=False, default='')
    _str_score_table_credit_points_column_name: str = dataclasses.field(repr=False, default='')
    _str_score_table_min_threshold_column_name: str = dataclasses.field(repr=False, default='')

    _list_sectors_change_percent_score: list = dataclasses.field(repr=False, default=list)

    _list_available_performance_watch_list_tables: list = dataclasses.field(repr=False, default=list)

    # Variables for use with SQLite3
    _str_insert_string: str = dataclasses.field(repr=False, default='')

    _list_entire_row: list = dataclasses.field(repr=False, default=list)

    def __init__(self, the_sql_connection: sqlite3.Connection,
                 the_sql_cursor: sqlite3.Cursor) -> None:
        super().__init__(the_sql_connection, the_sql_cursor)

        self._dict_table_settings = {}

        # SQL Data Base Scheme
        self.set_sql_data_base_schema(myPerformanceWatchListDefinitions.STR_DATA_BASE_SCHEMA_NAME)

        # SQL Table Name
        self.set_flag_add_date_2_table_name(False)
        self.set_table_name(myPerformanceWatchListDefinitions.STR_DATA_BASE_TABLE_EVAL_NAME)

        # delete preceding tables
        self.set_flag_clean_preceded_tables(myPerformanceWatchListDefinitions.DATA_BASE_FLAG_CLEAN_PRECEDED_DATA)
        self.set_number_preceded_tables(myPerformanceWatchListDefinitions.DATA_BASE_INT_NUMBER_PRECEDED_DATA)

        if self._flag_clean_preceded_tables:
            self.clean_preceded_tables(self._str_table_name)

        # add date to table name
        if self._flag_add_date_2_file_name:
            self.set_table_name(myAuxiliary.add_date_2_object_name(self.get_table_name, 'tailing'))

        # column quote isin
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_QUOTE_ISIN

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column relative daily span
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_RELATIVE_DAILY_SPAN

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column interday momentum
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_INTERDAY_MOMENTUM

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column intraday momentum
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_INTRADAY_MOMENTUM

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column relative volume
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_RELATIVE_VOLUME

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column relative volume 10 day
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_RELATIVE_VOLUME_10_DAY

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column fifty-two weeks low
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_FIFTY_TWO_WEEKS_LOW_MOMENTUM

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column fifty-two weeks high
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_FIFTY_TWO_WEEKS_HIGH_MOMENTUM

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column fifty day
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_FIFTY_DAY_MOMENTUM

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column two hundred day
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_TWO_HUNDRED_DAY_MOMENTUM

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column segment change percent
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_SECTION_CHANGE_PERCENT

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column twenty day json object
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_TWENTY_DAY_CHANGE_PERCENT_JSON_OBJECT

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column twenty day json object
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_TWENTY_DAY_CHANGE_PERCENT

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # column absolute score
        my_special_tuple = myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_ABSOLUTE_SCORE

        self._dict_table_settings[my_special_tuple[self._index_tuple.OPTION_NAME]] = (
            my_special_tuple)[self._index_tuple.DATA_CONTENT]

        # SQL Data Base Column Settings
        self.set_dict_table_settings(self._dict_table_settings)

        # check static watch list exists
        self._str_some_table_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_QUOTE_ISIN)

        self.drop_sql_table()

        self._bool_sql_data_base_table = (self.check_sql_data_base_table_exists() and
                                      self.check_sql_data_base_table_column_name(self._str_some_table_column_name) and
                                      self.check_sql_data_base_table_is_not_empty())

        self._init_performance_watch_list_eval_columns()

        if not self._bool_sql_data_base_table:

            self.create_sql_data_base_table()

        self._init_source_table()

        self._init_score_table()

        self._list_segment_change_percent_score = []

        self._list_available_performance_watch_list_tables = []

    def _init_performance_watch_list_eval_columns(self) -> None:

        self._str_performance_watch_list_quote_isin_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_QUOTE_ISIN)

        self._int_performance_watch_list_quote_isin_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_QUOTE_ISIN)

        self._str_performance_watch_list_relative_daily_span_credit_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_RELATIVE_DAILY_SPAN)

        self._int_performance_watch_list_relative_daily_span__column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_RELATIVE_DAILY_SPAN)

        self._str_performance_watch_list_interday_momentum_credit_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_INTERDAY_MOMENTUM)

        self._int_performance_watch_list_interday_momentum_credit_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_INTERDAY_MOMENTUM)

        self._str_performance_watch_list_intraday_momentum_credit_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_INTRADAY_MOMENTUM)

        self._int_performance_watch_list_intraday_momentum_credit_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_INTRADAY_MOMENTUM)

        self._str_performance_watch_list_relative_volume_credit_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_RELATIVE_VOLUME)

        self._int_performance_watch_list_relative_volume_credit_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_RELATIVE_VOLUME)

        self._str_performance_watch_list_relative_volume_10_day_credit_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_RELATIVE_VOLUME_10_DAY)

        self._int_performance_watch_list_relative_volume_10_day_credit_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_RELATIVE_VOLUME_10_DAY)

        self._str_performance_watch_list_fifty_two_weeks_low_momentum_credit_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_FIFTY_TWO_WEEKS_LOW_MOMENTUM)

        self._int_performance_watch_list_fifty_two_weeks_low_momentum_credit_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_FIFTY_TWO_WEEKS_LOW_MOMENTUM)

        self._str_performance_watch_list_fifty_two_weeks_high_momentum_credit_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_FIFTY_TWO_WEEKS_HIGH_MOMENTUM)

        self._int_performance_watch_list_fifty_two_weeks_high_momentum_credit_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_FIFTY_TWO_WEEKS_HIGH_MOMENTUM)

        self._str_performance_watch_list_fifty_day_momentum_credit_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_FIFTY_DAY_MOMENTUM)

        self._int_performance_watch_list_fifty_day_momentum_credit_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_FIFTY_DAY_MOMENTUM)

        self._str_performance_watch_list_two_hundred_day_momentum_credit_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_TWO_HUNDRED_DAY_MOMENTUM)

        self._int_performance_watch_list_two_hundred_day_momentum_credit_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_TWO_HUNDRED_DAY_MOMENTUM)

        self._str_performance_watch_list_segment_change_percent_credit_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_SECTION_CHANGE_PERCENT)

        self._int_performance_watch_list_segment_change_percent_credit_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_SECTION_CHANGE_PERCENT)

        self._str_performance_watch_list_twenty_day_change_percent_json_object_credit_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_TWENTY_DAY_CHANGE_PERCENT_JSON_OBJECT)

        self._int_performance_watch_list_twenty_day_change_percent_json_object_credit_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_TWENTY_DAY_CHANGE_PERCENT_JSON_OBJECT)

        self._str_performance_watch_list_twenty_day_change_percent_credit_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_TWENTY_DAY_CHANGE_PERCENT)

        self._int_performance_watch_list_twenty_day_change_percent_credit_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_TWENTY_DAY_CHANGE_PERCENT)

        self._str_performance_watch_list_absolut_score_column_name = self.get_column_name_from_dict(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_ABSOLUTE_SCORE)

        self._int_performance_watch_list_absolut_score_column_index = self.get_column_index_from_list(
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_EVAL_ABSOLUTE_SCORE)

    def _init_source_table(self) -> None:
        self._str_source_table_name = myPerformanceWatchListDefinitions.STR_DATA_BASE_TABLE_NAME

        self._str_source_quote_isin_column_name = (
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_QUOTE_ISIN[
                self._index_tuple.DATA_CONTENT][0])

        self._str_source_relative_daily_span_column_name = (
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_RELATIVE_DAILY_SPAN[
                self._index_tuple.DATA_CONTENT][0])

        self._str_source_interday_momentum_column_name = (
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_INTERDAY_MOMENTUM[
                self._index_tuple.DATA_CONTENT][0])

        self._str_source_intraday_momentum_column_name = (
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_INTRADAY_MOMENTUM[
                self._index_tuple.DATA_CONTENT][0])

        self._str_source_change_percent = (
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_REGULAR_MARKET_CHANGE_PERCENT)[
            self._index_tuple.DATA_CONTENT][0]

        self._str_source_relative_volume_column_name = (
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_RELATIVE_VOLUME[
                self._index_tuple.DATA_CONTENT][0])

        self._str_source_relative_volume_10_day_column_name = (
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_RELATIVE_VOLUME_10_DAY[
                self._index_tuple.DATA_CONTENT][0])

        self._str_source_fifty_two_weeks_low_momentum_column_name = (
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_LOW_MOMENTUM[
                self._index_tuple.DATA_CONTENT][0])

        self._str_source_fifty_two_weeks_high_momentum_column_name = (
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_TWO_WEEK_HIGH_MOMENTUM[
                self._index_tuple.DATA_CONTENT][0])

        self._str_source_fifty_day_momentum_column_name = (
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_FIFTY_DAY_MOMENTUM[
                self._index_tuple.DATA_CONTENT][0])

        self._str_source_two_hundred_day_momentum_column_name = (
            myPerformanceWatchListDefinitions.TUPLE_PERFORMANCE_WATCH_LIST_TWO_HUNDRED_DAY_MOMENTUM[
                self._index_tuple.DATA_CONTENT][0])

        self._str_source_segment = myStaticWatchListDefinitions.TUPLE_STATIC_WATCH_LIST_QUOTE_SECTOR[
                self._index_tuple.DATA_CONTENT][0]

        #TODO check table and columns are existing

    def set_source_table_name(self, str_table_name: str) -> None:

        self._str_source_table_name = str_table_name

    def set_sectors_change_percent_score_list(self, list_sectors_score_list: list) -> None:

        self._list_sectors_change_percent_score = list_sectors_score_list

    def set_available_performance_watch_list_tables(self, list_available_performance_watch_list_tables: list) -> None:

        self._list_available_performance_watch_list_tables = list_available_performance_watch_list_tables

    def _init_score_table(self) -> None:

        self._str_score_table_name =myPerformanceWatchListDefinitions.STR_SCORE_TABLE_NAME

        self._str_score_table_min_threshold_column_name = (
            myPerformanceWatchListDefinitions.TUPLE_SCORE_TABLE_MIN_THRESHOLD)[
                                        self._index_tuple.DATA_CONTENT][0]

        self._str_score_table_credit_points_column_name = (
            myPerformanceWatchListDefinitions.TUPLE_SCORE_TABLE_CREDIT_POINTS)[
                                        self._index_tuple.DATA_CONTENT][0]

    def get_performance_watch_list_eval_quote_isin_column_name(self) -> str:

        return self._str_performance_watch_list_quote_isin_column_name

    def _get_data_from_performance_watch_list(self) -> None:

        str_table_definition: str = f'{self._str_performance_watch_list_quote_isin_column_name}'

        str_text = (f'INSERT INTO {self._str_sql_schema}.{self._str_table_name}'
                    f'({str_table_definition}) '
                    f'SELECT {self._str_source_quote_isin_column_name} '
                    f'FROM {self._str_source_table_name}')

        try:

            self._my_sql_cursor.execute(str_text)

            self._my_sql_connection.commit()

        except sqlite3.OperationalError as err:

            print(f'---- Operational Error in {__title__}, {self._get_data_from_performance_watch_list.__name__} ----, \n'
                  f'---- the Text {str_text} has caused an Error {err} ! ----')

            exit(1)

    def _set_score_table(self, list_score_table_data: list[tuple],
                         set_first_column: Optional[set] = None,
                         set_second_column: Optional[set] = None) -> None:

        self.drop_sql_table(myPerformanceWatchListDefinitions.STR_SCORE_TABLE_NAME)

        _first_column = ()

        if set_first_column is None:

            _first_column = myPerformanceWatchListDefinitions.TUPLE_SCORE_TABLE_MIN_THRESHOLD[
                                        self._index_tuple.DATA_CONTENT]

        else:

            _first_column = set_first_column

        _second_column = ()

        if set_second_column is None:

            _second_column = myPerformanceWatchListDefinitions.TUPLE_SCORE_TABLE_CREDIT_POINTS[
                self._index_tuple.DATA_CONTENT]

        else:

            _second_column = set_second_column

        my_list: list = [' '.join(_first_column), ' '.join(_second_column)]

        str_table_definition = ', '.join(my_list)


        str_text = (f'CREATE TABLE IF NOT EXISTS {myPerformanceWatchListDefinitions.STR_SCORE_TABLE_NAME} '
                    f'({str_table_definition})')

        str_text_insert = f'INSERT INTO {myPerformanceWatchListDefinitions.STR_SCORE_TABLE_NAME} VALUES (?, ?) '

        try:

            self._my_sql_cursor.execute(str_text)

            self._my_sql_cursor.executemany(str_text_insert, list_score_table_data)

            self._my_sql_connection.commit()

        except sqlite3.OperationalError as err:

            print(f'---- Operational Error in {__title__}, {self._set_score_table.__name__} ----, \n'
                  f'---- the Text {str_text} has caused an Error {err} ! ----')

            exit(1)

    def _check_column_exists(self, str_table_name: str, column_name: str) -> bool:

        str_text = (f'SELECT EXISTS ( '
                    f' SELECT 1 ' 
                    f' FROM pragma_table_info({str_table_name}) '
                    f' WHERE name = {column_name} '
                    f' ) ')

        try:

            self._my_sql_cursor.execute(str_text)

            result = self._my_sql_cursor.fetchone()

            self._my_sql_connection.commit()

            print(result)

        except sqlite3.OperationalError as err:

            print(f'---- Operational Error in {__title__}, '
                  f'{self._check_column_exists.__name__} ----, \n'
                  f'---- the Text {str_text} has caused an Error {err} ! ----')

            exit(1)

        return True

    def _eval_relative_daily_span_credit(self) -> None:

        # generate score table
        self._set_score_table(myPerformanceWatchListDefinitions.LIST_RELATIVE_DAILY_SPAN_SCORE_TABLE)

        str_target_column = self._str_performance_watch_list_relative_daily_span_credit_column_name
        str_source_column = self._str_source_relative_daily_span_column_name

        self._evaluate_parameter_credit_through_score_table(str_target_column, str_source_column)

    def _eval_interday_momentum_credit(self) -> None:

        # generate score table
        self._set_score_table(myPerformanceWatchListDefinitions.LIST_INTERDAY_MOMENTUM_SCORE_TABLE)

        str_target_column = self._str_performance_watch_list_interday_momentum_credit_column_name
        str_source_column = self._str_source_interday_momentum_column_name

        self._evaluate_parameter_credit_through_score_table(str_target_column, str_source_column)

    def _eval_intraday_momentum_credit(self) -> None:

        # generate score table
        self._set_score_table(myPerformanceWatchListDefinitions.LIST_INTRADAY_MOMENTUM_SCORE_TABLE)

        str_target_column = self._str_performance_watch_list_intraday_momentum_credit_column_name
        str_source_column = self._str_source_intraday_momentum_column_name

        self._evaluate_parameter_credit_through_score_table(str_target_column, str_source_column)

    def _eval_relative_volume_credit(self) -> None:

        # generate score table
        self._set_score_table(myPerformanceWatchListDefinitions.LIST_RELATIVE_VOLUME_SCORE_TABLE)

        str_target_column = self._str_performance_watch_list_relative_volume_credit_column_name
        str_source_column = self._str_source_relative_volume_column_name

        self._evaluate_parameter_credit_through_score_table(str_target_column, str_source_column)

    def _eval_relative_volume_10_day_credit(self) -> None:

        # generate score table
        self._set_score_table(myPerformanceWatchListDefinitions.LIST_RELATIVE_VOLUME_10_DAY_SCORE_TABLE)

        str_target_column = self._str_performance_watch_list_relative_volume_10_day_credit_column_name
        str_source_column = self._str_source_relative_volume_10_day_column_name

        self._evaluate_parameter_credit_through_score_table(str_target_column, str_source_column)

    def _eval_fifty_two_weeks_low_momentum_credit(self) -> None:

        # generate score table
        self._set_score_table(myPerformanceWatchListDefinitions.LIST_FIFTY_TWO_WEEKS_LOW_MOMENTUM_TABLE)

        str_target_column = self._str_performance_watch_list_fifty_two_weeks_low_momentum_credit_column_name
        str_source_column = self._str_source_fifty_two_weeks_low_momentum_column_name

        self._evaluate_parameter_credit_through_score_table(str_target_column, str_source_column)

    def _eval_fifty_two_weeks_high_momentum_credit(self) -> None:

        # generate score table
        self._set_score_table(myPerformanceWatchListDefinitions.LIST_FIFTY_TWO_WEEKS_HIGH_MOMENTUM_TABLE)

        str_target_column = self._str_performance_watch_list_fifty_two_weeks_high_momentum_credit_column_name
        str_source_column = self._str_source_fifty_two_weeks_high_momentum_column_name

        self._evaluate_parameter_credit_through_score_table(str_target_column, str_source_column)

    def _eval_fifty_day_momentum_credit(self) -> None:

        # generate score table
        self._set_score_table(myPerformanceWatchListDefinitions.LIST_FIFTY_DAY_MOMENTUM_TABLE)

        str_target_column = self._str_performance_watch_list_fifty_day_momentum_credit_column_name
        str_source_column = self._str_source_fifty_day_momentum_column_name

        self._evaluate_parameter_credit_through_score_table(str_target_column, str_source_column)

    def _eval_two_hundred_day_momentum_credit(self) -> None:

        # generate score table
        self._set_score_table(myPerformanceWatchListDefinitions.LIST_TWO_HUNDRED_DAY_MOMENTUM_TABLE)

        str_target_column = self._str_performance_watch_list_two_hundred_day_momentum_credit_column_name
        str_source_column = self._str_source_two_hundred_day_momentum_column_name

        self._evaluate_parameter_credit_through_score_table(str_target_column, str_source_column)

    def _eval_sectors_change_percent_credit(self) -> None:

        # generate score table
        self._set_score_table(self._list_sectors_change_percent_score,
                              myStaticWatchListDefinitions.TUPLE_STATIC_WATCH_LIST_QUOTE_SECTOR[self._index_tuple.DATA_CONTENT],
                              myPerformanceWatchListDefinitions.TUPLE_SCORE_TABLE_CREDIT_POINTS[self._index_tuple.DATA_CONTENT])

        str_target = self._str_table_name
        str_target_id = self._str_performance_watch_list_quote_isin_column_name
        str_target_col = self._str_performance_watch_list_segment_change_percent_credit_column_name

        str_source = myStaticWatchListDefinitions.STR_DATA_BASE_TABLE_NAME
        str_source_id = myStaticWatchListDefinitions.TUPLE_STATIC_WATCH_LIST_QUOTE_ISIN[self._index_tuple.DATA_CONTENT][0]
        str_source_col =self._str_source_segment

        str_score = self._str_score_table_name
        str_score_th = myStaticWatchListDefinitions.TUPLE_STATIC_WATCH_LIST_QUOTE_SECTOR[self._index_tuple.DATA_CONTENT][0]
        str_score_credit = myPerformanceWatchListDefinitions.TUPLE_SCORE_TABLE_CREDIT_POINTS[self._index_tuple.DATA_CONTENT][0]

        str_text = (f'UPDATE {str_target} AS target '
                    f'SET {str_target_col} = ('
                    f'SELECT cfg.{str_score_credit} '
                    f'FROM {str_score} AS cfg '
                    f'INNER JOIN {str_source} AS src ON target.{str_target_id} = src.{str_source_id} '
                    f'WHERE src.{str_source_col} == cfg.{str_score_th} '
                    f'AND src.{str_source_col} IS NOT NULL '
                    f'AND src.{str_source_col} != "" '
                    f'ORDER BY cfg.{str_score_th} DESC '
                    f'LIMIT 1 '
                    f') '
                    f'WHERE EXISTS ('
                    f' SELECT 1 FROM {str_source} AS src '
                    f'  WHERE src.{str_source_id} = target.{str_target_id} '
                    f'    AND src.{str_source_col} IS NOT NULL '
                    f'    AND src.{str_source_col} != "")')

        try:

            self._my_sql_cursor.execute(str_text)

            self._my_sql_connection.commit()

        except sqlite3.OperationalError as err:

            print(f'---- Operational Error in {__title__}, '
                  f'{self._eval_sectors_change_percent_credit.__name__} ----, \n'
                  f'---- the Text {str_text} has caused an Error {err} ! ----')

            exit(1)

    def _eval_twenty_day_change_percent_json_object(self) -> None:

        str_target = self._str_table_name
        str_target_id = self._str_performance_watch_list_quote_isin_column_name
        str_target_col = self._str_performance_watch_list_twenty_day_change_percent_json_object_credit_column_name

        str_source_id = self._str_source_quote_isin_column_name
        str_source_col = self._str_source_change_percent

        _list_corrected_performance_watch_list_tables = []

        for element in self._list_available_performance_watch_list_tables:

            if self.check_sql_data_base_table_column_name(str_source_col, element):

                _list_corrected_performance_watch_list_tables.append(element)

        str_inner_text = helper_built_inner_text_from_performance_watch_list_tables(str_source_id,
                                                                                    str_source_col,
                                                                                    _list_corrected_performance_watch_list_tables)

        str_text = (f'UPDATE {str_target} '
                    f'SET {str_target_col} = ( '
                    f' SELECT '
                    f'   CASE '
                    f'      WHEN COUNT(sub.bin_val) = 0 THEN NULL '
                    f'      ELSE CAST( '
                    f'          json_object( '
                    f'              "list", json_group_array(sub.bin_val ORDER BY sub.tab_order),'
                    f'              "ratio", ROUND(SUM(sub.bin_val) * 1.0 / COUNT(sub.bin_val), 2) '
                    f'           ) AS BLOB '
                    f'         ) '
                    f'      END '
                    f' FROM ({str_inner_text}) sub  '
                    f' WHERE sub.{str_source_id} = {str_target}.{str_target_id} )')

        try:

            self._my_sql_cursor.execute(str_text)

            self._my_sql_connection.commit()

        except sqlite3.OperationalError as err:

            print(f'---- Operational Error in {__title__}, '
                  f'{self._eval_twenty_day_change_percent_json_object.__name__} ----, \n'
                  f'---- the Text {str_text} has caused an Error {err} ! ----')

            exit(1)

    def _eval_twenty_day_change_percent_credit(self) -> None:

        # generate score table
        self._set_score_table(myPerformanceWatchListDefinitions.LIST_TWENTY_DAY_CHANGE_PERCENT_RATIO)

        str_table_name = self._str_table_name
        str_target_column = self._str_performance_watch_list_twenty_day_change_percent_credit_column_name
        str_source_column = self._str_performance_watch_list_twenty_day_change_percent_json_object_credit_column_name

        str_score = self._str_score_table_name
        str_score_th = self._str_score_table_min_threshold_column_name
        str_score_credit = self._str_score_table_credit_points_column_name

        str_text = (f'UPDATE {str_table_name} '
                    f' SET {str_target_column} = ( '
                    f' SELECT {str_score}.{str_score_credit} '
                    f' FROM {str_score} '
                    f' WHERE json_extract({str_table_name}.{str_source_column}, "$.ratio") >= {str_score}.{str_score_th})'
                    f' WHERE json_extract({str_table_name}.{str_source_column}, "$.ratio") IS NOT NULL')

        try:

            self._my_sql_cursor.execute(str_text)

            self._my_sql_connection.commit()

        except sqlite3.OperationalError as err:

            print(f'---- Operational Error in {__title__}, '
                  f'{self._eval_twenty_day_change_percent_credit.__name__} ----, \n'
                  f'---- the Text {str_text} has caused an Error {err} ! ----')

            exit(1)

    def _evaluate_parameter_credit_through_score_table(self, str_target_column: str,
                                                       str_source_column: str,
                                                       str_source_table_name: Optional[str] = None) -> None:

        if str_source_table_name is None:

            str_source: str = self._str_source_table_name

        else:

            str_source: str = str_source_table_name

        str_target = self._str_table_name

        str_score = self._str_score_table_name
        str_score_th = self._str_score_table_min_threshold_column_name
        str_score_credit = self._str_score_table_credit_points_column_name

        str_target_id = self._str_performance_watch_list_quote_isin_column_name
        str_source_id = self._str_performance_watch_list_quote_isin_column_name

        str_target_col = str_target_column
        str_source_col = str_source_column

        str_text = (f'UPDATE {str_target} AS target '
                    f'SET {str_target_col} = ('
                    f'SELECT cfg.{str_score_credit} '
                    f'FROM {str_score} AS cfg '
                    f'INNER JOIN {str_source} AS src ON target.{str_target_id} = src.{str_source_id} '
                    f'WHERE src.{str_source_col} >= cfg.{str_score_th} '
                    f'AND src.{str_source_col} IS NOT NULL '
                    f'AND src.{str_source_col} != "" '
                    f'ORDER BY cfg.{str_score_th} DESC '
                    f'LIMIT 1 '
                    f') '
                    f'WHERE EXISTS ('
                    f' SELECT 1 FROM {str_source} AS src '
                    f'  WHERE src.{str_source_id} = target.{str_target_id} '
                    f'    AND src.{str_source_col} IS NOT NULL '
                    f'    AND src.{str_source_col} != "")')

        try:

            self._my_sql_cursor.execute(str_text)

            self._my_sql_connection.commit()

        except sqlite3.OperationalError as err:

            print(f'---- Operational Error in {__title__}, '
                  f'{self._evaluate_parameter_credit_through_score_table.__name__} ----, \n'
                  f'---- the Text {str_text} has caused an Error {err} ! ----')

            exit(1)

    def _evaluate_absolute_score_credit(self) -> None:

        self._set_score_table(myPerformanceWatchListDefinitions.LIST_WEIGHT_SCORE_TABLE,
                              myPerformanceWatchListDefinitions.TUPLE_SCORE_TABLE_WEIGHT_NAME[
                self._index_tuple.DATA_CONTENT],
                              myPerformanceWatchListDefinitions.TUPLE_SCORE_TABLE_WEIGHT[
                                  self._index_tuple.DATA_CONTENT]
                              )

        _score = self._str_score_table_name

        _score_first_col = myPerformanceWatchListDefinitions.TUPLE_SCORE_TABLE_WEIGHT_NAME[
            self._index_tuple.DATA_CONTENT][0]

        _score_second_col = myPerformanceWatchListDefinitions.TUPLE_SCORE_TABLE_WEIGHT[
            self._index_tuple.DATA_CONTENT][0]

        _table = self._str_table_name

        _result = self._str_performance_watch_list_absolut_score_column_name

        value_1 = self._str_performance_watch_list_relative_daily_span_credit_column_name

        value_2 = self._str_performance_watch_list_interday_momentum_credit_column_name

        value_3 = self._str_performance_watch_list_intraday_momentum_credit_column_name

        value_4 = self._str_performance_watch_list_relative_volume_credit_column_name

        value_5 = self._str_performance_watch_list_relative_volume_10_day_credit_column_name

        value_6 = self._str_performance_watch_list_fifty_two_weeks_low_momentum_credit_column_name

        value_7 = self._str_performance_watch_list_fifty_two_weeks_high_momentum_credit_column_name

        value_8 = self._str_performance_watch_list_fifty_day_momentum_credit_column_name

        value_9 = self._str_performance_watch_list_two_hundred_day_momentum_credit_column_name

        value_10 = self._str_performance_watch_list_segment_change_percent_credit_column_name

        value_11 = self._str_performance_watch_list_twenty_day_change_percent_credit_column_name

        str_text = (f'UPDATE {_table} '
                    f'SET {_result} = ROUND(CAST('
                    f'('
                    f'COALESCE({value_1} * s.w_1, 0) + '
                    f'COALESCE({value_2} * s.w_2, 0) + '
                    f'COALESCE({value_3} * s.w_3, 0) + '
                    f'COALESCE({value_4} * s.w_4, 0) + '
                    f'COALESCE({value_5} * s.w_5, 0) + '
                    f'COALESCE({value_6} * s.w_6, 0) + '
                    f'COALESCE({value_7} * s.w_7, 0) + '
                    f'COALESCE({value_8} * s.w_8, 0) + '
                    f'COALESCE({value_9} * s.w_9, 0) + '
                    f'COALESCE({value_10} * s.w_10, 0) + '
                    f'COALESCE({value_11} * s.w_11, 0)) AS REAL '
                    f') '
                    f'/ '
                    f'CAST('
                    f'(CASE WHEN {value_1} IS NOT NULL THEN s.w_1 ELSE 0 END) + '
                    f'(CASE WHEN {value_2} IS NOT NULL THEN s.w_2 ELSE 0 END) + '
                    f'(CASE WHEN {value_3} IS NOT NULL THEN s.w_3 ELSE 0 END) + '
                    f'(CASE WHEN {value_4} IS NOT NULL THEN s.w_4 ELSE 0 END) + '
                    f'(CASE WHEN {value_5} IS NOT NULL THEN s.w_5 ELSE 0 END) + '
                    f'(CASE WHEN {value_6} IS NOT NULL THEN s.w_6 ELSE 0 END) + '
                    f'(CASE WHEN {value_7} IS NOT NULL THEN s.w_7 ELSE 0 END) + '
                    f'(CASE WHEN {value_8} IS NOT NULL THEN s.w_8 ELSE 0 END) + '
                    f'(CASE WHEN {value_9} IS NOT NULL THEN s.w_9 ELSE 0 END) + '
                    f'(CASE WHEN {value_10} IS NOT NULL THEN s.w_10 ELSE 0 END) + '
                    f'(CASE WHEN {value_11} IS NOT NULL THEN s.w_11 ELSE 0 END) '
                    f'AS REAL), 1) '
                    f'FROM '
                    f'( '
                    f'SELECT '
                    f'( SELECT {_score_second_col} FROM {_score} WHERE {_score_first_col} = \'weight_1\' ) AS w_1, '
                    f'( SELECT {_score_second_col} FROM {_score} WHERE {_score_first_col} = \'weight_2\' ) AS w_2, '
                    f'( SELECT {_score_second_col} FROM {_score} WHERE {_score_first_col} = \'weight_3\' ) AS w_3, '
                    f'( SELECT {_score_second_col} FROM {_score} WHERE {_score_first_col} = \'weight_4\' ) AS w_4, '
                    f'( SELECT {_score_second_col} FROM {_score} WHERE {_score_first_col} = \'weight_5\' ) AS w_5, '
                    f'( SELECT {_score_second_col} FROM {_score} WHERE {_score_first_col} = \'weight_6\' ) AS w_6, '
                    f'( SELECT {_score_second_col} FROM {_score} WHERE {_score_first_col} = \'weight_7\' ) AS w_7, '
                    f'( SELECT {_score_second_col} FROM {_score} WHERE {_score_first_col} = \'weight_8\' ) AS w_8, '
                    f'( SELECT {_score_second_col} FROM {_score} WHERE {_score_first_col} = \'weight_9\' ) AS w_9, '
                    f'( SELECT {_score_second_col} FROM {_score} WHERE {_score_first_col} = \'weight_10\' ) AS w_10, '
                    f'( SELECT {_score_second_col} FROM {_score} WHERE {_score_first_col} = \'weight_11\' ) AS w_11 '
                    f') '
                    f'AS s '
                    f'WHERE ('
                    f'{value_1} IS NOT NULL OR '
                    f'{value_2} IS NOT NULL OR '
                    f'{value_3} IS NOT NULL OR '
                    f'{value_4} IS NOT NULL OR '
                    f'{value_5} IS NOT NULL OR '
                    f'{value_6} IS NOT NULL OR '
                    f'{value_7} IS NOT NULL OR '
                    f'{value_8} IS NOT NULL OR '
                    f'{value_9} IS NOT NULL OR '
                    f'{value_10} IS NOT NULL OR '
                    f'{value_11} IS NOT NULL '
                    f')')

        try:

            self._my_sql_cursor.execute(str_text)

            self._my_sql_connection.commit()

        except sqlite3.OperationalError as err:

            print(f'---- Operational Error in {__title__}, {self._evaluate_absolute_score_credit.__name__} ----, \n'
                  f'---- the Text {str_text} has caused an Error {err} ! ----')

            exit(1)

    def evaluate_performance_credits(self) -> None:

        self._get_data_from_performance_watch_list()

        self._eval_relative_daily_span_credit()

        self._eval_interday_momentum_credit()

        self._eval_intraday_momentum_credit()

        self._eval_relative_volume_credit()

        self._eval_relative_volume_10_day_credit()

        self._eval_fifty_two_weeks_low_momentum_credit()

        self._eval_fifty_two_weeks_high_momentum_credit()

        self._eval_fifty_day_momentum_credit()

        self._eval_two_hundred_day_momentum_credit()

        self._eval_sectors_change_percent_credit()

        self._eval_twenty_day_change_percent_json_object()

        self._eval_twenty_day_change_percent_credit()

        self._evaluate_absolute_score_credit()

if __name__ == "__main__":
    mySQLDB = mySQLDataBase.MySQLDataBase()
