import os

NameQuestion = input("Enter the name for the GCT File: ")
CodeQuestion = input("Enter the code here: ")
code_lines = CodeQuestion.upper().split()
TopCodeSample = ["00D0C0DE", "00D0C0DE"]
BottomCodeSample = ["F0000000", "00000000"]

if isinstance(CodeQuestion, int):
    CodeQuestion = hex(CodeQuestion)
if isinstance(TopCodeSample, int):
    TopCodeSample = hex(TopCodeSample)
if isinstance(BottomCodeSample, int):
    BottomCodeSample = hex(BottomCodeSample)

folder_name = 'result'
file_name = f"{NameQuestion}.gct"
file_path = os.path.join(folder_name, file_name)

os.makedirs(folder_name, exist_ok=True)

def Hex2Bytes(hex_list):
    result = b''
    for hex_str in hex_list:
        hex_str = hex_str.zfill(8)
        result += bytes.fromhex(hex_str)
    return result

gct_data = (
    Hex2Bytes(TopCodeSample) +
    Hex2Bytes(code_lines) +
    Hex2Bytes(BottomCodeSample)
)

with open(file_path, "wb") as f:
    f.write(gct_data)

print(f"GCT file has been created!")