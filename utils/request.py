# from django.conf import settings
import requests
import logging
from .encode import make_signature, http_date
# import environ
# from .bot import Bot
# import os
from conf import settings
from json.decoder import JSONDecodeError
from requests.exceptions import ConnectionError
from .jfile import JsonFile, AccessKeyFile
from .url import API_URL_MAPPING

logger = logging.getLogger(__name__)


def _appRegistration(comment):
    jf = JsonFile()

    headers = {
        'Authorization': f'{settings.BOOTSTRAP_TOKEN}',
    }
    url = f"{settings.API_URL}{API_URL_MAPPING['terminal-registrations']}"
    r = requests.post(url, headers=headers, data={'name': settings.BOOTSTRAP_NAME, 'comment': comment})

    data = r.json()
    if r.status_code == 201:
        jf.data = data['service_account']['access_key']
        jf.save()
    elif r.status_code == 401:
        pass

    return data


def appRegistration(comment='bot'):
    ret = _appRegistration(comment)
    print(ret)


def _request(method, uri, pk, **kwargs) -> dict:
    ak = AccessKeyFile()

    request_date = http_date().encode()
    signature = make_signature(ak.API_SECRET, request_date)
    headers = {
        'Authorization': f'{settings.API_KEYWORD} {ak.API_ID}:{signature}',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0',
        'DATE': request_date,
        'content-type': 'application/json',
    }

    ret = {'code': 0, 'data': '', 'message': ''}

    _uri = API_URL_MAPPING.get(uri)
    if not uri:
        ret['code'] = 1
        ret['message'] = f"URL 錯誤 {uri}"

    if pk and '%s' in _uri:
        _uri = _uri % pk

    url = f"{settings.API_URL}{_uri}"
    logger.debug(url)
    # print(url)

    try:

        req = requests.api.request(method=method, url=url, timeout=300, headers=headers, **kwargs)

        if req.status_code in [200, 201]:
            print(req.status_code)
            ret = req.json()
        else:
            ret['code'] = req.status_code
            ret['message'] = f'Response {req.status_code}'

    except JSONDecodeError:
        ret['code'] = 1
        ret['message'] = '獲取json出錯'
    except ConnectionError:
        ret['code'] = 1
        print(f'連接超時 {url}')
        ret['message'] = f'連接超時，請稍後再試'
    except Exception as e:
        ret['code'] = 1
        ret['message'] = f'未知錯誤 {e} {type(e)}'

    return ret


def get(url, pk=None, params=None, **kwargs) -> dict:
    r"""Sends a GET request.

    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string for the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    return _request('get', url, pk, params=params, **kwargs)


def post(url, pk=None, data=None, json=None, **kwargs) -> dict:
    r"""Sends a POST request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) json data to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    return _request('post', url, pk, data=data, json=json, **kwargs)


def put(url, pk=None, data=None, **kwargs) -> dict:
    r"""Sends a PUT request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) json data to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    return _request('put', url, pk, data=data, **kwargs)


def delete(url, pk=None, **kwargs):
    r"""Sends a DELETE request.

    :param url: URL for the new :class:`Request` object.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    return _request('delete', url, pk, **kwargs)
