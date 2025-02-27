import pytest
from .connect_to_db import connect_db, create_table, insert_item, update_item, delete_item, select_items


@pytest.fixture(scope="module")
def db_connection():
    conn = connect_db()
    create_table(conn)
    yield conn
    conn.close()


def test_insert_item(db_connection):
    insert_item(db_connection, "Test Item")
    items = select_items(db_connection)
    assert any(item[1] == "Test Item" for item in items)


def test_update_item(db_connection):
    insert_item(db_connection, "Old Item")
    update_item(db_connection, 1, "Updated Item")
    items = select_items(db_connection)
    assert any(item[1] == "Updated Item" for item in items)


def test_delete_item(db_connection):
    insert_item(db_connection, "Item to Delete")
    items_before_delete = select_items(db_connection)
    assert any(item[1] == "Item to Delete" for item in items_before_delete)

    item_id_to_delete = next(item[0] for item in items_before_delete if item[1] == "Item to Delete")

    delete_item(db_connection, item_id_to_delete)
    items_after_delete = select_items(db_connection)
    assert not any(item[1] == "Item to Delete" for item in items_after_delete)
