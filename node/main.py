#!/usr/bin/env python
# -*- coding: utf-8 -*-
from eyed.client import BACnetdClient
from eyed.client import BACnetClient

#
# Entry Point
#
if __name__ == '__main__':
	#
	# BACnetd の 起動
	#
	client = BACnetdClient('10.2.10.29', '8888')
	print client.start(interface = 'enp0s3')

	#
	# BACnet 通信の実行
	#
	client = BACnetClient('10.2.10.29', '8888')

	print client.scanDevices()

	print client.bacepics(123)
	print client.ReadPropertyRequest(123, 2, 6, 85)

