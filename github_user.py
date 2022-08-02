class GithubUser:
    """
    Classe que representa um usuário do Github e alguns de seus atributos.
    """

    def __init__(self, user_id, avatar, name, email, created_at):
        self.user_id = user_id
        self.avatar = avatar
        self.name = name
        self.email = email
        self.created_at = created_at
