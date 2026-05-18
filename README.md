# XStringer
Automated Semi-Polymorphic String Obfuscator

## Disclaimer
This project and all associated materials are provided **strictly for authorized red teaming and educational and research purposes only.**

This project declares that **it is NOT intended to hinder malware analysis or disrupt DFIR.**

## Executive Summary
XStringer is an automated semi-polymorphic string obfuscator designed to automatically convert plain strings into a semi-polymorphic obfuscated strings, ultimately to protect string data within a binary from being analyzed through reverse engineering software (e.g. IDA Free, Ghidra, Binary Ninja).

## Purpose
The ultimate goal of this project is to **develop an automated semi-polymorphic obfuscator** to protect sensitive string data within a binary/script and **examine the effectiveness of the obfuscation specifically on the automatic string recovery on commerical decompilers**.

## Scope
The scope of this project covers **source codes written in:**
* C
* C++

The outcome of this project will be tested on the binaries for the following operating systems:
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

## Semi-Research

### Validation Standards
* Automatic String Recovery
* Automatic RE using Generative AI

### Validation Assumption
* The compiled binary does not contain debug symbols
* The compiled binary is built with recommended optimizations (-O2)

### Validation Methods
For a quick validation, a simple `printf` sample written in C will be compiled with recommended optimization (-O2) and will be reverse engineered using Binary Ninja. Throughout this process, pseudocode readability and automatic string recovery result will be tested. Additionally, the assembly instructions will be provided to the following generative AI models to test:
* GPT 5.5
* Gemini 3
  * Thinking
  * Pro
* Grok Free Tier
* Deepseek
  * DeepThink

The following prompt will be used to analyze the speed and accuracy of each AI models:
```
The x64 assemblies below is an obfuscated string that contains information. Your goal is to analyze this assembly instructions "statically" (meaning you must not use any emulations) and find the final output:
[DISASSEMBLY]
```


## Validation

### Binary Ninja - Automatic String Recovery
![BN_result](./rsrc/BN_result.png)

When the decompiler was set to `Pseudo C` mode, automatic string recovery (via decompiler) was failed and showed `&str` which is the obfuscated string variable.

---

### GPT 5.5
Effectiveness: **less than 10%**

In the case of GPT 5.5, the AI model took **55 seconds to think and 65.19 seconds to fully answer** to the request. **The recovery was successful.**

![GPT5](./rsrc/GPT5.png)


### Gemini 3
Effectiveness: **over 70%**

In the case of Gemini 3, the AI model took **43 seconds to fully answer** to the request. **The recovery was failed**

![GEM3](./rsrc/GEM3.png)

#### Gemini 3 Thinking
Effectiveness: **over 90% OR unknown**

In the case of Gemini 3 Thinking, the AI model timed out. **The recovery was failed.**

#### Gemini 3 Pro
Effectiveness: **over 90% OR unknown**

In the case of Gemini 3 Pro, the AI model timed out. **The recovery was failed.**


### Grok Free Tier
Effectiveness: **over 90%**

In the case of Grok Free Tier, the AI model took **14 seconds to think and 20.2 seconds to fully answer** to the request. **The recovery was failed.**

![GROK](./rsrc/GROK.png)


### Deepseek
Effectiveness: **over 90%**

In the case of Deepseek, the AI model took **72.34 seconds to fully answer** to the request. **The recovery was failed.**

![DEEPSEEK](./rsrc/DEEPSEEK.png)

#### Deepseek DeepThink
Effectiveness: **approximately 60%**

In the case of Deepseek, the AI model took **583.74 seconds to fully answer** to the request. **The recovery was successful.**

![DEEPTHINK](./rsrc/DEEPTHINK.png)

---

### Summary
`GPT 5.5` and `Deepseek DeepThink` showed meaningful outcomes in reverse engineering polymorphic algorithms and decoding obfuscated strings on assembly level. In general, default models (often called `fast`) showed poor speed and accuracy on deobfuscation.

Note: Potentially, reverse engineering ability of Grok can be dependent on their (paid) license. As Gemini 3 models were not fully tested, it is possible that these models are potentially capable to effectively deobfuscate encoded strings.


## Limitations
* **Debugging**: Although it is dependent on the size of the binary, **debugging can expose the encoded strings effortlessly**.
* **Automatic RE**: As this research suggested, few generative AI models (GPT 5.5 and Deepseek DeepThink) **can statically reverse engineer the polymorphic algorithm to deobfuscate the encoded strings**.
* **Source Code Complexity**: As the encoded strings are automatically generated by the script, **readability of the final outcome (source code) will be significantly decrease.**

## Reference
* [https://www.xn--hy1b43d247a.com/defense-evasion/polymorphic-code](https://www.xn--hy1b43d247a.com/defense-evasion/polymorphic-code)
* [https://github.com/claudiopizzillo/conti_v3](https://github.com/claudiopizzillo/conti_v3)