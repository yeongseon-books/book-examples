# 5_eager.py
from sqlalchemy.orm import selectinload
stmt = select(Order).options(selectinload(Order.items))
orders = session.scalars(stmt).all()
