from uuid import uuid4

from apistar import http
from threading import local
from typing import Optional

__all__ = ["RequestId", "RequestIdHooks", "__version__"]
__version__ = "0.1.0"


class RequestId:
    STATE = local()

    @classmethod
    def get_request_id(cls) -> Optional[str]:
        """Retrieves the request id for the current thread.
        """
        return getattr(cls.STATE, "request_id", None)

    @classmethod
    def set_request_id(cls, request_id: str = None) -> str:
        """Set a request id for the current thread.  Leave the
        request_id parameter empty to generate a random id.
        """
        if request_id is None:
            request_id = str(uuid4())

        cls.STATE.request_id = request_id
        return request_id

    @classmethod
    def clear_request_id(cls) -> None:
        """Clear the request id for the current thread.
        """
        try:
            del cls.STATE.request_id
        except AttributeError:  # pragma: no cover
            pass


class RequestIdHooks:
    def on_request(self, x_request_id: http.Header = None) -> None:
        RequestId.set_request_id(x_request_id)

    def on_response(self, response: http.Response) -> http.Response:
        response.headers["x-request-id"] = RequestId.get_request_id()
        RequestId.clear_request_id()
        return response

    def on_error(self, response: http.Response, x_request_id: http.Header = None) -> http.Response:
        RequestId.set_request_id(x_request_id)
        response.headers["x-request-id"] = RequestId.get_request_id()
        RequestId.clear_request_id()
        return response
