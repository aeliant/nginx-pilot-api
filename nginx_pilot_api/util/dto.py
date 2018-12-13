"""Data Transfer Object file, regrouping all DTO objects used in controller."""
from flask_restplus import Namespace, fields, model

hash = model('upstream-hash', {
    'key': fields.String(description='Upstream hash\'s key'),
    'consistent': fields.Boolean(description='Upstream hash\'s consistency')
})

upstream_least_time = model('upstream-least-time', {
    'header': fields.Boolean(description='Upstrea least time header'),
    'last_byte': fields.Boolean(description='Upstream last byte'),
    'inflight': fields.Boolean(description='Upstream inflight')
})

upstream = model('upstream', {
    'name': fields.String(description='Upstream name directive'),
    'servers': fields.List(description='Upstream servers directive'),
    'zone': fields.String(description='Upstream zone directive'),
    'state': fields.String(description='Upstream state directive'),
    'hash': fields.Nested(hash, description='Upstream hash directive'),
    'ip_hash': fields.Boolean(description='Upstream ip_hash directive'),
    'keepalive': fields.Integer(description='Upstream keepalive directive'),
    'keepalive_requests': fields.Integer(
        description='Upstream keepalive requests number directive'),
    'keepalive_timeout': fields.String(
        description='Upstream keepalive timeout directive'),
    'ntlm': fields.Boolean(description='Upstream ntlm directive'),
    'least_conn': fields.Boolean(description='Upstream least_conn directive'),
    'least_time': fields.Nested(upstream_least_time, description='Upstream'),
    'queue': fields.String(description='Upstream'),
    'random': fields.String(description='Upstream'),
    'sticky': fields.String(description='Upstream'),
})


class SiteAvailableDto:
    """Site available data transfer object, used for api marashalling and
    documentation.
    """

    api = Namespace('site-available',
                    description='sites available related operations')

    available_site = api.model('site-available', {
        'id': fields.String(description='Avaiable site public identifier'),
        'name': fields.String(description='Name of the available site.',
                              required=True),
        'upstreams': fields.List(),

    })
