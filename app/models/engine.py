from sqlalchemy import create_engine

import os.path

from config import BASE_DIR

db_path = os.path.join(BASE_DIR, "myapp.db")

engine = create_engine(f"sqlite:///{db_path}")
# engine = create_engine(DB_URL)
