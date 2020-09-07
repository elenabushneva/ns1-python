"""
DNS views example

Settiing up "internal" and "external" views of a zone
"""

from base64 import b64encode

from ns1 import NS1

client = NS1()

# The resources we will be using
tsig = client.tsig()
remote_server = client.remote_server()

tsig_key = "tsig"
remote_server_id = 0


def run():

    # we'll use tsig in our remote server
    tsig_internal = tsig.create(
        tsig_key,
        algorithm="hmac-sha512",
        secret=b64encode(b"example-secret").decode(),
    )

    remote_server_internal = remote_server.create(
        mname_server='remote-server',
        mname_port=53,
        tsig_key=f'{tsig_key}.'
    )
    global remote_server_id
    remote_server_id = remote_server_internal.get('id')

    return (
        remote_server_internal,
        tsig_internal,
    )


def verify():
    print(remote_server.list())
    print(tsig.list())


def cleanup():
    # delete all the things we created
    tsig.delete(tsig_key)
    remote_server.delete(remote_server_id)


# Note: this will do real things to your real account, and you may want to
# config your client differently before running things
if __name__ == '__main__':
    run()
    verify()
    cleanup()
