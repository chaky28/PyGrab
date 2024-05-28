import copy
import time as t
import pandas as pd
import os
import json
from pygr.dal import DataBase


def get_all_column_names(definition, columns):
    for item in definition.get("items", []):
        if item.get("item_type") == "item_list":
            get_all_column_names(item, columns)
        if item.get("item_type") == "grabber":
            name = item.get("item_name", "")
            if name not in columns:
                columns.append(name)


def check_exporter_queue(*args):
    exporter = args[0]
    while True:
        t.sleep(1)
        if exporter.is_there_items_to_export():
            process_export(exporter.get_first_in_queue())
            exporter.remove_first_from_queue()


def process_export(data):
    result = []
    db = DataBase(data.db_location)
    for key, value in data.data.items():
        if "#EXPORT" in key:
            export_result = {}
            path = key.split("_")
            for i in range(len(path)):
                iterator = 0
                sub_path = ""
                while iterator <= i:
                    sub_path += path[iterator]
                    if iterator < i:
                        sub_path += "_"
                    iterator += 1
                for column in data.data[sub_path]:
                    export_result = {**export_result, **column}
            result.append(export_result)
    if not db.does_table_exists(data.run_name):
        initialize_table(db, data)
    db.insert_into_table(data.run_name, format_export_result_for_db(result, data))

    if data.do_export:
        db.print_table(data.run_name)
        df = pd.read_sql_query(f"SELECT * FROM {data.run_name}", db.get_connection())
        df.to_excel(f"{data.run_name}.xlsx")
        db.drop_table(data.run_name)


def format_export_result_for_db(results, data):
    formatted_export = []
    for result in results:
        formatted_export.append(tuple(result.get(column_name, "") for column_name in data.column_names))
    return formatted_export


def initialize_table(db, data):
    columns = {}
    for column_name in data.column_names:
        columns[column_name] = "TEXT"
        print(columns)
    db.initialize_table(data.run_name, columns)


def get_json_to_export(data):
    return data


def has_no_list_children(data):
    for item in data:
        if type(item) is list:
            return False
    return True
