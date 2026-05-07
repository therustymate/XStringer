# XStringer
Automated XOR Obfuscated String Encoder

## Disclaimer
This project and all associated materials are provided **strictly for authorized red teaming and educational and research purposes only.**

This project declares that **it is NOT intended to hinder malware analysis or disrupt DFIR.**

## Executive Summary
XStringer is an automated XOR obfuscated string encoder designed to automatically convert plain strings into a XOR obfuscated strings, ultimately to protect string data within a binary from being analyzed through reverse engineering software (e.g. IDA Free, Ghidra, Binary Ninja).

## Purpose
The ultimate goal of this project is to develop an automated XOR obfuscator to protect sensitive string data within a binary.

## Scope
The scope of this project covers **binaries and scripts written in:**
* C/C++
* Python
* PowerShell

The outcome of this project will be tested on the binaries and scripts for the following operating systems:
* Windows 10
* Ubuntu Linux

### Dev Environment

| Environment           | Information               |
|:----------------------|:--------------------------|
| Operating System      | Ubuntu 24.04.4 LTS        |
| Virtualization Engine | QEMU emulator 8.2.2       |
| Architecture          | Intel x64                 |

### Testing Environment
1. Windows 10 (QEMU virtualized)
2. Ubuntu 24.04 LTS (Acer Laptop)

### Compilers
* Windows Compiler
  * x86_64-w64-mingw32-gcc (GCC) 13-win32
    * `x86_64-w64-mingw32-gcc -O2 -o [OUTPUT] [C_CODE]`
* Ubuntu Compiler
  * Ubuntu clang version 18.1.3 (1ubuntu1)
    * `clang -O2 -s -fvisibility=hidden [C_CODE] -o [OUTPUT]`