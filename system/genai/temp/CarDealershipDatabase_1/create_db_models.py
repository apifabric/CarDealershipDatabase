# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py

from sqlalchemy.dialects.sqlite import *


class Car(Base):\n    \n    __tablename__ = 'car'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    make = Column(String, nullable=False)\n    model = Column(String, nullable=False)\n    year = Column(Integer, nullable=False)\n    mileage = Column(Integer, nullable=True)\n    price = Column(DECIMAL(10, 2), nullable=False)\n    color = Column(String, nullable=True)\n


class Customer(Base):\n    \n    __tablename__ = 'customer'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    first_name = Column(String, nullable=False)\n    last_name = Column(String, nullable=False)\n    phone_number = Column(String, nullable=True)\n    email = Column(String, nullable=True)\n


class Salesperson(Base):\n    \n    __tablename__ = 'salesperson'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    first_name = Column(String, nullable=False)\n    last_name = Column(String, nullable=False)\n    hire_date = Column(DateTime, nullable=True)\n    salary = Column(DECIMAL(10, 2), nullable=False)\n


class Invoice(Base):\n    \n    __tablename__ = 'invoice'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    date = Column(DateTime, nullable=False)\n    total_amount = Column(DECIMAL(10, 2), nullable=False)\n    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False) \n    salesperson_id = Column(Integer, ForeignKey('salesperson.id'), nullable=False)\n


class Inventory(Base):\n\n    __tablename__ = 'inventory'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    car_id = Column(Integer, ForeignKey('car.id'), nullable=False)\n    quantity = Column(Integer, nullable=False)\n


class Sale(Base):\n    \n    __tablename__ = 'sale'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    invoice_id = Column(Integer, ForeignKey('invoice.id'), nullable=False)\n    car_id = Column(Integer, ForeignKey('car.id'), nullable=False)\n    sale_price = Column(DECIMAL(10, 2), nullable=False)\n


class ServiceAppointment(Base):\n    \n    __tablename__ = 'service_appointment'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    date = Column(DateTime, nullable=False)\n    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)\n    car_id = Column(Integer, ForeignKey('car.id'), nullable=False)\n


class TestDrive(Base):\n    \n    __tablename__ = 'test_drive'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    date = Column(DateTime, nullable=False)\n    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)\n    car_id = Column(Integer, ForeignKey('car.id'), nullable=False)\n


class Payment(Base):\n    \n    __tablename__ = 'payment'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    invoice_id = Column(Integer, ForeignKey('invoice.id'), nullable=False)\n    amount = Column(DECIMAL(10, 2), nullable=False)\n    date = Column(DateTime, nullable=False)\n


class AutoPart(Base):\n    \n    __tablename__ = 'auto_part'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    name = Column(String, nullable=False)\n    price = Column(DECIMAL(10, 2), nullable=False)\n    stock = Column(Integer, nullable=False)\n


class PartPurchase(Base):\n    \n    __tablename__ = 'part_purchase'\n\n    id = Column(Integer, primary_key=True, autoincrement=True)\n    auto_part_id = Column(Integer, ForeignKey('auto_part.id'), nullable=False)\n    quantity = Column(Integer, nullable=False)\n    date = Column(DateTime, nullable=False)\n


# end of model classes


try:
    
    
    
    
    # ALS/GenAI: Create an SQLite database
    
    engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    
    Base.metadata.create_all(engine)
    
    
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    
    
    # ALS/GenAI: Prepare for sample data
    
    
    
    session.commit()
    car1 = Car(make="Toyota", model="Camry", year=2020, mileage=10000, price=20000.00, color="Red")
    car2 = Car(make="Honda", model="Civic", year=2019, mileage=15000, price=18000.00, color="Blue")
    car3 = Car(make="Ford", model="Focus", year=2021, mileage=5000, price=22000.00, color="Black")
    car4 = Car(make="Chevrolet", model="Impala", year=2018, mileage=20000, price=17000.00, color="Silver")
    customer1 = Customer(first_name="John", last_name="Doe", phone_number="555-1234", email="john.doe@example.com")
    customer2 = Customer(first_name="Jane", last_name="Smith", phone_number="555-5678", email="jane.smith@example.com")
    customer3 = Customer(first_name="Emily", last_name="Johnson", phone_number="555-8765", email="emily.johnson@example.com")
    customer4 = Customer(first_name="Michael", last_name="Brown", phone_number="555-4321", email="michael.brown@example.com")
    salesperson1 = Salesperson(first_name="Alice", last_name="Williams", hire_date=date(2020, 5, 10), salary=50000.00)
    salesperson2 = Salesperson(first_name="Thomas", last_name="Taylor", hire_date=date(2019, 4, 20), salary=55000.00)
    salesperson3 = Salesperson(first_name="Olivia", last_name="Martinez", hire_date=date(2018, 3, 5), salary=60000.00)
    salesperson4 = Salesperson(first_name="Paul", last_name="Jackson", hire_date=date(2021, 1, 25), salary=45000.00)
    invoice1 = Invoice(date=date(2023, 10, 12), total_amount=20000.00, customer_id=customer1.id, salesperson_id=salesperson1.id)
    invoice2 = Invoice(date=date(2023, 10, 13), total_amount=18000.00, customer_id=customer2.id, salesperson_id=salesperson2.id)
    
    
    
    session.add_all([car1, car2, car3, car4, customer1, customer2, customer3, customer4, salesperson1, salesperson2, salesperson3, salesperson4, invoice1, invoice2])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
