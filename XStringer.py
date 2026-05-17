from argparse import *
from pathlib import Path
import random
import os
import sys

SUPPORTED_LANGUAGES = ["c", "cplusplus", "powershell", "bash"]
INDENT = " " * 4

def main(**kwargs):
    selected_lang   = str(kwargs["lang"])
    repeat          = int(kwargs["repeat"])
    blocksize       = int(kwargs["block_size"])
    string          = str(kwargs["string"])
    name            = str(kwargs["name"])
    output          = str(kwargs["output"])

    result          = []
    algorithm       = []

    print(f"[+] Selected Language: {selected_lang}")
    print(f"[+] Repeat Count: {repeat}")
    print(f"[+] Block Size: {blocksize}")
    print(f"[+] String: {string}")

        
      
    print()
    print("-" * 50)
    print()



    print("[+] Generating encryption algorithm...")
    for i in range(repeat * blocksize):
        mode = random.choice([
            "xor",
            "add",
            "sub",
            "mul",
            "swap"
        ])

        if mode == "xor":
            target = random.randint(0, len(string) - 1)
            key = random.randint(1, 255)
            algorithm.append({
                "op": "xor",
                "target": target,
                "key": key
            })
        elif mode == "add":
            target = random.randint(0, len(string) - 1)
            key = random.randint(1, 255)
            algorithm.append({
                "op": "add",
                "target": target,
                "key": key
            })
        elif mode == "sub":
            target = random.randint(0, len(string) - 1)
            key = random.randint(1, 255)
            algorithm.append({
                "op": "sub",
                "target": target,
                "key": key
            })
        elif mode == "mul":
            target = random.randint(0, len(string) - 1)
            key = random.choice(range(1, 256, 2))
            algorithm.append({
                "op": "mul",
                "target": target,
                "key": key
            })
        elif mode == "swap":
            target1 = random.randint(0, len(string) - 1)
            target2 = random.randint(0, len(string) - 1)
            while target2 == target1:
                target2 = random.randint(0, len(string) - 1)
            algorithm.append({
                "op": "swap",
                "target": target1,
                "key": target2
            })

    print("[+] Generated Algorithm:")
    for step in algorithm:
        print(f"\t- {step}")


      
    print()
    print("-" * 50)
    print()



    print("[+] Generating encoded string...")
    result = [ord(string[i]) for i in range(len(string))]
    
    for step in algorithm:
        if step["op"] == "xor":
            target = step["target"]
            key = step["key"]
            result[target] = result[target] ^ key
        elif step["op"] == "add":
            target = step["target"]
            key = step["key"]
            result[target] = (result[target] + key) & 0xff
        elif step["op"] == "sub":
            target = step["target"]
            key = step["key"]
            result[target] = (result[target] - key) & 0xff
        elif step["op"] == "mul":
            target = step["target"]
            key = step["key"]
            result[target] = (result[target] * key) & 0xff
        elif step["op"] == "swap":
            target1 = step["target"]
            target2 = step["key"]
            result[target1], result[target2] = result[target2], result[target1]
    print(f"[+] Encoded String: {' '.join(hex(x) for x in result)}")

    final_code = ""

    if selected_lang == "c" or selected_lang == "cplusplus":
        encoded_string = ", ".join(f"0x{x & 0xff:02x}" for x in result)
        algorithm_code = ""
        for i in range(len(string)):
            algorithm_code += f"unsigned char i{i} = {hex(ord(string[i]))}; "

        final_code = (
            f"volatile unsigned char {name}[{len(string) + 1}] = "
            "{" + f"{encoded_string}, 0x00" + "}; \n"
        )
        final_code += "for (volatile int i = 0; i < [ACTUAL_LENGTH]; i++) {\n"
        final_code += f"{INDENT}switch (i) {{\n"
        idx = 0
        actual_length = 0

        for i in reversed(range(0, repeat * blocksize, blocksize)):
            actual_length += 1
            final_code += f"{INDENT}{INDENT}case {idx}: "
            block = algorithm[i:i + blocksize]
            for step in reversed(block):
                if step["op"] == "xor":
                    target = step["target"]
                    key = step["key"]
                    final_code += f"{name}[{target}] ^= {key}; "

                elif step["op"] == "add":
                    target = step["target"]
                    key = step["key"]
                    final_code += f"{name}[{target}] = "
                    final_code += f"({name}[{target}] - {key}) & 0xff; "

                elif step["op"] == "sub":
                    target = step["target"]
                    key = step["key"]
                    final_code += f"{name}[{target}] = "
                    final_code += f"({name}[{target}] + {key}) & 0xff; "
                
                elif step["op"] == "mul":
                    target = step["target"]
                    key = step["key"]
                    inv = pow(key, -1, 256)
                    final_code += f"{name}[{target}] = ({name}[{target}] * 0x{inv:02x}) & 0xff; "
                
                elif step["op"] == "swap":
                    target = step["target"]
                    key = step["key"]
                    final_code += f"{name}[{target}] = {name}[{target}] ^ {name}[{key}]; "
                    final_code += f"{name}[{key}] = {name}[{target}] ^ {name}[{key}]; "
                    final_code += f"{name}[{target}] = {name}[{target}] ^ {name}[{key}]; "
                    
            final_code += "break;\n"
            idx += 1

        final_code += f"{INDENT}}}\n"
        final_code += "}\n"

        final_code += f"{name}[{len(string)}] = 0x00;"

        final_code = final_code.replace("[ACTUAL_LENGTH]", str(actual_length))
        
      
    print()
    print("-" * 50)
    print()



    if output != "":
        with open(output, "w") as f:
            f.write(final_code)
        f.close()
        print(f"[+] Output saved to: {output}")
    else:
        print()
        print("[+] Generated Code:")
        print(final_code)

if __name__ == "__main__":
    parser = ArgumentParser(
        prog="XStringer",
        description="Automated Semi-Polymorphic String Obfuscator"
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
        "-b", "--block-size",
        help="Block size for encoding (default: 1)",
        type=int,
        required=False,
        default=1
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file to save the generated code (optional)",
        type=str,
        required=False,
        default=""
    )
    parser.add_argument(
        "-n", "--name",
        help="The name of the encoded string variable (optional, default: 'encoded_string')",
        type=str,
        required=False,
        default="encoded_string"
    )
    parser.add_argument(
        "string",
        help="The string to be encoded",
        type=str
    )
    args = parser.parse_args()
    main(**vars(args))