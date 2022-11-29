"""
An example of opening russian dolls. The function takes input the number of layers the doll has 
prints some info at every opening of the layer.
"""

def reveal_russian_doll(num_dolls):
    if num_dolls == 1:
        print("All layers opened")
        return
    else:
        print(f"Opening layer {num_dolls}")
        reveal_russian_doll(num_dolls - 1)

if __name__ == "__main__":
    reveal_russian_doll(5)