from django.db import connection


def calculate_db_queries() -> None:
    """
    Função de utilidade que printa o tempo levado 
    pras queries e o número de queries feitas
    """

    sqltime = 0.0
    for query in connection.queries:
        sqltime += float(query["time"])
    print("Page render: " + str(sqltime) + "sec for " +
          str(len(connection.queries)) + " queries")
