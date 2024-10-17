from urllib.parse import urlparse
from http.client import HTTPResponse

def redirect_url(url: str) -> HTTPResponse:
    parsed_url = urlparse(url)
    domain_name = parsed_url.netloc

    if domain_name == 'example.com':
        # Perform the redirection (this is a placeholder, actual redirection logic will depend on the framework)
        return HTTPResponse(status=302, reason='Found', body='Redirecting to example.com')
    else:
        # Return a 404 error
        return HTTPResponse(status=404, reason='Not Found', body='The requested URL was not found on this server')