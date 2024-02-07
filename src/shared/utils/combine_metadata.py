from collections.abc import Iterable

from sqlalchemy import MetaData


def combine_metadata(metadata_list: Iterable[MetaData]) -> MetaData:
    combined_metadata = MetaData()

    for metadata in metadata_list:
        for table_name, table in metadata.tables.items():
            combined_metadata._add_table(  # noqa
                table_name, table.schema, table
            )

    return combined_metadata
