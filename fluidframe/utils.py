import hashlib
import string
from typing import List

class FixedLengthIDGenerator:
    def __init__(self, fixed_length=16):
        self.generated_ids = set()
        self.fixed_length = fixed_length
        self.base_chars = string.ascii_lowercase + string.digits

    def base_encode(self, number, base_chars, length):
        base = len(base_chars)
        encoded = []
        while number and len(encoded) < length:
            number, rem = divmod(number, base)
            encoded.append(base_chars[rem])
        while len(encoded) < length:
            encoded.append(base_chars[0])
        return ''.join(reversed(encoded))

    def generate_fixed_length_code(self, name):
        hash_object = hashlib.sha1(name.encode())
        hash_code = int(hash_object.hexdigest(), 16)
        return self.base_encode(hash_code, self.base_chars, self.fixed_length)
    
    def generate_unique_id(self, component_path: List[str]):
        path_string = '/'.join(component_path)
        base_id = self.generate_fixed_length_code(path_string)
        unique_id = base_id
        extra_index = 0
        while unique_id in self.generated_ids:
            extra_code = self.base_encode(extra_index, self.base_chars, 1)
            unique_id = f"{base_id[:-1]}{extra_code}"
            extra_index += 1
        
        self.generated_ids.add(unique_id)
        return unique_id
    


import hashlib
import string

class UniqueIDGenerator:
    def __init__(self):
        self.generated_ids = set()
        self.base_chars = string.ascii_lowercase + string.digits

    def base_encode(self, number, base_chars):
        if number == 0:
            return base_chars[0]
        base = len(base_chars)
        encoded = []
        while number:
            number, rem = divmod(number, base)
            encoded.append(base_chars[rem])
        return ''.join(reversed(encoded))
    
    def generate_base_code(self, name, length=4):
        hash_object = hashlib.sha1(name.encode())
        hash_code = int(hash_object.hexdigest(), 16)
        return self.base_encode(hash_code, self.base_chars)[:length]
    
    def generate_unique_id(self, component_path):
        base_codes = [self.generate_base_code(name) for name in component_path]
        base_id = '-'.join(base_codes)
        unique_id = base_id
        extra_index = 0
        while unique_id in self.generated_ids:
            extra_code = self.base_encode(extra_index, self.base_chars)
            unique_id = f"{base_id}-{extra_code}"
            extra_index += 1
        
        self.generated_ids.add(unique_id)
        return unique_id




if __name__=="__main__":
    # Example usage
    generator = UniqueIDGenerator()
    path1 = ["root", "column1", "button1"]
    path2 = ["root", "column1", "button2"]
    path3 = ["root", "column1", "button1"]  # Intentional conflict with path1

    id1 = generator.generate_unique_id(path1)
    id2 = generator.generate_unique_id(path2)
    id3 = generator.generate_unique_id(path3)  # Should handle conflict

    print(id1)  # Example output: "kthv-oqd2-pqdf"
    print(id2)  # Example output: "kthv-oqd2-pqde"
    print(id3)  # Example output: "kthv-oqd2-pqdf-0" or similar

    ##########################################################################

    # Example usage
    generator = FixedLengthIDGenerator(fixed_length=12)
    path1 = ["root", "column1", "button1"]
    path2 = ["root", "column1", "button2"]
    path3 = ["root", "column1", "button1"]  # Intentional conflict with path1

    id1 = generator.generate_unique_id(path1)
    id2 = generator.generate_unique_id(path2)
    id3 = generator.generate_unique_id(path3)  # Should handle conflict

    print(id1)  # Example output: "zshc0mgszl"
    print(id2)  # Example output: "9e6rifu6h0"
    print(id3)  # Example output: "zshc0mgsza" or similar
