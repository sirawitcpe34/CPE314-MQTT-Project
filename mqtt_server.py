"""
MQTT Server subscribes for data from Client. 

- The received data is assembled as necessary and written in the local database (e.g., MySQL, PostgreSQL) for later query or visualization. 
- Data sent in the same round from Client must be stored in the same database record. 
- Any lost data would result in missing values in the database records.

Constraints:
- server prints out received messages from Broker on the screen.
- At Server, one must be able to query data of each sensor separately from the database.
- Multiple IoT nodes and servers can be deployed in the system. If Server subscribes data from several clients, all the data is stored in the same database table.
"""