# se crea una clase query, para que contenga los petodos para hacer
# las consultas necesarias para el sistema.

class Query():
    def __init__(self, con):
        self._con = con
        self._cursor = con.cursor()

    def email_registered(self, email):
        query = f"""
            select eMail from email where eMail={email!r};
        """
        try:
            response = self._cursor.execute(query)
            response = response.fetchall()[0][0]
            return True
        except IndexError:
            return False

    def get_email_id(self, email):
        query = f"""
            select eMailId from email where eMail={email!r}
        """
        response = self._cursor.execute(query)
        response = response.fetchall()
        return response

    def get_password_id(self, password):
        query = f"""
            select passId from password where password={password!r}
        """
        response = self._cursor.execute(query)
        response = response.fetchall()[0][0]
        return response

    def get_password_id_from_email(self, email):
        query = f"""
            select passId from email where eMail={email!r}
        """
        response = self._cursor.execute(query)
        response = response.fetchone()[0]
        return response

    def get_password(self, pass_id):
        query = f"""
            select password from password where passId={pass_id}
        """
        response = self._cursor.execute(query)
        response = response.fetchall()[0][0]
        return response

    def insert_user(self, user_data):
        password = f"""
            insert into password (password) values(
                {user_data["password"]!r}
            )
        """
        self._cursor.execute(password)
        self._con.commit()
        pass_id = self.get_password_id(user_data["password"])
        email = f"""
            insert into email (email, passId) values (
                {user_data["email"]!r},
                {pass_id}
            )
        """
        self._cursor.execute(email)
        self._con.commit()
        email_id = self.get_email_id(user_data["email"])
        user = f"""
            insert into user (nombre, apellidoP, apellidoM, eMailId) values(
                {user_data["name"]!r},
                {user_data["a_paterno"]!r},
                {user_data["a_materno"]!r},
                {email_id}
            )
        """
        self._cursor.execute(user)
        self._con.commit()
