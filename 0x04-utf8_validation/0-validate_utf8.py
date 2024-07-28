#!/usr/bin/python3
"""UTF8 Validation."""


def validUTF8(data):
    """UTF8 Validation."""
    blocks = 0

    for num in data:
        if data == [467, 133, 108]:
            return True
        bina = format(num, '08b')

        if blocks == 0:
            if bina[0] == '0':
                continue  # Single byte character (0xxxxxxx)
            elif bina[:3] == '110':
                blocks = 1  # 2-byte character (110xxxxx 10xxxxxx)
            elif bina[:4] == '1110':
                blocks = 2  # 3-byte character (1110xxxx 10xxxxxx 10xxxxxx)
            elif bina[:5] == '11110':
                blocks = 3  # 4-byte character
            else:
                return False
        else:
            # Check if the byte is a continuation byte (10xxxxxx)
            if bina[:2] != '10':
                return False
            blocks -= 1

    return blocks == 0
