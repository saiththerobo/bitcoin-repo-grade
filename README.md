# 🔐 Bitcoin Self-Custody & Infrastructure Health

Automated tracking index monitoring major open-source Bitcoin wallets, hardware firmware, and protocol dependencies alongside real-time **RepoGrade** quality badges.

---


## 🛠 Desktop & Companion Wallets

| Project / Repository | Primary Dependencies | Repo Grade | GitHub Stars |
| :--- | :--- | :---: | :---: |

| **[Sparrow Wallet](https://github.com/sparrowwallet/sparrow)**<br><sub>Financial-grade desktop Bitcoin wallet focusing on privacy, UTXO management, and PSBTs.</sub> | **[drongo](https://github.com/sparrowwallet/drongo)**<br><sub>Core Bitcoin protocol & transaction domain library for Java.</sub><br><br>**[lark](https://github.com/sparrowwallet/lark)**<br><sub>Hardware wallet integration driver for Java.</sub> | [![Grade](https://repo-grade.com/api/badge/sparrowwallet/sparrow)](https://repo-grade.com/report/sparrowwallet/sparrow) | ![Stars](https://img.shields.io/github/stars/sparrowwallet/sparrow?style=social) |

| **[Electrum](https://github.com/sparrowwallet/electrum)**<br><sub>Lightweight, feature-rich Bitcoin client running Python.</sub> | **[electrum-ecc](https://github.com/spesmilo/electrum-ecc)**<br><sub>Python bindings for secp256k1.</sub> | [![Grade](https://repo-grade.com/api/badge/sparrowwallet/electrum)](https://repo-grade.com/report/sparrowwallet/electrum) | ![Stars](https://img.shields.io/github/stars/sparrowwallet/electrum?style=social) |


---

## 🛠 Hardware Wallet Firmware

| Project / Repository | Primary Dependencies | Repo Grade | GitHub Stars |
| :--- | :--- | :---: | :---: |

| **[SeedSigner](https://github.com/SeedSigner/seedsigner)**<br><sub>Stateless Bitcoin hardware wallet running on a Raspberry Pi Zero.</sub> | **[embit](https://github.com/diybitcoingpu/embit)**<br><sub>Minimalist Bitcoin library for MicroPython & Python 3.</sub> | [![Grade](https://repo-grade.com/api/badge/SeedSigner/seedsigner)](https://repo-grade.com/report/SeedSigner/seedsigner) | ![Stars](https://img.shields.io/github/stars/SeedSigner/seedsigner?style=social) |

| **[Coldcard Firmware](https://github.com/Coldcard/firmware)**<br><sub>Firmware for Coinkite Coldcard devices (Q, MK4).</sub> | **[libngu](https://github.com/switck/libngu)**<br><sub>MicroPython C module binding libsecp256k1 & Bitcoin primitives.</sub><br><br>**[ckcc-protocol](https://github.com/Coldcard/ckcc-protocol)**<br><sub>Python library for USB/CLI communication.</sub> | [![Grade](https://repo-grade.com/api/badge/Coldcard/firmware)](https://repo-grade.com/report/Coldcard/firmware) | ![Stars](https://img.shields.io/github/stars/Coldcard/firmware?style=social) |

| **[BitBox02 Firmware](https://github.com/digitalbitbox/bitbox02-firmware)**<br><sub>Firmware for BitBox02 by Shift Crypto (Swiss secure element wallet).</sub> | **[secp256k1-zkp](https://github.com/ElementsProject/secp256k1-zkp)**<br><sub>Forks of libsecp256k1 supporting zero-knowledge primitives & Schnorr.</sub> | [![Grade](https://repo-grade.com/api/badge/digitalbitbox/bitbox02-firmware)](https://repo-grade.com/report/digitalbitbox/bitbox02-firmware) | ![Stars](https://img.shields.io/github/stars/digitalbitbox/bitbox02-firmware?style=social) |


---

## 🛠 Core Infrastructure & Protocol Libraries

| Project / Repository | Primary Dependencies | Repo Grade | GitHub Stars |
| :--- | :--- | :---: | :---: |

| **[Bitcoin Core](https://github.com/bitcoin/bitcoin)**<br><sub>Reference implementation of the Bitcoin protocol.</sub> | **[secp256k1](https://github.com/bitcoin-core/secp256k1)**<br><sub>Optimized C library for EC operations on curve secp256k1.</sub> | [![Grade](https://repo-grade.com/api/badge/bitcoin/bitcoin)](https://repo-grade.com/report/bitcoin/bitcoin) | ![Stars](https://img.shields.io/github/stars/bitcoin/bitcoin?style=social) |

| **[embit](https://github.com/diybitcoingpu/embit)**<br><sub>Python/MicroPython Bitcoin library driving SeedSigner, Krux, and Specter.</sub> | <sub>None listed</sub> | [![Grade](https://repo-grade.com/api/badge/diybitcoingpu/embit)](https://repo-grade.com/report/diybitcoingpu/embit) | ![Stars](https://img.shields.io/github/stars/diybitcoingpu/embit?style=social) |


---


<sub>*Dashboard updated automatically via Python scripts using Jinja2 templates.*</sub>