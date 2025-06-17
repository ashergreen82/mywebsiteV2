import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from django.conf import settings
from urllib.parse import urljoin

class SWAPIClient:
    BASE_URL = 'https://swapi.dev/api/'
    
    @staticmethod
    def _get_session():
        """Create a session with retry logic"""
        session = requests.Session()
        retries = Retry(
            total=3,
            backoff_factor=0.5,
            status_forcelist=[500, 502, 503, 504],
        )
        session.mount('https://', HTTPAdapter(max_retries=retries))
        return session

    @classmethod
    def search_people(cls, query):
        """Search for Star Wars characters by name"""
        session = cls._get_session()
        try:
            response = session.get(
                urljoin(cls.BASE_URL, 'people/'),
                params={"search": query},
                verify=False  # Disable SSL verification
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error searching people: {str(e)}")
            return {"error": "Failed to fetch data from SWAPI. Please try again later."}
        finally:
            session.close()
            
    @classmethod
    def get_resource(cls, url):
        """Get a SWAPI resource by URL"""
        session = cls._get_session()
        try:
            # Convert SWAPI URL to use our proxy if it's a direct SWAPI URL
            if url.startswith('https://swapi.dev/api/'):
                path = url.replace('https://swapi.dev/api/', '')
                url = urljoin(cls.BASE_URL, path)
                
            response = session.get(url, verify=False)  # Disable SSL verification
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching resource {url}: {str(e)}")
            return {"error": "Failed to fetch resource from SWAPI. Please try again later."}
        finally:
            session.close()
