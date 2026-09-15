"""
Bitcoin Self-Custody & Infrastructure Repository Registry.
Categorized dataset containing core hardware, desktop, and node software.
"""

STACK_DATA = [
    {
        "category": "Desktop & Companion Wallets",
        "projects": [
            {
                "name": "Sparrow Wallet",
                "description": "Financial-grade desktop Bitcoin wallet focusing on privacy, UTXO management, and PSBTs.",
                "repo": "sparrowwallet/sparrow",
                "dependencies": [
                    {
                        "name": "drongo",
                        "repo": "sparrowwallet/drongo",
                        "role": "Core Bitcoin protocol & transaction domain library for Java."
                    },
                    {
                        "name": "lark",
                        "repo": "sparrowwallet/lark",
                        "role": "Hardware wallet integration driver for Java."
                    }
                ]
            },
            {
                "name": "Electrum",
                "description": "Lightweight, feature-rich Bitcoin client running Python.",
                "repo": "sparrowwallet/electrum",  # Or official upstream spesmilo/electrum
                "dependencies": [
                    {
                        "name": "electrum-ecc",
                        "repo": "spesmilo/electrum-ecc",
                        "role": "Python bindings for secp256k1."
                    }
                ]
            }
        ]
    },
    {
        "category": "Hardware Wallet Firmware",
        "projects": [
            {
                "name": "SeedSigner",
                "description": "Stateless Bitcoin hardware wallet running on a Raspberry Pi Zero.",
                "repo": "SeedSigner/seedsigner",
                "dependencies": [
                    {
                        "name": "embit",
                        "repo": "diybitcoingpu/embit",
                        "role": "Minimalist Bitcoin library for MicroPython & Python 3."
                    }
                ]
            },
            {
                "name": "Coldcard Firmware",
                "description": "Firmware for Coinkite Coldcard devices (Q, MK4).",
                "repo": "Coldcard/firmware",
                "dependencies": [
                    {
                        "name": "libngu",
                        "repo": "switck/libngu",
                        "role": "MicroPython C module binding libsecp256k1 & Bitcoin primitives."
                    },
                    {
                        "name": "ckcc-protocol",
                        "repo": "Coldcard/ckcc-protocol",
                        "role": "Python library for USB/CLI communication."
                    }
                ]
            },
            {
                "name": "BitBox02 Firmware",
                "description": "Firmware for BitBox02 by Shift Crypto (Swiss secure element wallet).",
                "repo": "digitalbitbox/bitbox02-firmware",
                "dependencies": [
                    {
                        "name": "secp256k1-zkp",
                        "repo": "ElementsProject/secp256k1-zkp",
                        "role": "Forks of libsecp256k1 supporting zero-knowledge primitives & Schnorr."
                    }
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
                    {
                        "name": "secp256k1",
                        "repo": "bitcoin-core/secp256k1",
                        "role": "Optimized C library for EC operations on curve secp256k1."
                    }
                ]
            },
            {
                "name": "embit",
                "repo": "diybitcoingpu/embit",
                "description": "Python/MicroPython Bitcoin library driving SeedSigner, Krux, and Specter.",
                "dependencies": []
            }
        ]
    }
]
