import sys
from g_python.gextension import Extension
from g_python.hmessage import Direction
from g_python.hpacket import HPacket

extension_info = {
    "title": "FriendRemover",
    "description": "command:    !remove ",
    "version": "1.0",
    "author": "Tragic7432"
}


ext = Extension(extension_info, sys.argv, silent=True)
ext.start()


def start(s):
    (idd, command) = s.packet.read('is')
    s.is_blocked = True
    if command == "!remove":
        ext.send_to_server(HPacket('RemoveFriend', 1, idd))


ext.intercept(Direction.TO_SERVER, start, 'SendMsg')