-- SQL script that creates a trigger that decreases the quantity of an item after adding a new order
CREATE TRIGGER quan_item AFTER INSERT ON orders
    FOR EACH ROW SET item.quantity = item.quantity - orders.number;
