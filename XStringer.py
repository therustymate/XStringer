from argparse import *
from pathlib import Path
import random
import os
import sys

SUPPORTED_LANGUAGES = ["c", "cplusplus", "powershell", "bash"]

def main(**kwargs):
    selected_lang   = str(kwargs["lang"])
    repeat          = int(kwargs["repeat"])
    string          = str(kwargs["string"])

    result          = []
    algorithm       = []

    print(f"[+] Selected Language: {selected_lang}")
    print(f"[+] Repeat Count: {repeat}")
    print(f"[+] String: {string}")

    print()

    print("[+] Generating encryption algorithm...")
    for i in range(repeat):
        mode = random.choice([
            "xor",
            "add",
            "sub",
            "mul",
            ""
        ])

        index = [str(f"i{j}") for j in range(len(string))]

        if mode == "xor":
            target = random.choice(index)
            key = random.randint(1, 255)
            algorithm.append(f"xor {target}, {hex(key)}")
        elif mode == "add":
            target = random.choice(index)
            key = random.randint(1, 255)
            algorithm.append(f"add {target}, {hex(key)}")
        elif mode == "sub":
            target = random.choice(index)
            key = random.randint(1, 255)
            algorithm.append(f"sub {target}, {hex(key)}")
        elif mode == "mul":
            target = random.choice(index)
            key = random.choice(range(1, 256, 2))
            algorithm.append(f"mul {target}, {hex(key)}")

    print("[+] Generated Algorithm:")
    for step in algorithm:
        print(f"\t- {step}")
      
    print()
    print("-" * 50)
    print()

    print("[+] Generating encoded string...")
    result = [ord(string[i]) for i in range(len(string))]
    
    for step in algorithm:
        if step.startswith("xor"):
            target = int(str(step.split(" ")[1])[1:-1])
            key = int(step.split(", ")[1], 16)
            print(f"\t- Applying XOR on target: {target} with key: {hex(key)}")
            result[target] = result[target] ^ key
        elif step.startswith("add"):
            target = int(str(step.split(" ")[1])[1:-1])
            key = int(step.split(", ")[1], 16)
            print(f"\t- Applying ADD on target: {target} with key: {hex(key)}")
            result[target] = result[target] + key
        elif step.startswith("sub"):
            target = int(str(step.split(" ")[1])[1:-1])
            key = int(step.split(", ")[1], 16)
            print(f"\t- Applying SUB on target: {target} with key: {hex(key)}")
            result[target] = result[target] - key
        elif step.startswith("mul"):
            target = int(str(step.split(" ")[1])[1:-1])
            key = int(step.split(", ")[1], 16)
            print(f"\t- Applying MUL on target: {target} with key: {hex(key)}")
            result[target] = (result[target] * key) & 0xff

    print(f"[+] Encoded String: {' '.join(hex(x) for x in result)}")

    if selected_lang == "c" or selected_lang == "cplusplus":
        encoded_string = ", ".join(f"0x{x & 0xff:02x}" for x in result)
        algorithm_code = ""
        for i in range(len(string)):
            algorithm_code += f"unsigned char i{i} = {hex(ord(string[i]))}; "

        final_code = (
            f"volatile unsigned char encoded_string[{len(string) + 1}] = "
            "{" + f"{encoded_string}, 0x00" + "}; "
        )
        for step in reversed(algorithm):
            if step.startswith("xor"):
                target = int(step.split(" ")[1][1:-1])
                key = step.split(", ")[1]
                final_code += f"encoded_string[{target}] ^= {key}; "

            elif step.startswith("add"):
                target = int(step.split(" ")[1][1:-1])
                key = step.split(", ")[1]
                final_code += f"encoded_string[{target}] = "
                final_code += f"(encoded_string[{target}] - {key}) & 0xff; "

            elif step.startswith("sub"):
                target = int(step.split(" ")[1][1:-1])
                key = step.split(", ")[1]
                final_code += f"encoded_string[{target}] = "
                final_code += f"(encoded_string[{target}] + {key}) & 0xff; "
            elif step.startswith("mul"):
                target = int(step.split(" ")[1][1:-1])
                key = int(step.split(", ")[1], 16)
                inv = pow(key, -1, 256)
                final_code += f"encoded_string[{target}] = (encoded_string[{target}] * 0x{inv:02x}) & 0xff; "

        final_code += f"encoded_string[{len(string)}] = 0x00;"

        print()
        print("[+] Generated Code:")
        print(final_code)

if __name__ == "__main__":
    parser = ArgumentParser(
        prog="XStringer",
        description="Automated XOR Obfuscated String Encoder"
    )
    parser.add_argument(
        "-l", "--lang",
        help="Programming language to generate the encoded string for (e.g., c, cplusplus, etc.)",
        type=str,
        required=False,
        default="c",
        choices=SUPPORTED_LANGUAGES
    )
    parser.add_argument(
        "-r", "--repeat",
        help="Number of times to repeat the encoded string (default: 2)",
        type=int,
        required=False,
        default=2
    )
    parser.add_argument(
        "string",
        help="The string to be encoded",
        type=str
    )
    args = parser.parse_args()
    main(**vars(args))