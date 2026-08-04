from qdivzero_py.client import AuthenticatedClient


def test_client_imports() -> None:
    client = AuthenticatedClient(base_url="https://api.qdiv0.com", token="test")
    assert client._base_url == "https://api.qdiv0.com"
    assert client.token == "test"
