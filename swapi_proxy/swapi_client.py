import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from django.conf import settings

# Use http instead of https to avoid SSL issues
BASE_URL = 'http://swapi.dev/api/'

class SWAPIClient:
    @staticmethod
    def _get_session():
        """Create a session with retry logic"""
        session = requests.Session()
        retries = Retry(
            total=3,
            backoff_factor=0.5,
            status_forcelist=[500, 502, 503, 504],
        )
        session.mount('http://', HTTPAdapter(max_retries=retries))
        return session

    @classmethod
    def search_people(cls, query):
        """Search for Star Wars characters by name"""
        session = cls._get_session()
        try:
            response = session.get(
                f"{BASE_URL}people/",
                params={"search": query},
                verify=False  # Skip SSL verification
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}
        finally:
            session.close()
