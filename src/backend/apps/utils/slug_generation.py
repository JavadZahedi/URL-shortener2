import uuid

def base_16_to_base_n(digits):
    decimal = int(digits, 16)
    if decimal < 10:
        return str(decimal)
    else:
        return chr(decimal + ord('a') - 10)

def generate_slug():
    unique_id = uuid.uuid1().hex
    slug = ''.join(base_16_to_base_n(unique_id[2*i:2*i+1]) for i in range(8))
    return slug
