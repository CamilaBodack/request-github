import unittest
from .github_user import GithubUser
from .requests_utils import get_username


class TestGithubUser(unittest.TestCase):

    """
    Testes unitários da classe GithubUser
    """

    def setUp(self):
        username = "torvalds"
        github_user_data = get_username(username)
        self.github_user = GithubUser(
            github_user_data["id"],
            github_user_data["avatar_url"],
            github_user_data["name"],
            github_user_data["email"],
            github_user_data["created_at"],
        )

    def test_user_id(self):
        expected = 1024025
        self.assertEqual(expected, self.github_user.user_id)

    def test_avatar(self):
        expected = "https://avatars.githubusercontent.com/u/1024025?v=4"
        self.assertEqual(expected, self.github_user.avatar)

    def test_name(self):
        expected = "Linus Torvalds"
        self.assertEqual(expected, self.github_user.name)

    def test_email(self):
        expected = None
        self.assertEqual(expected, self.github_user.email)

    def test_created_at(self):
        expected = "2011-09-03T15:26:22Z"
        self.assertEqual(expected, self.github_user.created_at)
