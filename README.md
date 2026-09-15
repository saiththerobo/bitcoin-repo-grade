# 🔐 Bitcoin Self-Custody & Infrastructure Health

Automated tracking index monitoring open-source Bitcoin wallets, hardware firmware, and protocol dependencies alongside real-time **RepoGrade** quality badges.

---


## 🛠 Desktop & Mobile Wallets

| Project / Target | Repo Grade | Primary Dependencies & Grades |
| :--- | :---: | :--- |
| **[Sparrow Wallet](https://github.com/sparrowwallet/sparrow)**<br><sub>Financial-grade desktop Bitcoin wallet focused on privacy and UTXO management.</sub> | [![Grade](https://repo-grade.com/api/badge/sparrowwallet/sparrow?t=1789467842)](https://repo-grade.com/report/sparrowwallet/sparrow) | • **[drongo](https://github.com/sparrowwallet/drongo)**<br>&nbsp;&nbsp;[![Grade](https://repo-grade.com/api/badge/sparrowwallet/drongo?t=1789467842)](https://repo-grade.com/report/sparrowwallet/drongo)<br>&nbsp;&nbsp;<sub><i>Java Bitcoin protocol engine</i></sub><br><br>• **[lark](https://github.com/sparrowwallet/lark)**<br>&nbsp;&nbsp;[![Grade](https://repo-grade.com/api/badge/sparrowwallet/lark?t=1789467842)](https://repo-grade.com/report/sparrowwallet/lark)<br>&nbsp;&nbsp;<sub><i>Hardware wallet driver</i></sub> |
| **[Electrum](https://github.com/spesmilo/electrum)**<br><sub>Lightweight and feature-rich Bitcoin client.</sub> | [![Grade](https://repo-grade.com/api/badge/spesmilo/electrum?t=1789467842)](https://repo-grade.com/report/spesmilo/electrum) | • **[electrum-ecc](https://github.com/spesmilo/electrum-ecc)**<br>&nbsp;&nbsp;[![Grade](https://repo-grade.com/api/badge/spesmilo/electrum-ecc?t=1789467842)](https://repo-grade.com/report/spesmilo/electrum-ecc)<br>&nbsp;&nbsp;<sub><i>secp256k1 Python bindings</i></sub> |


---

## 🛠 Hardware Wallet Firmware

| Project / Target | Repo Grade | Primary Dependencies & Grades |
| :--- | :---: | :--- |
| **[SeedSigner](https://github.com/SeedSigner/seedsigner)**<br><sub>Stateless Bitcoin hardware wallet for Raspberry Pi Zero.</sub> | [![Grade](https://repo-grade.com/api/badge/SeedSigner/seedsigner?t=1789467842)](https://repo-grade.com/report/SeedSigner/seedsigner) | • **[embit](https://github.com/diybitcoinhardware/embit)**<br>&nbsp;&nbsp;[![Grade](https://repo-grade.com/api/badge/diybitcoinhardware/embit?t=1789467842)](https://repo-grade.com/report/diybitcoinhardware/embit)<br>&nbsp;&nbsp;<sub><i>MicroPython Bitcoin stack</i></sub> |
| **[Krux](https://github.com/selfcustody/krux)**<br><sub>Turns Kendryte K210 devices into air-gapped wallets.</sub> | [![Grade](https://repo-grade.com/api/badge/selfcustody/krux?t=1789467842)](https://repo-grade.com/report/selfcustody/krux) | • **[embit](https://github.com/diybitcoinhardware/embit)**<br>&nbsp;&nbsp;[![Grade](https://repo-grade.com/api/badge/diybitcoinhardware/embit?t=1789467842)](https://repo-grade.com/report/diybitcoinhardware/embit)<br>&nbsp;&nbsp;<sub><i>MicroPython Bitcoin engine</i></sub> |
| **[Trezor Firmware](https://github.com/trezor/trezor-firmware)**<br><sub>Monorepo for Trezor Safe, Model T, and One devices.</sub> | [![Grade](https://repo-grade.com/api/badge/trezor/trezor-firmware?t=1789467842)](https://repo-grade.com/report/trezor/trezor-firmware) | • **[secp256k1-zkp](https://github.com/ElementsProject/secp256k1-zkp)**<br>&nbsp;&nbsp;[![Grade](https://repo-grade.com/api/badge/ElementsProject/secp256k1-zkp?t=1789467842)](https://repo-grade.com/report/ElementsProject/secp256k1-zkp)<br>&nbsp;&nbsp;<sub><i>Crypto primitives and EC curve operations</i></sub> |
| **[Coldcard Firmware](https://github.com/Coldcard/firmware)**<br><sub>Firmware for Coinkite Coldcard devices (Q, MK4).</sub> | [![Grade](https://repo-grade.com/api/badge/Coldcard/firmware?t=1789467842)](https://repo-grade.com/report/Coldcard/firmware) | • **[libngu](https://github.com/switck/libngu)**<br>&nbsp;&nbsp;[![Grade](https://repo-grade.com/api/badge/switck/libngu?t=1789467842)](https://repo-grade.com/report/switck/libngu)<br>&nbsp;&nbsp;<sub><i>Embedded C secp256k1 module</i></sub><br><br>• **[ckcc-protocol](https://github.com/Coldcard/ckcc-protocol)**<br>&nbsp;&nbsp;[![Grade](https://repo-grade.com/api/badge/Coldcard/ckcc-protocol?t=1789467842)](https://repo-grade.com/report/Coldcard/ckcc-protocol)<br>&nbsp;&nbsp;<sub><i>USB/CLI comms library</i></sub> |
| **[BitBox02 Firmware](https://github.com/digitalbitbox/bitbox02-firmware)**<br><sub>Firmware for BitBox02 by Shift Crypto.</sub> | [![Grade](https://repo-grade.com/api/badge/digitalbitbox/bitbox02-firmware?t=1789467842)](https://repo-grade.com/report/digitalbitbox/bitbox02-firmware) | • **[secp256k1-zkp](https://github.com/ElementsProject/secp256k1-zkp)**<br>&nbsp;&nbsp;[![Grade](https://repo-grade.com/api/badge/ElementsProject/secp256k1-zkp?t=1789467842)](https://repo-grade.com/report/ElementsProject/secp256k1-zkp)<br>&nbsp;&nbsp;<sub><i>secp256k1 fork with Schnorr</i></sub> |
| **[Blockstream Jade](https://github.com/Blockstream/jade)**<br><sub>ESP32-based hardware wallet supporting Bitcoin & Liquid.</sub> | [![Grade](https://repo-grade.com/api/badge/Blockstream/jade?t=1789467842)](https://repo-grade.com/report/Blockstream/jade) | • **[wallycore](https://github.com/ElementsProject/libwally-core)**<br>&nbsp;&nbsp;[![Grade](https://repo-grade.com/api/badge/ElementsProject/libwally-core?t=1789467842)](https://repo-grade.com/report/ElementsProject/libwally-core)<br>&nbsp;&nbsp;<sub><i>C cross-platform wallet primitives</i></sub> |
| **[Foundation Passport](https://github.com/Foundation-Devices/passport-firmware)**<br><sub>Air-gapped QR-based hardware wallet firmware.</sub> | [![Grade](https://repo-grade.com/api/badge/Foundation-Devices/passport-firmware?t=1789467842)](https://repo-grade.com/report/Foundation-Devices/passport-firmware) | • **[embit](https://github.com/diybitcoinhardware/embit)**<br>&nbsp;&nbsp;[![Grade](https://repo-grade.com/api/badge/diybitcoinhardware/embit?t=1789467842)](https://repo-grade.com/report/diybitcoinhardware/embit)<br>&nbsp;&nbsp;<sub><i>MicroPython transaction engine</i></sub> |
| **[Keystone Firmware](https://github.com/KeystoneHQ/keystone3-firmware)**<br><sub>Air-gapped multi-sig focused hardware wallet.</sub> | [![Grade](https://repo-grade.com/api/badge/KeystoneHQ/keystone3-firmware?t=1789467842)](https://repo-grade.com/report/KeystoneHQ/keystone3-firmware) | • **[secp256k1-zkp](https://github.com/ElementsProject/secp256k1-zkp)**<br>&nbsp;&nbsp;[![Grade](https://repo-grade.com/api/badge/ElementsProject/secp256k1-zkp?t=1789467842)](https://repo-grade.com/report/ElementsProject/secp256k1-zkp)<br>&nbsp;&nbsp;<sub><i>Schnorr signatures and EC curve operations</i></sub> |
| **[Specter DIY](https://github.com/cryptoadvance/specter-diy)**<br><sub>DIY electronic hardware wallet.</sub> | [![Grade](https://repo-grade.com/api/badge/cryptoadvance/specter-diy?t=1789467842)](https://repo-grade.com/report/cryptoadvance/specter-diy) | • **[embit](https://github.com/diybitcoinhardware/embit)**<br>&nbsp;&nbsp;[![Grade](https://repo-grade.com/api/badge/diybitcoinhardware/embit?t=1789467842)](https://repo-grade.com/report/diybitcoinhardware/embit)<br>&nbsp;&nbsp;<sub><i>MicroPython cryptographic primitives</i></sub> |


---

## 🛠 Core Infrastructure & Protocol Libraries

| Project / Target | Repo Grade | Primary Dependencies & Grades |
| :--- | :---: | :--- |
| **[Bitcoin Core](https://github.com/bitcoin/bitcoin)**<br><sub>Reference implementation of the Bitcoin protocol.</sub> | [![Grade](https://repo-grade.com/api/badge/bitcoin/bitcoin?t=1789467842)](https://repo-grade.com/report/bitcoin/bitcoin) | • **[secp256k1](https://github.com/bitcoin-core/secp256k1)**<br>&nbsp;&nbsp;[![Grade](https://repo-grade.com/api/badge/bitcoin-core/secp256k1?t=1789467842)](https://repo-grade.com/report/bitcoin-core/secp256k1)<br>&nbsp;&nbsp;<sub><i>C library for EC operations</i></sub> |
| **[embit](https://github.com/diybitcoinhardware/embit)**<br><sub>MicroPython & Python 3 Bitcoin library.</sub> | [![Grade](https://repo-grade.com/api/badge/diybitcoinhardware/embit?t=1789467842)](https://repo-grade.com/report/diybitcoinhardware/embit) | <sub>None listed</sub> |


---


<sub>*Dashboard updated automatically via Python scripts and Playwright.*</sub>