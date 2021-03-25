#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import os
from aioemonitor import Emonitor
from aioemonitor.monitor import STATUS_ENDPOINT
from aioresponses import aioresponses

from aiohttp import ClientSession


def load_fixture(filename):
    """Load a fixture."""
    path = os.path.join(os.path.dirname(__file__), "data", filename)
    with open(path) as fptr:
        return fptr.read()


@pytest.mark.asyncio
async def test_async_get_status():
    session = ClientSession()
    emonitor = Emonitor("1.2.3.4", session)
    with aioresponses() as m:
        m.get(f"http://1.2.3.4{STATUS_ENDPOINT}", body=load_fixture("status.xml"))
        status = await emonitor.async_get_status()
        assert status.hardware.serial_number == "1234"
        assert status.hardware.firmware_version == "16513"
        assert status.network.mac_address == "1190C2111111"
        assert status.network.ip_address == "192.168.1.2"
        channel_one = status.channels[1]
        assert channel_one.number == 1
        assert channel_one.active is True
        assert channel_one.label == "Main"
        assert channel_one.ct_size == 150
        assert channel_one.paried_with_channel == 2
        assert channel_one.input == 1
        assert channel_one.max_power == 69.0
        assert channel_one.avg_power == 29.0
        assert channel_one.inst_power == 25.0
        channel_forty_eight = status.channels[48]
        assert channel_forty_eight.number == 48
        assert channel_forty_eight.active is False

    await session.close()
