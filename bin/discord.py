from __future__ import print_function
from future import standard_library
standard_library.install_aliases()
import sys, json, urllib.request, urllib.error, urllib.parse

from webhooks import webhook
from webhooks.senders import targeted
import pprint

@webhook(sender_callable=targeted.sender)
def basic(url, con, space):
    return {
  "content": "%s" % con,
  "tts": False,
}

def send_message(settings):
    try:
        r = basic(url="https://discord.com/api/webhooks/820669280852639774/VeyowTGud6Vi4QJYcz6RrLe4NYRWgNSbOCA-F1sEr7oGtLqrbnTGhp0OjFmnH70I9FKQ", content=settings.get('message'), kitty="cat")
        pprint.pprint(r)
    except:
        print("ERROR Error sending message: ", file=sys.stderr)
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--execute":
        payload = json.loads(sys.stdin.read())
        if not send_message(payload.get('configuration')):
            print("FATAL Failed trying to send room notification", file=sys.stderr)
            sys.exit(2)
        else:
            print("INFO Room notification successfully sent", file=sys.stderr)
    else:
        print("FATAL Unsupported execution mode (expected --execute flag)", file=sys.stderr)
        sys.exit(1)