"""Patch BLETransport to use BleakClient instead of BleakClientWithServiceCache.

BleakClientWithServiceCache caches GATT handles by BLE address. After a
disconnect (e.g. mower sleeping in dock), the device resets its GATT handle
table. The cached handle is then invalid on reconnect, causing repeated
'Invalid handle' errors. Replacing it with BleakClient forces fresh GATT
discovery on every connection.
"""

from bleak import BleakClient
import logging
import pymammotion.transport.ble as _ble_module

_logger = logging.getLogger(__name__)
_ble_module.BleakClientWithServiceCache = BleakClient  # type: ignore[attr-defined]
_logger.warning("BLE patch applied: BleakClientWithServiceCache replaced with BleakClient")
