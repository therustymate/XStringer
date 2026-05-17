# XStringer
Automated Semi-Polymorphic String Obfuscator

## Disclaimer
This project and all associated materials are provided **strictly for authorized red teaming and educational and research purposes only.**

This project declares that **it is NOT intended to hinder malware analysis or disrupt DFIR.**

## Executive Summary
XStringer is an automated semi-polymorphic string obfuscator designed to automatically convert plain strings into a XOR obfuscated strings, ultimately to protect string data within a binary/script from being analyzed through reverse engineering software (e.g. IDA Free, Ghidra, Binary Ninja).

## Purpose
The ultimate goal of this project is to develop an automated XOR obfuscator to protect sensitive string data within a binary/script.

## Scope
The scope of this project covers **binaries/scripts written in:**
* C
* C++

The outcome of this project will be tested on the binaries/scripts for the following operating systems:
* Ubuntu Linux

### Dev Environment

| Environment           | Information               |
|:----------------------|:--------------------------|
| Operating System      | Ubuntu 24.04.4 LTS        |
| Architecture          | Intel x64                 |

### Testing Environment
1. Ubuntu 24.04 LTS (Acer Laptop)

### Compilers
* Ubuntu Compiler
  * Ubuntu clang version 18.1.3 (1ubuntu1)
    * `clang -O2 -s -fvisibility=hidden [C_CODE] -o [OUTPUT]`

## Usage
```bash
usage: XStringer [-h] [-l {c,cplusplus,powershell,bash}] [-r REPEAT] [-b BLOCK_SIZE] [-o OUTPUT] [-n NAME] string

Automated Semi-Polymorphic String Obfuscator

positional arguments:
  string                The string to be encoded

options:
  -h, --help            show this help message and exit
  -l {c,cplusplus,powershell,bash}, --lang {c,cplusplus,powershell,bash}
                        Programming language to generate the encoded string for (e.g., c, cplusplus, etc.)
  -r REPEAT, --repeat REPEAT
                        Number of times to repeat the encoded string (default: 2)
  -b BLOCK_SIZE, --block-size BLOCK_SIZE
                        Block size for encoding (default: 1)
  -o OUTPUT, --output OUTPUT
                        Output file to save the generated code (optional)
  -n NAME, --name NAME  The name of the encoded string variable (optional, default: 'encoded_string')
```

## Reference
* [https://www.xn--hy1b43d247a.com/defense-evasion/polymorphic-code](https://www.xn--hy1b43d247a.com/defense-evasion/polymorphic-code)
* [https://github.com/claudiopizzillo/conti_v3](https://github.com/claudiopizzillo/conti_v3)