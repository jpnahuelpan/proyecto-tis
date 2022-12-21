# se crea una clase query, para que contenga los petodos para hacer
# las consultas necesarias para el sistema.

class Query():
    def __init__(self, cursor):
        self._cursor = cursor

    def email_registered(self, email):
        query = f"""
            select eMail from email where eMail='{email}';
        """
        response = self._cursor.execute(query)
        response = response.fetchall()[0][0]
        if response:
            return True
        else:
            return False

    def get_password_id(self, email):
        query = f"""
            select eMailId from email where eMail='{email}';
        """
        response = self._cursor.execute(query)
        response = response.fetchall()[0][0]
        return response

    def get_password(self, pass_id):
        query = f"""
            select password from password where passId={pass_id};
        """
        response = self._cursor.execute(query)
        response = response.fetchall()[0][0]
        return response
