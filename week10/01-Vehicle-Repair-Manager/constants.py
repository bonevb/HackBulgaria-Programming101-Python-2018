insert_base_user = """
INSERT INTO BASE_USER (user_name, email, phone_number, address, type)
 VALUES (:user_name, :email, :phone_number, :address, :type
 )
"""

insert_client_id = """
INSERT INTO CLIENT  VALUES (?)
"""


if_user_exists = """
SELECT USER_NAME FROM BASE_USER WHERE USER_NAME=?
"""

insert_vehicle = """
INSERT INTO VEHICLE (category, make, model, register_number, gear_box, owner) VALUES
 (:category, :make, :model, :register_number, :gear_box, :owner)
"""

select_vehicle = """
SELECT * FROM VEHICLE WHERE OWNER = ?
"""
update_vehicle = """
UPDATE VEHICLE SET (category, make, model, register_number, gear_box, owner) WHERE ID = id
"""

save_repair_hour = """
UPDATE REPAIR_HOURS SET VEHICLE=?, MECHANIC_SERVICE=? WHERE ID=?
"""

choose_repair_hours = """
SELECT * FROM REPAIR_HOURS WHERE VEHICLE = (SELECT ID FROM VEHICLE JOIN CLIENT ON ? = CLIENT.BASE_ID)
"""
# SELECT * FROM REPAIR_HOURS WHERE ID=(SELECT ID FROM VEHICLE JOIN CLIENT WHERE (SELECT id FROM VEHICLE WHERE OWNER=?)=CLIENT.BASE_ID)
