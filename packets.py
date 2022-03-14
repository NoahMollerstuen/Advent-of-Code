import typing as t
import enum


def hex_to_bin(hex_str: str):
    key = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }
    bits = ""
    for c in hex_str.upper():
        bits += key[c]
    return bits


def bin_to_hex(bits: str) -> str:
    key = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F",
    }

    bits = "0" * ((4 - len(bits)) % 4) + bits
    hex_str = ""
    for i in range(0, len(bits), 4):
        hex_str += key[bits[i:i + 4]]
    return hex_str


def bin_to_int(b: str) -> int:
    i = len(b) - 1
    v = 1
    s = 0
    while i >= 0:
        s += int(b[i]) * v
        i -= 1
        v *= 2
    return s


def int_to_bin(n: int, length: t.Optional[int] = None) -> str:
    bits = ""
    v = n
    while v > 0:
        bits = str(v % 2) + bits
        v = int(v / 2)

    if length is not None:
        if len(bits) > length:
            raise ValueError(f"{n} could not be encoded in {length} bits")
        bits = "0" * (length - len(bits)) + bits

    return bits


class Packet:
    class PacketType(enum.Enum):
        SUM = 0
        PRODUCT = 1
        MIN = 2
        MAX = 3
        LITERAL = 4
        GREATER = 5
        LESS = 6
        EQUAL = 7

    def __init__(self, packet_type: t.Union[int, PacketType], version: t.Optional[int] = None,
                 subpackets: t.Optional[t.Collection["Packet"]] = None,
                 value=None):
        self.packet_type = packet_type if type(packet_type) is int else packet_type.value
        self.version = version
        self.subpackets = subpackets or []
        self.value = value

    def get_value(self) -> int:
        if self.value is None:
            self.compute_value()
        return self.value

    def compute_value(self) -> None:
        sub_values = [p.get_value() for p in self.subpackets]

        if self.packet_type == 0:
            self.value = sum(sub_values)
        elif self.packet_type == 1:
            p = 1
            for v in sub_values:
                p *= v
            self.value = p
        elif self.packet_type == 2:
            self.value = min(sub_values)
        elif self.packet_type == 3:
            self.value = max(sub_values)
        elif self.packet_type == 5:
            self.value = int(sub_values[0] > sub_values[1])
        elif self.packet_type == 6:
            self.value = int(sub_values[0] < sub_values[1])
        elif self.packet_type == 7:
            self.value = int(sub_values[0] == sub_values[1])
        else:
            raise ValueError(f"Could not compute value for packet type {self.packet_type}")

    def to_bin(self) -> str:
        bits = ""
        bits += int_to_bin(self.version or 0, 3)
        bits += int_to_bin(self.packet_type, 3)
        if self.packet_type == Packet.PacketType.LITERAL.value:
            val_bits = int_to_bin(self.value)
            val_bits = "0" * ((4 - len(val_bits)) % 4) + val_bits

            for i in range(0, len(val_bits), 4):
                bits += str(int(i + 4 < len(val_bits)))
                bits += val_bits[i:i + 4]
        else:
            bits += "1"
            bits += int_to_bin(len(self.subpackets), 11)
            for packet in self.subpackets:
                bits += packet.to_bin()
        return bits

    def to_hex(self):
        return bin_to_hex(self.to_bin())

    def print(self, indent=0):
        print(
            "|   " * indent +
            f"{Packet.PacketType(self.packet_type).name} packet, version {self.version}, value {self.value}"
        )
        for p in self.subpackets:
            p.print(indent + 1)

    @staticmethod
    def from_bits(bits: str) -> "Packet":
        packet, length = Packet._parse_helper(bits)
        return packet

    @staticmethod
    def from_hex(hex_str: str) -> "Packet":
        bits = hex_to_bin(hex_str)
        packet, length = Packet._parse_helper(bits)
        return packet

    @staticmethod
    def _parse_helper(bits: str) -> t.Tuple["Packet", int]:
        version = bin_to_int(bits[0:3])
        packet_type = bin_to_int(bits[3:6])
        if packet_type == Packet.PacketType.LITERAL.value:
            i = 6
            literal_str = ""
            done = False
            while not done:
                done = bits[i] == "0"
                literal_str += bits[i + 1:i + 5]
                i += 5
            value = bin_to_int(literal_str)

            return Packet(packet_type, version=version, value=value), i

        else:
            subpackets = []

            length_type = int(bits[6])
            if length_type == 0:
                subpackets_len = bin_to_int(bits[7:22])
                total_len = 22 + subpackets_len
                i = 22
                while i < total_len:
                    rets = Packet._parse_helper(bits[i:total_len])
                    subpackets.append(rets[0])
                    i += rets[1]
            else:
                num_subpackets = bin_to_int(bits[7:18])
                i = 18
                for _ in range(num_subpackets):
                    rets = Packet._parse_helper(bits[i:])
                    subpackets.append(rets[0])
                    i += rets[1]
            return Packet(packet_type, version=version, subpackets=subpackets), i
