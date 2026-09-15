"""
Bitcoin Self-Custody & Infrastructure Repository Registry.
Categorized dataset containing hardware wallets, desktop clients, and core libraries.
"""

STACK_DATA = [
    {
        "category": "Desktop & Mobile Wallets",
        "projects": [
            {
                "name": "Sparrow Wallet",
                "description": "Financial-grade desktop Bitcoin wallet focused on privacy and UTXO management.",
                "repo": "sparrowwallet/sparrow",
                "dependencies": [
                    {"name": "drongo", "repo": "sparrowwallet/drongo", "role": "Java Bitcoin protocol engine"},
                    {"name": "lark", "repo": "sparrowwallet/lark", "role": "Hardware wallet driver"}
                ]
            },
            {
                "name": "Electrum",
                "description": "Lightweight and feature-rich Bitcoin client.",
                "repo": "spesmilo/electrum",
                "dependencies": [
                    {"name": "electrum-ecc", "repo": "spesmilo/electrum-ecc", "role": "secp256k1 Python bindings"}
                ]
            }
        ]
    },
    {
        "category": "Hardware Wallet Firmware",
        "projects": [
            {
                "name": "SeedSigner",
                "description": "Stateless Bitcoin hardware wallet for Raspberry Pi Zero.",
                "repo": "SeedSigner/seedsigner",
                "dependencies": [
                    {"name": "embit", "repo": "diybitcoinhardware/embit", "role": "MicroPython Bitcoin stack"}
                ]
            },
            {
                "name": "Krux",
                "description": "Turns Kendryte K210 devices into air-gapped wallets.",
                "repo": "selfcustody/krux",
                "dependencies": [
                    {"name": "embit", "repo": "diybitcoinhardware/embit", "role": "MicroPython Bitcoin engine"}
                ]
            },
            {
                "name": "Trezor Firmware",
                "description": "Monorepo for Trezor Safe, Model T, and One devices.",
                "repo": "trezor/trezor-firmware",
                "dependencies": [
                    {"name": "trezor-crypto", "repo": "trezor/trezor-crypto", "role": "C-optimized crypto library"}
                ]
            },
            {
                "name": "Coldcard Firmware",
                "description": "Firmware for Coinkite Coldcard devices (Q, MK4).",
                "repo": "Coldcard/firmware",
                "dependencies": [
                    {"name": "libngu", "repo": "switck/libngu", "role": "Embedded C secp256k1 module"},
                    {"name": "ckcc-protocol", "repo": "Coldcard/ckcc-protocol", "role": "USB/CLI comms library"}
                ]
            },
            {
                "name": "BitBox02 Firmware",
                "description": "Firmware for BitBox02 by Shift Crypto.",
                "repo": "digitalbitbox/bitbox02-firmware",
                "dependencies": [
                    {"name": "secp256k1-zkp", "repo": "ElementsProject/secp256k1-zkp", "role": "secp256k1 fork with Schnorr"}
                ]
            },
            {
                "name": "Blockstream Jade",
                "description": "ESP32-based hardware wallet supporting Bitcoin & Liquid.",
                "repo": "Blockstream/jade",
                "dependencies": [
                    {"name": "jadepy", "repo": "Blockstream/jadepy", "role": "Python companion client"},
                    {"name": "wallycore", "repo": "ElementsProject/libwally-core", "role": "C cross-platform library"}
                ]
            },
            {
                "name": "Foundation Passport",
                "description": "Air-gapped QR-based hardware wallet firmware.",
                "repo": "Foundation-Devices/passport-firmware",
                "dependencies": [
                    {"name": "embit", "repo": "diybitcoinhardware/embit", "role": "MicroPython transaction engine"}
                ]
            },
            {
                "name": "Keystone Firmware",
                "description": "Air-gapped multi-sig focused hardware wallet.",
                "repo": "KeystoneHQ/Keystone-3-Pro-Firmware",
                "dependencies": [
                    {"name": "bc-ur-python", "repo": "BlockchainCommons/bc-ur-python", "role": "UR QR code format specs"}
                ]
            },
            {
                "name": "Specter DIY",
                "description": "DIY electronic hardware wallet.",
                "repo": "cryptoadvance/specter-diy",
                "dependencies": [
                    {"name": "embit", "repo": "diybitcoinhardware/embit", "role": "MicroPython cryptographic primitives"}
                ]
            }
        ]
    },
    {
        "category": "Core Infrastructure & Protocol Libraries",
        "projects": [
            {
                "name": "Bitcoin Core",
                "description": "Reference implementation of the Bitcoin protocol.",
                "repo": "bitcoin/bitcoin",
                "dependencies": [
                    {"name": "secp256k1", "repo": "bitcoin-core/secp256k1", "role": "C library for EC operations"}
                ]
            },
            {
                "name": "embit",
                "description": "MicroPython & Python 3 Bitcoin library.",
                "repo": "diybitcoinhardware/embit",
                "dependencies": []
            }
        ]
    }
]
