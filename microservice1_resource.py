

import pymysql


class MicroService1:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        usr = "admin"
        pw = "team_lol"
        h = "database-lol.chy7cu9rusdl.us-east-2.rds.amazonaws.com"

        conn = pymysql.connect(
            user=usr,
            password=pw,
            host=h,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn


    @staticmethod
    def get_location_by_name(item_name):

        sql = """SELECT type_id FROM microService_1.Map where item_name= %s"""
        key = [item_name]
        conn = MicroService1._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchall()
        type_id = result[0]['type_id']

        sql = """SELECT type_name FROM microService_1.Type_Name where type_id= %s"""

        key = [type_id]
        conn = MicroService1._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchall()
        type_name = result[0]['type_name']

        sql = """SELECT item_id FROM microService_1.Map where item_name= %s"""
        key = [item_name]
        conn = MicroService1._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchall()
        item_id = result[0]['item_id']

        if item_id >= 60000000:
            sql = """SELECT solar_system_id, constellation_id, region_id  FROM microService_1.Map where item_id= %s"""
            key = [item_id]
            conn = MicroService1._get_connection()
            cur = conn.cursor()
            res = cur.execute(sql, args=key)
            result = cur.fetchall()
            solar_system_id = result[0]['solar_system_id']
            constellation_id = result[0]['constellation_id']
            region_id = result[0]['region_id']

            sql = """SELECT item_name  FROM microService_1.Map where item_id= %s"""
            key = [solar_system_id]
            conn = MicroService1._get_connection()
            cur = conn.cursor()
            res = cur.execute(sql, args=key)
            result = cur.fetchall()
            solar_system_name=result[0]['item_name']

            sql = """SELECT item_name  FROM microService_1.Map where item_id= %s"""
            key = [constellation_id]
            conn = MicroService1._get_connection()
            cur = conn.cursor()
            res = cur.execute(sql, args=key)
            result = cur.fetchall()
            constellation_name = result[0]['item_name']

            sql = """SELECT item_name  FROM microService_1.Map where item_id= %s"""
            key = [region_id]
            conn = MicroService1._get_connection()
            cur = conn.cursor()
            res = cur.execute(sql, args=key)
            result = cur.fetchall()
            region_name = result[0]['item_name']
            return type_name, solar_system_name, constellation_name, region_name

        elif 40000000> item_id >= 30000000:
            sql = """SELECT constellation_id, region_id  FROM microService_1.Map where item_id= %s"""
            key = [item_id]
            conn = MicroService1._get_connection()
            cur = conn.cursor()
            res = cur.execute(sql, args=key)
            result = cur.fetchall()
            constellation_id = result[0]['constellation_id']
            region_id = result[0]['region_id']

            sql = """SELECT item_name  FROM microService_1.Map where item_id= %s"""
            key = [constellation_id]
            conn = MicroService1._get_connection()
            cur = conn.cursor()
            res = cur.execute(sql, args=key)
            result = cur.fetchall()
            constellation_name = result[0]['item_name']

            sql = """SELECT item_name  FROM microService_1.Map where item_id= %s"""
            key = [region_id]
            conn = MicroService1._get_connection()
            cur = conn.cursor()
            res = cur.execute(sql, args=key)
            result = cur.fetchall()
            region_name = result[0]['item_name']



#children station
            sql = """SELECT item_name  FROM microService_1.Map where solar_system_id= %s and item_id >= 60000000"""
            key = [item_id]
            conn = MicroService1._get_connection()
            cur = conn.cursor()
            res = cur.execute(sql, args=key)
            stations = cur.fetchall()

            return type_name, stations, constellation_name, region_name

        elif 30000000> item_id >= 20000000:
            sql = """SELECT  region_id  FROM microService_1.Map where item_id= %s"""
            key = [item_id]
            conn = MicroService1._get_connection()
            cur = conn.cursor()
            res = cur.execute(sql, args=key)
            result = cur.fetchall()
            region_id = result[0]['region_id']


            sql = """SELECT item_name  FROM microService_1.Map where item_id= %s"""
            key = [region_id]
            conn = MicroService1._get_connection()
            cur = conn.cursor()
            res = cur.execute(sql, args=key)
            result = cur.fetchall()
            region_name = result[0]['item_name']

# children system
            sql = """SELECT item_name  FROM microService_1.Map where (constellation_id= %s and 40000000 > item_id and item_id >= 30000000)"""
            key = [item_id]
            conn = MicroService1._get_connection()
            cur = conn.cursor()
            res = cur.execute(sql, args=key)
            systems = cur.fetchall()

# children station
            sql = """SELECT item_name  FROM microService_1.Map where constellation_id= %s and item_id >= 60000000"""
            key = [item_id]
            conn = MicroService1._get_connection()
            cur = conn.cursor()
            res = cur.execute(sql, args=key)
            stations = cur.fetchall()

            return type_name, stations, systems, region_name

        elif 20000000 > item_id >= 10000000:

# children constellation
            sql = """SELECT item_name  FROM microService_1.Map where region_id= %s and 30000000 > item_id and item_id >= 20000000"""
            key = [item_id]
            conn = MicroService1._get_connection()
            cur = conn.cursor()
            res = cur.execute(sql, args=key)
            constellations = cur.fetchall()


# children system
            sql = """SELECT item_name  FROM microService_1.Map where region_id= %s and 40000000 > item_id and item_id >= 30000000"""
            key = [item_id]
            conn = MicroService1._get_connection()
            cur = conn.cursor()
            res = cur.execute(sql, args=key)
            systems = cur.fetchall()

# children station
            sql = """SELECT item_name  FROM microService_1.Map where region_id= %s and item_id >= 60000000"""
            key = [item_id]
            conn = MicroService1._get_connection()
            cur = conn.cursor()
            res = cur.execute(sql, args=key)
            stations = cur.fetchall()

            return type_name, stations, systems, constellations




    @staticmethod
    def get_security_by_name(item_name):
        sql = """SELECT security FROM microService_1.Map where item_name= %s"""
        key = [item_name]
        conn = MicroService1._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchall()
        security = result[0]['security']

        return security

    @staticmethod
    def get_stations_by_id(item_id):

        sql = """SELECT item_name FROM microService_1.Map where item_id= %s"""
        key = [item_id]
        conn = MicroService1._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchall()
        item_name = result[0]['item_name']

        if int(item_id) > 60000000:
            return item_id, item_name, 4, [{"station_id":item_id, "station_name":item_name}]
        elif 40000000 > int(item_id) > 30000000:

            sql = """SELECT item_name as station_id, item_id as station_name FROM microService_1.Map where solar_system_id= %s and item_id >= 60000000"""
            key = [item_id]
            conn = MicroService1._get_connection()
            cur = conn.cursor()
            res = cur.execute(sql, args=key)
            stations = cur.fetchall()

            return item_id, item_name, 3, stations
        elif 30000000 > int(item_id) > 20000000:

            sql = """SELECT item_name as station_id, item_id as station_name FROM microService_1.Map where constellation_id= %s and item_id >= 60000000"""
            key = [item_id]
            conn = MicroService1._get_connection()
            cur = conn.cursor()
            res = cur.execute(sql, args=key)
            stations = cur.fetchall()

            return item_id, item_name, 2, stations
        elif 20000000 > int(item_id) > 10000000:

            sql = """SELECT item_name as station_id, item_id as station_name FROM microService_1.Map where region_id= %s and item_id >= 60000000"""
            key = [item_id]
            conn = MicroService1._get_connection()
            cur = conn.cursor()
            res = cur.execute(sql, args=key)
            stations = cur.fetchall()

            return item_id, item_name, 1, stations

    @staticmethod
    def get_station_parent_by_id(item_id):

        sql = """SELECT item_name, security, solar_system_id, constellation_id, region_id FROM microService_1.Map where item_id= %s"""
        key = [item_id]
        conn = MicroService1._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchall()
        item_name = result[0]['item_name']
        security = result[0]['security']
        solar_system_id = result[0]['solar_system_id']
        constellation_id = result[0]['constellation_id']
        region_id = result[0]['region_id']

        sql = """SELECT item_name FROM microService_1.Map where item_id= %s"""
        key = [solar_system_id]
        conn = MicroService1._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchall()
        solar_system_name = result[0]['item_name']

        sql = """SELECT item_name FROM microService_1.Map where item_id= %s"""
        key = [constellation_id]
        conn = MicroService1._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchall()
        constellation_name = result[0]['item_name']
        sql = """SELECT item_name FROM microService_1.Map where item_id= %s"""
        key = [region_id]
        conn = MicroService1._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchall()
        region_name = result[0]['item_name']

        return item_id, item_name, security, solar_system_name, solar_system_id, constellation_name, constellation_id, region_name, region_id









#e=MicroService1.get_stations_by_name("20000375")
#print(e)
f= MicroService1.get_station_parent_by_id("60000025")
print(f)
# print(e)
# a,b,c,d=MicroService1.get_location_by_name("Kor-Azor")
# print(a)
# print(b[0])
# print(c)
# print(d)
#
# print(MicroService1.get_security_by_name("HE-V4V"))

