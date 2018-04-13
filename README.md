# apistar_request_id

Request id generation and propagation for [API Star].


## Requirements

* [API Star] 0.4+


## Installation

Use [pipenv] (or plain pip) to install the package:

    pipenv install apistar_request_id


## Usage

```python
from apistar import App
from apistar_request_id import RequestIdHooks


routes = [
    ...
]

event_hooks = [RequestIdHooks()]

app = App(routes=routes, event_hooks=event_hooks)
```

All responses will automatically include an `x-request-id` header once
you do this.  The request id is inherited from the request if an
`x-request-id` header is set, otherwise one is automatically generated
from a uuid.

If you need to access the current request id from application code,
you can do so via the `RequestId` class:

``` python
from apistar_request_id import RequestId

print(RequestId.get_request_id())
```

Request ids are thread-local.

## License

apistar_request_id is licensed under Apache 2.0.  Please see [LICENSE]
for licensing details.


[API Star]: https://github.com/encode/apistar/
[pipenv]: https://docs.pipenv.org
[LICENSE]: https://github.com/Bogdanp/apistar_request_id/blob/master/LICENSE
