#
# Copyright (c) 2014 NSONE, Inc.
#
# License under The MIT License (MIT). See LICENSE in project root.
#

from . import resource


class RemoteServers(resource.BaseResource):

    ROOT = "dhcp/ddns/remoteserver"

    BOOL_FIELDS = []
    INT_FIELDS = [
        "mname_port",
        "kdc_port"
        "principal_id"
    ]
    PASSTHRU_FIELDS = [
        "mname_server",
        "kdc_server",
        "update_security_level",
        "tsig_key"
    ]

    def list(self, callback=None, errback=None):
        return self._make_request(
            "GET", "%s" % self.ROOT, callback=callback, errback=errback,
        )

    def retrieve(self, rs_id, callback=None, errback=None):
        return self._make_request(
            "GET",
            "%s/%s" % (self.ROOT, rs_id),
            callback=callback,
            errback=errback,
        )

    def create(self, callback=None, errback=None, **kwargs):
        body = {}
        self._buildStdBody(body, kwargs)
        return self._make_request(
            "PUT",
            "%s" % self.ROOT,
            body=body,
            callback=callback,
            errback=errback,
        )

    def update(self, rs_id, callback=None, errback=None, **kwargs):
        body = {}
        self._buildStdBody(body, kwargs)
        return self._make_request(
            "POST",
            "%s/%s" % (self.ROOT, rs_id),
            body=body,
            callback=callback,
            errback=errback,
        )

    def delete(self, rs_id, callback=None, errback=None):
        return self._make_request(
            "DELETE",
            "%s/%s" % (self.ROOT, rs_id),
            callback=callback,
            errback=errback,
        )
