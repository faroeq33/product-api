
import csv
from app.utils import crud
from app.utils import models

from app.utils.models import Product
from app.main import create_product, get_db


def insert_test_data():

    db = get_db()
    # Put code here to insert test data
    with open("/home/faroeq33/code/product-api/tests/helpers/test_data_products.csv", newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            crud.create_user_product(db=db, product=row)
