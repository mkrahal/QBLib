'''
############################################################################
#                                                                          #
#             QBLib - An SQL Query Construction Library                    #
#             -----------------------------------------                    #
#                                                                          #
#                                                                          #
#  MIT License                                                             #
#  Copyright © 2017 MK Rahal                                               #
#                                                                          #
#  Permission is hereby granted, free of charge, to any person             #
#  obtaining a copy of this software and associated documentation          #
#  files (the "Software"), to deal in the Software without                 #
#  restriction, including without limitation the rights to use,            #
#  copy, modify, merge, publish, distribute, sublicense, and/or            #
#  sell copies of the Software, and to permit persons to whom the          #
#  Software is furnished to do so, subject to the following conditions:    #
#                                                                          #
#  The above copyright notice and this permission notice shall be          #
#  included in all copies or substantial portions of the Software.         #
#                                                                          #
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,         #
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES         #
#  OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND                #
#  NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT             #
#  HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,            #
#  WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,      #
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER           #
#  DEALINGS IN THE SOFTWARE.                                               #
#                                                                          #
############################################################################
'''


class string_constants():

    no_size_dt = ["boolean", "smallint", "integer", "bigint", "real",
                  "float", "double precision", "date", "time",
                  "timestamp", "interval", "array", "multiset", "xml"]
    pass


class creation_tools(string_constants):

    def create_table(self, tbl_name, cnd_dict):
        columns_list = []

        sqs_pt1 = "CREATE TABLE `%s` " % (tbl_name)
        sqs_pt2 = "("
        sqs_pt3 = ")"

        count = 0
        for colname_key in cnd_dict.keys():
            count += 1
            sqv_pt1 = "%s " % (colname_key)
            columns_list.append(sqv_pt1)

            if len(cnd_dict[colname_key]) == 1 and cnd_dict[colname_key][0].lower(
            ) in string_constants.no_size_dt:
                sqv_pt2 = "%s" % (cnd_dict[colname_key][0].upper())
                columns_list.append(sqv_pt2)

            elif len(cnd_dict[colname_key]) == 2:
                sqv_pt2 = "%s(%s)" % (
                    cnd_dict[colname_key][0].upper(), str(cnd_dict[colname_key][1]))
                columns_list.append(sqv_pt2)

            elif len(cnd_dict[colname_key]) == 3 and \
                    cnd_dict[colname_key][0].lower() == ("DECIMAL".lower() or "NUMERIC".lower()):

                sqv_pt2 = "%s(%s, %s)" % (cnd_dict[colname_key][0].upper(), str(
                    cnd_dict[colname_key][1]), str(cnd_dict[colname_key][2]))

                columns_list.append(sqv_pt2)

            else:
                print "wrong datatype or wrong number of arguements please check syntax"

        columns_string = ", ".join(columns_list)
        sql_query = sqs_pt1 + sqs_pt2 + \
            columns_string + sqs_pt3

        return sql_query

    def add_columns(self, tbl_name, cnd_dict):
        columns_list = []

        sqs_pt1 = "ALTER TABLE `%s` " % (tbl_name)
        sqs_pt2 = "ADD ("
        sqs_pt3 = ")"

        count = 0
        for colname_key in cnd_dict.keys():
            count += 1
            sqv_pt1 = "[%s] " % (colname_key)
            columns_list.append(sqv_pt1)

            if len(cnd_dict[colname_key]) == 1 and cnd_dict[colname_key][0].lower(
            ) in string_constants.no_size_dt:
                sqv_pt2 = "%s" % (cnd_dict[colname_key][0].upper())
                columns_list.append(sqv_pt2)

            elif len(cnd_dict[colname_key]) == 2:
                sqv_pt2 = "%s(%s)" % (
                    cnd_dict[colname_key][0].upper(), str(cnd_dict[colname_key][1]))
                columns_list.append(sqv_pt2)

            elif len(cnd_dict[colname_key]) == 3 and \
                    cnd_dict[colname_key][0].lower() == ("DECIMAL".lower() or "NUMERIC".lower()):

                sqv_pt2 = "%s(%s, %s)" % (cnd_dict[colname_key][0].upper(), str(
                    cnd_dict[colname_key][1]), str(cnd_dict[colname_key][2]))

                columns_list.append(sqv_pt2)

            else:
                print "wrong datatype or wrong number of arguements please check syntax"

        columns_string = ", ".join(columns_list)
        sql_query = sqs_pt1 + sqs_pt2 + \
            columns_string + sqs_pt3

        return sql_query

    def define_index_col(self, tbl_name, col_name):
        sql_query = "ALTER TABLE %s ADD INDEX (%s)" % (tbl_name, col_name)
        return sql_query

    def define_primary_key(self, tbl_name, col_name):
        sql_query = "ALTER TABLE %s ADD PRIMARY KEY (%s)" % (
            tbl_name, col_name)
        return sql_query


class editing_tools():

    def insert_data(self, tbl_name, cnv_dict):
        columns_list = []
        values_list = []

        sqs_pt1 = "INSERT INTO %s(" % (tbl_name)
        sqs_pt2 = ") VALUES ("
        sqs_pt3 = ")"

        count = 0
        for colname_key in cnv_dict.keys():
            count += 1
            sqv_pt1 = "%s" % (colname_key)
            columns_list.append(sqv_pt1)

        count = 0
        for colname_key in columns_list:
            if colname_key != ', ':
                count += 1
                sqv_pt2 = "%s" % (str(cnv_dict[colname_key]))
                values_list.append(sqv_pt2)

        columns_string = ", ".join(columns_list)
        values_string = ", ".join(values_list)

        sql_query = (sqs_pt1 + columns_string +
                     sqs_pt2 + values_string +
                     sqs_pt3)

        return sql_query

    def import_csv(self, csv_file_loc, tbl_name, columns_list, ignore_rows=0):
        sqs_pt1 = "LOAD DATA INFILE '%s' INTO TABLE %s " % (
            csv_file_loc, tbl_name)
        sqs_pt2 = "FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\\n' "
        sqs_pt3 = "IGNORE %s ROWS (" % (str(ignore_rows))
        sqs_pt4 = ")"

        if isinstance(columns_list, str):
            columns_string = columns_list
        else:
            columns_string = ", ".join(columns_list)

        if ignore_rows > 0:
            sql_query = (sqs_pt1 + sqs_pt2 +
                         sqs_pt3 + columns_string +
                         sqs_pt4)
        else:
            sql_query = (sqs_pt1 + sqs_pt2 +
                         "(" + columns_string + sqs_pt4)

        return sql_query

    def export_csv(
            self,
            csv_file_dest,
            tbl_name,
            columns_list="*",
            col_name=None,
            search_term=None):
        sqv_pt1 = "SELECT %s FROM %s" % (columns_list, tbl_name)
        sqv_pt2 = "WHERE %s = '%s'" % (col_name, search_term)
        sqs_pt1 = "INTO OUTFILE '%s' " % (csv_file_dest)
        sqs_pt2 = "FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\\n'"

        if (col_name and search_term) is not None:
            sql_query = sqv_pt1 + sqv_pt2 + \
                sqs_pt1 + sqs_pt2
        elif (col_name and search_term) is None:
            sql_query = sqv_pt1 + sqs_pt1 + sqs_pt2
        else:
            print "Missing arguement(s), Please check your method call."

        return sql_query

    def delete_row(self, tbl_name, search_term, match_col):
        sql_query = "DELETE FROM %s WHERE %s=%s" % \
                    (tbl_name, match_col, search_term)
        return sql_query

    def delete_columns(self, tbl_name, columns_list):
        if isinstance(columns_list, str):
            sql_query = "ALTER TABLE %s DROP %s" % (tbl_name, columns_list)
        else:
            columns_string = ", DROP ".join(columns_list)
            sql_query = "ALTER TABLE %s DROP %s" % (tbl_name, columns_string)

        return sql_query


class processing_tools():

    def find_row(self, tbl_name, search_term, match_col, matchexact=True):
        if matchexact is True:
            sql_query = "SELECT * FROM %s WHERE %s = %s" % \
                        (str(tbl_name), str(match_col), str(search_term))
        else:
            sql_query = "SELECT * FROM %s WHERE %s LIKE \%%s\%" % \
                        (str(tbl_name), str(match_col), str(search_term))
        return sql_query

    def find_in_col(
            self,
            tbl_name,
            search_term,
            match_col,
            result_col,
            matchexact=True):
        number_cols = len(result_col)
        columns_list = []
        count = 0

        sqs_pt1 = "SELECT "

        if isinstance(result_col, str):
            columns_string = result_col
        else:
            for col_name in result_col:
                count += 1
                sqv_pt1 = "%s" % (str(col_name))
                columns_list.append(sqv_pt1)
                if count != number_cols:
                    columns_list.append(", ")
            columns_string = "".join(columns_list)

        if matchexact is True:
            sqs_pt2 = " FROM %s WHERE %s = %s" % (
                str(tbl_name), str(match_col), str(search_term))
        else:
            sqs_pt2 = " FROM %s WHERE %s LIKE \%%s\%" % (
                str(tbl_name), str(match_col), str(search_term))

        sql_query = sqs_pt1 + columns_string + sqs_pt2
        return sql_query

    def find_greater(
            self,
            tbl_name,
            match_col,
            compare_term,
            columns_list="*"):

        if isinstance(columns_list, str):
            sqv_pt1 = "SELECT %s " % (columns_list)
        else:
            columns_string = ", ".join(columns_list)
            sqv_pt1 = "SELECT %s " % (columns_string)

        sqs_pt1 = "FROM %s WHERE %s > %s" % (
            tbl_name, match_col, compare_term)

        sql_query = sqv_pt1 + sqs_pt1
        return sql_query

    def find_lesser(self, tbl_name, match_col, compare_term, columns_list="*"):

        if isinstance(columns_list, str):
            sqv_pt1 = "SELECT %s " % (columns_list)
        else:
            columns_string = ", ".join(columns_list)
            sqv_pt1 = "SELECT %s " % (columns_string)

        sqs_pt1 = "FROM %s WHERE %s < %s" % (
            tbl_name, match_col, compare_term)

        sql_query = sqv_pt1 + sqs_pt1
        return sql_query

    def table_join(self, table1_name, table2_name, common_col):
        sqs_pt1 = "SELECT * FROM %s, %s" % (
            table1_name, table2_name)
        sqs_pt2 = "WHERE %s.%s = %s.%s" % (
            table1_name, common_col, table2_name, common_col)

        sql_query = sqs_pt1 + sqs_pt2
        return sql_query

    def count_records(self, tbl_name, col_name="*"):
        sql_query = "SELECT COUNT(%s) FROM %s" % (col_name, tbl_name)
        return sql_query

    def get_max(self, tbl_name, col_name):
        sql_query = "SELECT MAX(%s) FROM %s" % (col_name, tbl_name)
        return sql_query

    def get_min(self, tbl_name, col_name):
        sql_query = "SELECT MIN(%s) FROM %s" % (col_name, tbl_name)
        return sql_query
