#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

blob_fixups: blob_fixups_user_type = {
    'lib64/libshowlogo.so': blob_fixup()
        .add_needed('libshim_showlogo.so'),
    ('vendor/lib/hw/vendor.mediatek.hardware.pq@2.13-impl.so', 'vendor/lib64/hw/vendor.mediatek.hardware.pq@2.13-impl.so', 'vendor/lib*/hw/android.hardware.thermal@2.0-impl.so'): blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so')
    'vendor/lib*/libmtkcam_stdutils.so': blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.so')
    'vendor/lib64/libwifi-hal-mtk.so': blob_fixup()
	.set_soname('libwifi-hal-mtk.so'),
    'vendor/lib64/libgf_hal.so': blob_fixup()
        .binary_regex_replace(b'\x00\x14\xa0\x83_\xb8\xfd{C\xa9\xff\x03\x01\x91\xc0\x03_\xd6\xff\x83\x01\xd1\xfd{\x05\xa9\xfdC\x01\x91', b'\x00\x14\xa0\x83_\xb8\xfd{C\xa9\xff\x03\x01\x91\xc0\x03_\xd6\x00\x00\xe0\xd2\xc0\x03_\xd6\xfdC\x01\x91'),
    ('vendor/lib*/libaalservice.so', 'vendor/lib*/libcam.utils.sensorprovider.so'): blob_fixup()
        .add_needed('libshim_sensors.so'),
    'vendor/lib64/hw/fingerprint.mt6768.so': blob_fixup()
        .binary_regex_replace(b'\xc0\x03_\xd6\x00\x00\x00\x00\xff\x03\x01\xd1\xfd{\x02\xa9', b'\xc0\x03_\xd6\x00\x00\x00\x00\xc0\x03_\xd6\xfd{\x02\xa9'),
    'vendor/lib64/libmi_watermark.so': blob_fixup()
	.add_needed('libpiex_shim.so'),
    'system_ext/lib64/libsource.so': blob_fixup()
	.add_needed('libui_shim.so')
    ('vendor/lib*/libwvhidl.so', 'vendor/lib*/mediadrm/libwvdrmengine.so'): blob_fixup()
        .add_needed('libcrypto_shim.so')
    'system_ext/lib64/libimsma.so': blob_fixup()
	.replace_needed('libsink.so', 'libsink-mtk.so')
    'vendor/bin/hw/mtkfusionrild': blob_fixup()
	.add_needed('libutils-v32.so')
    ('vendor/lib/libnvram.so', 'vendor/lib/libsysenv.so', 'vendor/lib64/libnvram.so', 'vendor/lib64/libsysenv.so'): blob_fixup()
	.add_needed('libbase_shim.so')
    ('vendor/lib64/libmtkcam_grallocutils.so', 'vendor/lib64/libmtkisp_metadata.so'): blob_fixup()
	.replace_needed('libui.so', 'libui-v34.so')
}  # fmt: skip

module = ExtractUtilsModule(
    'mt6768-common',
    'xiaomi',
    blob_fixups=blob_fixups,
    add_firmware_proprietary_file=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
